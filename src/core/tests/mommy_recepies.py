"""Recipies for the Survey models."""
from core.models import Survey, SurveyResult
from model_mommy.recipe import Recipe


SurveyRecipe = Recipe(
    Survey,
    company_name='Test Survey',
)

SurveyResultRecipe = Recipe(
    SurveyResult,
)
