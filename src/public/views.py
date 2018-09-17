from core.models import Survey, SurveyResult
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


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
