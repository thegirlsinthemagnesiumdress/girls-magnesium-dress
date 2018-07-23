from django.shortcuts import render
from django.http import Http404
from core.models import SurveyResult, Survey
from core.qualtrics.benchmark import calculate_response_benchmark


def reports_list(request):
    s_results = SurveyResult.objects.all()
    surveys = []

    for result in s_results:
        if result.survey:
            surveys.append(result.survey)

    return render(request, 'public/reports-list.html', {
        'surveys': set(surveys),
    })


def report_view(request, sid):
    try:
        s = Survey.objects.get(sid=sid)
        s_result = SurveyResult.objects.filter(survey=s).latest('loaded_at')
    except Survey.DoesNotExist:
        raise Http404("Survey does not exist.")
    except SurveyResult.DoesNotExist:
        raise Http404("Report has not been generated yet.")

    DMB, DMBd = calculate_response_benchmark(s_result.questions)
    return render(request, 'public/report.html', {
        'company_name': s.company_name,
        'DMB': DMB,
        'DMBd': DMBd,
    })
