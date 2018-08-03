from core.models import Survey, SurveyResult
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render


def report_view(request, sid):
    try:
        s_result = SurveyResult.objects.filter(survey_id=sid).latest('loaded_at')
    except SurveyResult.DoesNotExist:
        raise Http404("Report does not exist.")

    return render(request, 'public/report.html', {
        'company_name': s_result.survey.company_name,
        'DMB': s_result.dmb,
        'DMBd': s_result.dmb_d,
    })


@login_required
def reports_admin(request):

    if request.user.is_whitelisted:
        s_results = SurveyResult.objects.all()
    else:
        engagement_lead_surveys = Survey.objects.filter(engagement_lead=request.user.engagement_lead)
        s_results = SurveyResult.objects.filter(survey__in=engagement_lead_surveys)

    surveys_with_results = []
    surveys_without_results = []

    for result in s_results:
        if result.survey:
            surveys_with_results.append(result.survey)
        else:
            surveys_without_results.append(result)

    return render(request, 'public/reports-list.html', {
        'surveys': surveys_with_results,
    })
