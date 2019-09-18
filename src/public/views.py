# coding=utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from angular.shortcuts import render

from core.auth import survey_admin_required
from core.models import Survey, SurveyResult
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from core.response_detail import get_response_detail
from core.conf import utils
import json
from django.utils.translation import ugettext as _
from core.encoders import LazyEncoder
from api.views import AdminSurveyListView
from core import tasks
from django.http import HttpResponse
import logging
from djangae import deferred
import datetime
import os


COUNTRIES_TUPLE = [(k, v)for k, v in settings.COUNTRIES.items()]

version, is_nightly, is_development, is_staging = utils.version_info(os.environ['HTTP_HOST'])
STAGING = is_staging


def _dump_tenant_content_data(tenant):
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']

    data = {
        'levels': content_data['levels'],
        'levels_max': content_data['levels_max'],
        'level_descriptions': content_data['level_descriptions'],
        'report_level_descriptions': content_data.get('report_level_descriptions'),
        'dimensions': content_data['dimensions'],
        'dimension_titles': content_data['dimension_titles'],
        'dimension_header_descriptions': content_data['dimension_header_descriptions'],
        'dimension_level_description': content_data['dimension_level_description'],
        'dimension_recommendations': content_data['dimension_recommendations'],
        'industry_avg_description': content_data.get('industry_avg_description'),
        'industry_best_description': content_data.get('industry_best_description'),
        'dimension_sidepanel_heading': content_data.get('dimension_sidepanel_heading'),
        'dimension_sidepanel_descriptions': content_data.get('dimension_sidepanel_descriptions'),
        'subdimension_lists': content_data.get('subdimension_lists'),
        'subdimensions_report_heading': content_data.get('subdimensions_report_heading'),
        'subdimensions_report_description': content_data.get('subdimensions_report_description'),
        'subdimensions_report_cta': content_data.get('subdimensions_report_cta'),
        'subdimensions_report_subheading': content_data.get('subdimensions_report_subheading'),
        'subdimensions_sidepanel_heading': content_data.get('subdimensions_sidepanel_heading'),
        'subdimension_names': content_data.get('subdimension_names'),
        'subdimension_descriptions': content_data.get('subdimension_descriptions'),
    }

    return json.dumps(data, cls=LazyEncoder)


def registration(request, tenant):

    tenant_conf = settings.TENANTS[tenant]
    industries = utils.flatten(tenant_conf['HIERARCHICAL_INDUSTRIES'])
    return render(request, 'public/registration.html', {
        'tenant': tenant,
        'slug': utils.get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'industries': industries,
        'countries': COUNTRIES_TUPLE,
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
    })


def report_static(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    all_dimensions = settings.TENANTS[tenant]['CONTENT_DATA']['dimensions']
    dimension_scores = survey.last_survey_result.dmb_d
    report_dimensions = []
    for dimension in all_dimensions:
        if dimension_scores[dimension] is not None:
            report_dimensions.append(dimension)

    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'staging': STAGING,
        'tenant': tenant,
        'slug': utils.get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'is_nightly': utils.version_info(request.get_host())[1],
        'started_at': survey.last_survey_result.started_at,
    })


def internal_report(request, tenant, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_internal_result:
        raise Http404

    return render(request, 'public/{}/report-internal.html'.format(tenant), {
        'tenant': tenant,
        'slug': utils.get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'is_nightly': utils.version_info(request.get_host())[1],
    })


def report_result_static(request, tenant, response_id):
    get_object_or_404(SurveyResult, response_id=response_id)
    return render(request, 'public/{}/report-static.html'.format(tenant), {
        'staging': STAGING,
        'tenant': tenant,
        'slug': utils.get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'is_nightly': utils.version_info(request.get_host())[1],
    })


def index_static(request, tenant):
    slug = utils.get_tenant_slug(tenant)
    levels_info = []
    for k, v in sorted(settings.TENANTS[tenant]['CONTENT_DATA']['levels'].items()):
        levels_info.append({
            'heading': v,
            'text': settings.TENANTS[tenant]['CONTENT_DATA']['level_descriptions'][k],
        })
    return render(request, 'public/{}/index.html'.format(tenant), {
        'tenant': tenant,
        'content_data': _dump_tenant_content_data(tenant),
        'slug': slug,
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'levels_info': levels_info,
    })


def thank_you(request, tenant):
    slug = utils.get_tenant_slug(tenant)
    return render(request, 'public/thank-you.html', {
        'tenant': tenant,
        'content_data': _dump_tenant_content_data(tenant),
        'slug': slug,
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
    })


@login_required
@survey_admin_required
def internal_survey_completion(request, tenant):
    slug = utils.get_tenant_slug(tenant)
    return render(request, 'public/admin/survey-completion.html', {
        'content_data': _dump_tenant_content_data(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'slug': slug,
        'tenant': tenant,
    })


@login_required
@survey_admin_required
def reports_admin(request, tenant):
    return redirect(reverse('accounts', kwargs={'tenant': utils.get_tenant_slug(tenant)}))


@login_required
@survey_admin_required
def accounts(request, tenant):
    tenant_conf = settings.TENANTS[tenant]
    industries = utils.flatten(tenant_conf['HIERARCHICAL_INDUSTRIES'])

    slug = utils.get_tenant_slug(tenant)

    api_data = AdminSurveyListView.as_view()(request, tenant=tenant).render().data

    return render(request, 'public/admin/accounts.html', {
        'accounts': request.user.accounts,
        'bootstrap_data': JSONRenderer().render(api_data),
        'content_data': _dump_tenant_content_data(tenant),
        'engagement_lead': request.user.engagement_lead,
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'slug': slug,
        'tenant': tenant,
        'industries': industries,
        'countries': COUNTRIES_TUPLE,
        'create_survey_url': request.build_absolute_uri(reverse('registration', kwargs={'tenant': slug})),
    })


@login_required
@survey_admin_required
def add_account(request, tenant):
    tenant_conf = settings.TENANTS[tenant]
    industries = utils.flatten(tenant_conf['HIERARCHICAL_INDUSTRIES'])

    slug = utils.get_tenant_slug(tenant)

    return render(request, 'public/admin/add-account.html', {
        'content_data': _dump_tenant_content_data(tenant),
        'engagement_lead': request.user.engagement_lead,
        'other_tenants': utils.get_other_tenant_footers(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'slug': slug,
        'tenant': tenant,
        'industries': industries,
        'countries': COUNTRIES_TUPLE,
    })


@login_required
@survey_admin_required
def account_detail(request, tenant, sid):
    account = get_object_or_404(Survey, sid=sid)
    content_data = settings.TENANTS[tenant]['CONTENT_DATA']

    account_info, external_surveys, internal_surveys = utils.get_account_detail_data(content_data, account)

    return render(request, 'public/admin/account-details.html', {
        'tenant': tenant,
        'slug': utils.get_tenant_slug(tenant),
        'account': account_info,
        'external_results': external_surveys,
        'internal_results': internal_surveys,
        'content_data': _dump_tenant_content_data(tenant),
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
    })


@login_required
@survey_admin_required
def result_detail(request, tenant, response_id):
    survey_result = get_object_or_404(SurveyResult, response_id=response_id)

    if survey_result.completed_by != request.user:
        raise PermissionDenied

    result_detail = get_response_detail(
        survey_result.survey_definition.content,
        survey_result.raw,
        settings.TENANTS[tenant]['DIMENSIONS'],
        settings.TENANTS[tenant]['CONTENT_DATA']['dimension_titles']
    )
    return render(request, 'public/{}/result-detail.html'.format(tenant), {
        'tenant': tenant,
        'slug': utils.get_tenant_slug(tenant),
        'content_data': _dump_tenant_content_data(tenant),
        'result_detail': result_detail,
        'survey_result': survey_result,
        'survey': survey_result.survey,
        'product_name': utils.get_tenant_product_name(tenant),
        'other_tenants': utils.get_other_tenant_footers(tenant),
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
        'product_name': '',
        'other_tenants': [],
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
        'product_name': '',
        'other_tenants': [],
    }, status=500)


@login_required
@survey_admin_required
def generate_spreadsheet_export(request, tenant):
    """Generate a spreadsheet export for tenant data."""
    _MISSING_INFO_MSG = ("Missing information for generating spreadsheet export for "
                         "Enagagement Lead: {engagement_lead}, Tenant: {tenant}")

    _GENERATED_INFO_MSG = ("Generate spreadsheet export for Enagagement Lead: "
                           "{engagement_lead}, Tenant: {tenant}")

    _USER_USING_DIFFERENT_EL = ("User {user} is trying to access to data that belongs to another "
                                "Enagagement Lead: {engagement_lead}")

    if request.method != "POST":
        return HttpResponse(status=405)

    try:
        json_body = json.loads(request.body)
        engagement_lead = json_body.get('engagement_lead')

        if not engagement_lead:
            msg = _MISSING_INFO_MSG.format(engagement_lead=engagement_lead, tenant=tenant)
            logging.warning(msg)
            return HttpResponse(msg, status=400)

        if engagement_lead != request.user.engagement_lead:
            msg = _USER_USING_DIFFERENT_EL.format(user=request.user.email, engagement_lead=engagement_lead)
            logging.error(msg)

        engagement_lead = request.user.engagement_lead

        tenant_conf = settings.TENANTS[tenant]
        survey_fields_mappings = tenant_conf['GOOGLE_SHEET_EXPORT_SURVEY_FIELDS']
        survey_result_fields_mapping = tenant_conf['GOOGLE_SHEET_EXPORT_RESULT_FIELDS']
        product_name = tenant_conf['PRODUCT_NAME']

        is_super_admin = request.user.is_super_admin

        now = datetime.datetime.now()

        msg = _GENERATED_INFO_MSG.format(engagement_lead=engagement_lead, tenant=tenant)
        logging.info(msg)
        deferred.defer(
            tasks.export_tenant_data,
            "{} | Data Export | {} ".format(product_name, now.strftime("%d-%m-%Y %H:%M")),
            tenant,
            is_super_admin,
            engagement_lead,
            survey_fields_mappings,
            survey_result_fields_mapping,
            request.user.email,
            _queue='default',
        )

    except ValueError:
        return HttpResponse(status=500)

    return HttpResponse(msg)
