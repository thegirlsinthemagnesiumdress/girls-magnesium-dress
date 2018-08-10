from api.serializers import (
    SurveyCompanyNameSerializer,
    SurveyResultSerializer,
    SurveySerializer,
)
from core.models import Survey, SurveyResult
from core.qualtrics import benchmark
from django.conf import settings
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateSurveyView(CreateAPIView):
    """
    Internal API endpoint to create a survey and return the created survey data including both link and link_sponsor.
    """
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class SurveyCompanyNameFromUIDView(RetrieveAPIView):
    """
    External API endpoint to get the company name given a UID.
    Must use `sid` GET param to specify company: e.g. ?sid=a95c7b47c8e2e1d057c56d114bb2862c
    """
    # Only allow authentication via token
    # Only using session authentication by default everywhere else
    # locks out anyone with a token from using any of the other endpoints
    authentication_classes = (TokenAuthentication,)
    serializer_class = SurveyCompanyNameSerializer
    queryset = Survey.objects.all()
    lookup_field = 'sid'
    lookup_url_kwarg = 'sid'

    def retrieve(self, request, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        instance = get_object_or_404(self.queryset, **{self.lookup_field: request.GET.get(self.lookup_url_kwarg)})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SurveyResultsDetail(ListAPIView):
    """
    Retrieve `SurveyResults` instance.
    By spec we assume we should have a single SurveyResult per Survey and in case we have
    more than one we just take the latest. That's why we are using survey_id as lookup field
    instead of the pk.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SurveyResultSerializer
    filter_backends = (OrderingFilter,)
    lookup_field = 'survey_id'
    lookup_url_kwarg = 'sid'
    ordering = ('-loaded_at')

    def get_queryset(self):
        lookup_url_kwarg = self.kwargs.get(self.lookup_url_kwarg)
        return SurveyResult.objects.filter(**{self.lookup_field: lookup_url_kwarg})

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset:
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        raise Http404


class SurveyResultsIndustryDetail(APIView):
    """
    Returns the bechmark data given an industry.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, industry_name, *args, **kwargs):
        dmb = None
        dmb_d = None
        dmb_bp = None
        dmb_d_bp = None

        surveys = Survey.objects.filter(industry=industry_name).exclude(last_survey_result__isnull=True)
        if not surveys:
            raise Http404
        dmb_d_list = [survey.last_survey_result.dmb_d for survey in surveys]
        if dmb_d_list and len(dmb_d_list) > settings.MIN_ITEMS_INDUSTRY_THRESHOLD:
            dmb, dmb_d = benchmark.calculate_group_benchmark(dmb_d_list)
            dmb_bp, dmb_d_bp = benchmark.calculate_best_practice(dmb_d_list)

        data = {
            'industry_name': industry_name,
            'dmb': dmb,
            'dmb_d': dmb_d,
            'dmb_bp': dmb_bp,
            'dmb_d_bp': dmb_d_bp,
        }

        return Response(data)
