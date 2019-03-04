# coding=utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from angular.shortcuts import render
from public.serializers import AdminSurveyResultsSerializer

from core.auth import survey_admin_required
from core.models import Survey, SurveyResult
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.http import Http404
from core.response_detail import get_response_detail
from core.conf.utils import flatten, get_tenant_slug
import json


INDUSTRIES_TUPLE = flatten(settings.HIERARCHICAL_INDUSTRIES)
COUNTRIES_TUPLE = [(k, v)for k, v in settings.COUNTRIES.items()]


def registration(request, tenant):
    return render(request, 'public/{}/registration.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
    })


def report_static(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
    })


# @TODO remove this and use report_static. This is a temporary view to develop new report styles
def report_static_news(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    return render(request, 'public/{}/report-static-news.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
    })


def report_result_static(request, tenant, response_id):
    get_object_or_404(SurveyResult, response_id=response_id)
    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
    })


def index_static(request, tenant):
    slug = get_tenant_slug(tenant)
    return render(request, 'public/{}/index.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
        'slug': slug,
    })


@login_required
@survey_admin_required
def reports_admin(request, tenant):

    surveys = Survey.objects.filter(tenant=tenant)
    if not request.user.is_super_admin:
        surveys = surveys.filter(engagement_lead=request.user.engagement_lead)

    slug = get_tenant_slug(tenant)

    serialized_data = AdminSurveyResultsSerializer(surveys, many=True)
    return render(request, 'public/{}/reports-list.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
        'engagement_lead': request.user.engagement_lead,
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
        'create_survey_url': request.build_absolute_uri(reverse('registration', kwargs={'tenant': slug})),
        'bootstrap_data': JSONRenderer().render({
            'surveys': serialized_data.data
        }),
    })


@login_required
@survey_admin_required
def result_detail(request, tenant, response_id):
    survey_result = get_object_or_404(SurveyResult, response_id=response_id)

    result_detail = get_response_detail(
        survey_result.survey_definition.content,
        survey_result.raw,
        settings.TENANTS[tenant]['DIMENSIONS'],
        settings.TENANTS[tenant]['DIMENSION_TITLES']
    )
    return render(request, 'public/{}/result-detail.html'.format(tenant), {
        'tenant': tenant,
        'dimensions': json.dumps(settings.TENANTS[tenant]['DIMENSION_TITLES']),
        'result_detail': result_detail,
        'survey_result': survey_result,
        'survey': survey_result.survey,
    })


def handler404(request):
    return render(request, 'public/error.html', {
        'title': '404',
        'subtitle': "Woops.. that page doesn't seem to exist, or the link is broken.",
        'text': 'Try returning to the homepage.',
        'cta': 'Return to homepage',
    }, status=404)


def handler500(request):
    return render(request, 'public/error.html', {
        'title': '500',
        'subtitle': 'Woops.. there was an internal server error.',
        'text': 'Try returning to the homepage.',
        'cta': 'Return to homepage',
    }, status=500)
