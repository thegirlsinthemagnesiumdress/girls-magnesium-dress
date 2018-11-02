"""Recipies for the Survey models."""
from model_mommy import mommy
from django.conf import settings
from datetime import datetime, timedelta
from django.utils.timezone import make_aware


def make_survey(**kwargs):
    survey_kwargs = {
        "industry": settings.INDUSTRIES.keys()[0],
        "country": settings.COUNTRIES.keys()[0],
    }

    survey_kwargs.update(kwargs)

    survey = mommy.make('core.Survey', **survey_kwargs)
    sid = kwargs.get('sid')
    if sid:
        survey.sid = sid
        survey.save()
    return survey


def make_survey_result(**kwargs):
    if not kwargs.get('started_at'):
        kwargs.update(started_at=make_aware(datetime.now() - timedelta(days=1)))
    return mommy.make('core.SurveyResult', **kwargs)
