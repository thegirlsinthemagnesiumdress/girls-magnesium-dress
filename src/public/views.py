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


def _dump_tenant_content_data(tenant):
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']

    data = {
        'levels': content_data['levels'],
        'level_descriptions': content_data['level_descriptions'],
        'dimensions': content_data['dimensions'],
        'dimension_labels': content_data['dimension_labels'],
        'dimension_headers_descriptions': content_data['dimension_headers_descriptions'],
        'dimension_level_description': content_data['dimension_level_description'],
        'dimension_level_recommendations': content_data['dimension_level_recommendations'],
    }

    return json.dumps(data)


def registration(request, tenant):
    return render(request, 'public/{}/registration.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'recommendations': _dump_tenant_content_data(tenant),
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
    })


def report_static(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'recommendations': _dump_tenant_content_data(tenant),
    })


# @TODO remove this and use report_static. This is a temporary view to develop new report styles
def report_static_news(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    return render(request, 'public/{}/report-static-news.html'.format(tenant), {
        'tenant': tenant,
        'recommendations': _dump_tenant_content_data(tenant),
    })


def report_result_static(request, tenant, response_id):
    get_object_or_404(SurveyResult, response_id=response_id)
    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'recommendations': _dump_tenant_content_data(tenant),
    })


def index_static(request, tenant):
    slug = get_tenant_slug(tenant)
    return render(request, 'public/{}/index.html'.format(tenant), {
        'tenant': tenant,
        'recommendations': _dump_tenant_content_data(tenant),
        'slug': slug,
    })


def thank_you(request, tenant):
    slug = get_tenant_slug(tenant)
    return render(request, 'public/{}/thank-you.html'.format(tenant), {
        'tenant': tenant,
        'recommendations': _dump_tenant_content_data(tenant),
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
        'slug': get_tenant_slug(tenant),
        'recommendations': _dump_tenant_content_data(tenant),
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
        settings.TENANTS[tenant]['recommendations'],
        settings.TENANTS[tenant]['DIMENSION_TITLES']
    )
    return render(request, 'public/{}/result-detail.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'recommendations': _dump_tenant_content_data(tenant),
        'result_detail': result_detail,
        'survey_result': survey_result,
        'survey': survey_result.survey,
    })


def handler404(request, *args, **kwargs):
    return render(request, 'public/error.html', {
        'title': '404',
        'subtitle': "Woops.. that page doesn't seem to exist, or the link is broken.",
        'text': 'Try returning to the homepage.',
        'cta': 'Return to homepage',
        'tenant': '',
        'slug': '',
        'recommendations': '',
    }, status=404)


def handler500(request, *args, **kwargs):
    return render(request, 'public/error.html', {
        'title': '500',
        'subtitle': 'Woops.. there was an internal server error.',
        'text': 'Try returning to the homepage.',
        'cta': 'Return to homepage',
        'tenant': '',
        'slug': '',
        'recommendations': '',
    }, status=500)
