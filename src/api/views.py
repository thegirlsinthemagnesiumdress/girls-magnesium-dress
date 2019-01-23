from api.serializers import (
    SurveyCompanyNameSerializer,
    SurveySerializer,
    SurveyWithResultSerializer,
)
from core.models import Survey
from core.qualtrics import benchmark
from django.conf import settings
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from core.benchmark import get_surveys_by_industry
from django.core.cache import cache


class CreateSurveyView(CreateAPIView):
    """
    Internal API endpoint to create a survey and return the created survey data including both link and link_sponsor.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
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
    _bypass_domain_restriction = True

    def retrieve(self, request, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        instance = get_object_or_404(self.queryset, **{self.lookup_field: request.GET.get(self.lookup_url_kwarg)})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SurveyDetailView(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SurveyWithResultSerializer
    queryset = Survey.objects.all()
    lookup_field = 'sid'
    lookup_url_kwarg = 'sid'


class SurveyResultsIndustryDetail(APIView):
    """
    Returns the bechmark data given an industry.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request, industry_name, *args, **kwargs):
        dmb = None
        dmb_d = None
        dmb_bp = None
        dmb_d_bp = None

        try:
            surveys, industry = get_surveys_by_industry(industry_name)
        except ValueError:
            raise Http404

        cached = cache.get(industry)
        if cached:
            return Response(cached)

        dmb_d_list = [survey.last_survey_result.dmb_d for survey in surveys]
        if dmb_d_list and len(dmb_d_list) > settings.MIN_ITEMS_INDUSTRY_THRESHOLD:
            dmb, dmb_d = benchmark.calculate_group_benchmark(dmb_d_list)
            dmb_bp, dmb_d_bp = benchmark.calculate_best_practice(dmb_d_list)

        data = {
            'industry_name': industry,
            'dmb': dmb,
            'dmb_d': dmb_d,
            'dmb_bp': dmb_bp,
            'dmb_d_bp': dmb_d_bp,
        }
        cache.set(industry, data)
        return Response(data)
