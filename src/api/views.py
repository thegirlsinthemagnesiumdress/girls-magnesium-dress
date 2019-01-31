from collections import OrderedDict
from api.serializers import (
    SurveyCompanyNameSerializer,
    SurveySerializer,
    SurveyWithResultSerializer,
)
from core.models import Survey, SurveyResult
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
from core.aggregate import get_surveys_by_industry
from core.conf.utils import flatten


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

    def retrieve(self, request, sid, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        survey_instance = get_object_or_404(self.queryset, **{self.lookup_field: sid})
        survey_instance.survey_result = survey_instance.last_survey_result
        serializer = self.get_serializer(survey_instance)
        return Response(serializer.data)


class SurveyResultDetailView(RetrieveAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SurveyWithResultSerializer
    queryset = SurveyResult.objects.all()
    lookup_field = 'response_id'
    lookup_url_kwarg = 'response_id'

    def retrieve(self, request, response_id, *args, **kwargs):
        """
        Overridden RetrieveAPIView retrieve() to get instance via GET param instead of URL keyword arg.
        """
        survey_result_instance = get_object_or_404(self.queryset, **{self.lookup_field: response_id})
        survey_instance = survey_result_instance.survey
        survey_instance.survey_result = survey_result_instance
        serializer = self.get_serializer(survey_instance)
        return Response(serializer.data)


class SurveyResultsIndustryDetail(APIView):
    """
    Returns the bechmark data given an industry.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, industry, *args, **kwargs):
        industry_map = OrderedDict(flatten(settings.HIERARCHICAL_INDUSTRIES, leaf_only=False))

        if industry not in settings.INDUSTRIES.keys():
            raise Http404

        global_id, _ = settings.ALL_INDUSTRIES

        surveys, current_industry = get_surveys_by_industry(industry, settings.MIN_ITEMS_INDUSTRY_THRESHOLD)
        dmb_d_list = [survey.last_survey_result.dmb_d for survey in surveys]
        dmb, dmb_d, dmb_industry = None, None, None
        if len(dmb_d_list) >= settings.MIN_ITEMS_INDUSTRY_THRESHOLD:
            print dmb_d_list
            dmb, dmb_d = benchmark.calculate_group_benchmark(dmb_d_list)
            dmb_industry = industry_map[current_industry] if current_industry else global_id

        surveys, current_industry = get_surveys_by_industry(industry, settings.MIN_ITEMS_BEST_PRACTICE_THRESHOLD)
        dmb_d_list = [survey.last_survey_result.dmb_d for survey in surveys]
        dmb_bp, dmb_d_bp, dmb_bp_industry = None, None, None
        if len(dmb_d_list) >= settings.MIN_ITEMS_BEST_PRACTICE_THRESHOLD:
            dmb_bp, dmb_d_bp = benchmark.calculate_best_practice(dmb_d_list)
            dmb_bp_industry = industry_map[current_industry] if current_industry else global_id

        data = {
            'industry': industry_map[industry],
            'dmb_industry': dmb_industry,
            'dmb_bp_industry': dmb_bp_industry,
            'dmb': dmb,
            'dmb_d': dmb_d,
            'dmb_bp': dmb_bp,
            'dmb_d_bp': dmb_d_bp,
        }
        return Response(data)
