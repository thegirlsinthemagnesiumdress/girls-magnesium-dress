"""Recipies for the Survey models."""
from core.models import Survey, SurveyResult
from model_mommy.recipe import Recipe
from model_mommy import mommy

SurveyRecipe = Recipe(
    Survey,
    company_name='Test Survey',
)

SurveyResultRecipe = Recipe(
    SurveyResult,
)


def make_survey(**kwargs):
    survey = mommy.make('core.Survey', **kwargs)
    sid = kwargs.get('sid')
    if sid:
        survey.sid = sid
        survey.save()
    return survey


def make_survey_result(**kwargs):
    return mommy.make('core.SurveyResult', **kwargs)
