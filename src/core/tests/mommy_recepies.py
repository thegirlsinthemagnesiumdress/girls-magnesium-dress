"""Recipies for the Survey models."""
from model_mommy import mommy
from django.conf import settings
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
import pytz
from django.utils.dateparse import parse_datetime
from uuid import uuid4


def make_survey(**kwargs):
    tenant = kwargs.get('tenant', settings.TENANTS.keys()[0])
    industry = settings.TENANTS[tenant]['INDUSTRIES'].keys()[0]
    survey_kwargs = {
        "industry": industry,
        "country": settings.COUNTRIES.keys()[0],
        "tenant": tenant,
        "sid": kwargs.get('sid', uuid4().hex)
    }
    survey_kwargs.update(kwargs)
    survey = mommy.make('core.Survey', **survey_kwargs)
    return survey


def make_survey_result(**kwargs):
    if not kwargs.get('started_at'):
        started_at = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    else:
        started_at = kwargs.get('started_at')
    kwargs.update(
        started_at=make_aware(parse_datetime(started_at), pytz.timezone('US/Mountain'))
    )
    return mommy.make('core.SurveyResult', **kwargs)


def make_user(**kwargs):
    return mommy.make('core.User', **kwargs)


def make_survey_definition(**kwargs):
    return mommy.make('core.SurveyDefinition', **kwargs)


def make_survey_with_result(**kwargs):
    sr_kwargs = {}
    started_at = kwargs.pop('started_at', None)
    if started_at:
        sr_kwargs['started_at'] = started_at
    survey = make_survey(**kwargs)
    survey_res = make_survey_result(survey=survey, **sr_kwargs)
    survey.last_survey_result = survey_res
    survey.save()
    return survey


def make_industry_benchmark(**kwargs):
    return mommy.make('core.IndustryBenchmark', **kwargs)
