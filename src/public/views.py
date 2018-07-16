from django.shortcuts import render
from django.http import Http404
from core.models import SurveyResult
from core.qualtrics import calculate_benchmark


def ReportsView(request, sid):
    try:
        sResult = SurveyResult.objects.get(survey__sid=sid)
    except SurveyResult.DoesNotExist:
        raise Http404("Report has not been generated yet")

    DMB, DMBd = calculate_benchmark(sResult.questions)

    return render(request, 'public/report.html', {
        DMB,
        DMBd
    })
