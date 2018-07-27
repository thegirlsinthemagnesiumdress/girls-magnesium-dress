from api.serializers import (
    SurveyCompanyNameSerializer,
    SurveyResultSerializer,
    SurveySerializer,
)
from core.models import Survey, SurveyResult
from django.http import Http404
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
