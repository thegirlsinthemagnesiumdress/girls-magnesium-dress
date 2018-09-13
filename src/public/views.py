from core.models import Survey, SurveyResult
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


def report_view(request, sid):
    try:
        s = Survey.objects.get(pk=sid)
        s_result = s.last_survey_result
    except SurveyResult.DoesNotExist:
        raise Http404("Report does not exist.")

    if s.industry:
        industry = settings.INDUSTRIES[s.industry]
    else:
        industry = None

    return render(request, 'public/report.html', {
        'company_name': s.company_name,
        'industry': industry,
        'country': s.country,
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
