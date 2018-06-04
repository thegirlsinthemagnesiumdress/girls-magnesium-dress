from django.http import HttpResponse
from qualtrics import get_responses_by_field, get_results, calculate_benchmark, dimensions
from core.models import Survey

def update_survey_results(request):
    surveys = Survey.objects.all()
    data = get_results()
    responses_by_survey =  get_responses_by_field(data, 'survey_id')

    for survey in surveys:
        survey.DMB_overall_average = calculate_benchmark(responses_by_survey[survey.uid])
        survey.DMB_overall_average_by_dimension = calculate_benchmark(responses_by_survey[survey.uid], True)


    return HttpResponse(status=200)
