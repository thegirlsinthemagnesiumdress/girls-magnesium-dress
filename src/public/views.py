from django.conf import settings
from django.contrib.auth.decorators import login_required
from angular.shortcuts import render
from api.serializers import SurveyWithResultSerializer

from core.auth import survey_admin_required
from core.models import Survey
from rest_framework.renderers import JSONRenderer


INDUSTRIES_TUPLE = [(k, v)for k, v in settings.INDUSTRIES.items()]
COUNTRIES_TUPLE = [(k, v)for k, v in settings.COUNTRIES.items()]


def registration(request):
    return render(request, 'public/registration.html', {
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
    })


def report_static(request, sid):
    return render(request, 'public/report-static.html', {})


def index_static(request):
    return render(request, 'public/index.html', {})


@login_required
@survey_admin_required
def reports_admin(request):

    if request.user.is_whitelisted:
        surveys = Survey.objects.all()
    else:
        surveys = Survey.objects.filter(engagement_lead=request.user.engagement_lead)

    serialized_data = SurveyWithResultSerializer(surveys, many=True)

    return render(request, 'public/reports-list.html', {
        'surveys': surveys,
        'engagement_lead': request.user.engagement_lead,
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
        'host': request.get_host(),
        'bootstrap_data': JSONRenderer().render({
            'surveys': serialized_data.data
        })
    })
