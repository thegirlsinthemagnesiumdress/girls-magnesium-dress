from core.models import Survey, SurveyResult
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render


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

    return render(request, 'public/report.html', {
        'company_name': s.company_name,
        'DMB': s_result.dmb,
        'DMBd': s_result.dmb_d,
    })


@login_required
def reports_admin(request):

    if request.user.is_whitelisted:
        s_results = SurveyResult.objects.exclude(survey__isnull=True)
    else:
        engagement_lead_surveys = Survey.objects.filter(engagement_lead=request.user.engagement_lead)
        s_results = SurveyResult.objects.filter(survey__in=engagement_lead_surveys)

    surveys = [result.survey for result in s_results if result.survey]

    return render(request, 'public/reports-list.html', {
        'surveys': surveys,
    })
