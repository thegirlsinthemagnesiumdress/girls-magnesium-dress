# coding=utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from angular.shortcuts import render

from core.auth import survey_admin_required
from core.models import Survey, SurveyResult
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.http import Http404
from core.response_detail import get_response_detail
from core.conf.utils import flatten, get_tenant_slug
import json
from django.utils.translation import ugettext as _
from core.encoders import LazyEncoder
from api.views import AdminSurveyListView
from core import tasks
from django.http import HttpResponse
import logging
from djangae import deferred
import datetime


COUNTRIES_TUPLE = [(k, v)for k, v in settings.COUNTRIES.items()]


def _dump_tenant_content_data(tenant):
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']

    data = {
        'levels': content_data['levels'],
        'levels_max': content_data['levels_max'],
        'level_descriptions': content_data['level_descriptions'],
        'report_level_descriptions': content_data.get('report_level_descriptions'),
        'dimensions': content_data['dimensions'],
        'dimension_labels': content_data['dimension_labels'],
        'dimension_header_descriptions': content_data['dimension_header_descriptions'],
        'dimension_level_description': content_data['dimension_level_description'],
        'dimension_recommendations': content_data['dimension_recommendations'],
        'industry_avg_description': content_data.get('industry_avg_description'),
        'industry_best_description': content_data.get('industry_best_description'),
        'dimension_sidepanel_heading': content_data.get('dimension_sidepanel_heading'),
        'dimension_sidepanel_descriptions': content_data.get('dimension_sidepanel_descriptions'),
    }

    return json.dumps(data, cls=LazyEncoder)


def registration(request, tenant):
    industries = flatten(settings.HIERARCHICAL_INDUSTRIES)
    return render(request, 'public/{}/registration.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'industries': industries,
        'countries': COUNTRIES_TUPLE,
    })


def report_static(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
    })


def report_result_static(request, tenant, response_id):
    get_object_or_404(SurveyResult, response_id=response_id)
    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
    })


def index_static(request, tenant):
    slug = get_tenant_slug(tenant)
    return render(request, 'public/{}/index.html'.format(tenant), {
        'tenant': tenant,
        'content_data': _dump_tenant_content_data(tenant),
        'slug': slug,
    })


def thank_you(request, tenant):
    slug = get_tenant_slug(tenant)
    return render(request, 'public/{}/thank-you.html'.format(tenant), {
        'tenant': tenant,
        'content_data': _dump_tenant_content_data(tenant),
        'slug': slug,
    })


@login_required
@survey_admin_required
def reports_admin(request, tenant):
    industries = flatten(settings.HIERARCHICAL_INDUSTRIES)

    slug = get_tenant_slug(tenant)

    api_data = AdminSurveyListView.as_view()(request, tenant=tenant).render().data

    return render(request, 'public/{}/reports-list.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'engagement_lead': request.user.engagement_lead,
        'industries': industries,
        'countries': COUNTRIES_TUPLE,
        'create_survey_url': request.build_absolute_uri(reverse('registration', kwargs={'tenant': slug})),
        'bootstrap_data': JSONRenderer().render(api_data),
    })


@login_required
@survey_admin_required
def result_detail(request, tenant, response_id):
    survey_result = get_object_or_404(SurveyResult, response_id=response_id)

    result_detail = get_response_detail(
        survey_result.survey_definition.content,
        survey_result.raw,
        settings.TENANTS[tenant]['DIMENSIONS'],
        settings.TENANTS[tenant]['CONTENT_DATA']['dimension_labels']
    )
    return render(request, 'public/{}/result-detail.html'.format(tenant), {
        'tenant': tenant,
        'slug': get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'result_detail': result_detail,
        'survey_result': survey_result,
        'survey': survey_result.survey,
    })


def handler404(request, *args, **kwargs):
    return render(request, 'public/error.html', {
        'title': '404',
        'subtitle': _('Woops.. that page doesn\'t seem to exist, or the link is broken.'),
        'text': _('Try returning to the homepage.'),
        'cta': _('Return to homepage'),
        'tenant': '',
        'slug': '',
        'content_data': '',
    }, status=404)


def handler500(request, *args, **kwargs):
    return render(request, 'public/error.html', {
        'title': '500',
        'subtitle': _('Woops.. there was an internal server error.'),
        'text': _('Try returning to the homepage.'),
        'cta': _('Return to homepage'),
        'tenant': '',
        'slug': '',
        'content_data': '',
    }, status=500)


@login_required
@survey_admin_required
def generate_spreadsheet_export(request, tenant):
    """Generate a spreadsheet export for tenant data."""
    _MISSING_INFO_MSG = ("Missing information for generating spreadsheet export for "
                         "Enagagement Lead: {engagement_lead}, Tenant: {tenant}")

    _GENERATED_INFO_MSG = ("Generate spreadsheet export for Enagagement Lead: "
                           "{engagement_lead}, Tenant: {tenant}")

    if request.method != "POST":
        return HttpResponse(status=405)

    try:
        json_body = json.loads(request.body)
        engagement_lead = json_body.get('engagement_lead')

        if not engagement_lead:
            msg = _MISSING_INFO_MSG.format(engagement_lead=engagement_lead, tenant=tenant)
            logging.warning(msg)
            return HttpResponse(msg, status=400)

        tenant_conf = settings.TENANTS[tenant]
        survey_fields_mappings = tenant_conf['GOOGLE_SHEET_EXPORT_SURVEY_FIELDS']
        survey_result_fields_mapping = tenant_conf['GOOGLE_SHEET_EXPORT_RESULT_FIELDS']
        data = Survey.objects.filter(engagement_lead=engagement_lead, tenant=tenant)
        now = datetime.datetime.now()

        msg = _GENERATED_INFO_MSG.format(engagement_lead=engagement_lead, tenant=tenant)
        logging.info(msg)
        deferred.defer(
            tasks.export_tenant_data,
            "Digital Maturity Benchmark | Data Export | {} ".format(now.strftime("%d-%m-%Y %H:%M")),
            data,
            survey_fields_mappings,
            survey_result_fields_mapping,
            request.user.email,
            _queue='default',
        )

    except ValueError:
        return HttpResponse(status=500)

    return HttpResponse(msg)
