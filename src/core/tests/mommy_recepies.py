"""Recipies for the Survey models."""
from core.models import Survey, Benchmark
from model_mommy.recipe import Recipe


SurveyRecipe = Recipe(
    Survey,
    company_name='Test Survey',
)

BenchmarkRecipe = Recipe(
    Benchmark,
    sid='AAA'
)
