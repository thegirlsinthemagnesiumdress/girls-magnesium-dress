from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.auth import survey_admin_required
from core.models import Survey


def registration(request):
    return render(request, 'public/registration.html', {
        'industries': settings.INDUSTRIES,
        'countries': settings.COUNTRIES,
    })


@login_required
@survey_admin_required
def reports_admin(request):

    if request.user.is_superuser:
        surveys = Survey.objects.all()
    else:
        surveys = Survey.objects.filter(engagement_lead=request.user.engagement_lead)

    return render(request, 'public/reports-list.html', {
        'surveys': surveys,
        'engagement_lead': request.user.engagement_lead,
        'industries': settings.INDUSTRIES,
        'countries': settings.COUNTRIES,
    })
