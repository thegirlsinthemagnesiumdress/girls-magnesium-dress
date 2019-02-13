"""Recipies for the Survey models."""
from model_mommy import mommy
from django.conf import settings
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
import pytz
from django.utils.dateparse import parse_datetime
from uuid import uuid4


def make_survey(**kwargs):
    survey_kwargs = {
        "industry": settings.INDUSTRIES.keys()[0],
        "country": settings.COUNTRIES.keys()[0],
        "tenant": settings.TENANTS.keys()[0],
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