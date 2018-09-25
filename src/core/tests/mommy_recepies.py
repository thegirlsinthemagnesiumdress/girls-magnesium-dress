"""Recipies for the Survey models."""
from model_mommy import mommy
from django.conf import settings


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
    return mommy.make('core.SurveyResult', **kwargs)
