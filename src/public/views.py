from core.models import Survey, SurveyResult
from django.contrib.auth.decorators import login_required
from django.conf import settings
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


def registration(request):
    return render(request, 'public/registration.html', {
        'industries': settings.INDUSTRIES,
        'countries': settings.COUNTRIES,
    })


@login_required
def reports_admin(request):

    if request.user.is_whitelisted:
        surveys = Survey.objects.all()
    else:
        surveys = Survey.objects.filter(engagement_lead=request.user.engagement_lead)

    return render(request, 'public/reports-list.html', {
        'surveys': surveys,
        'engagement_lead': request.user.engagement_lead,
    })
