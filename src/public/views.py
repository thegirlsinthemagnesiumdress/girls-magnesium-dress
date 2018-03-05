from core.models import Company
from django.http import JsonResponse
SURVEY_URL = 'https://google.qualtrics.com/jfe/form/SV_beH0HTFtnk4A5rD'

# POST only endopoint to create a new survey.
# The endpoint should return a unique link for the survey.
#
# TODO: This endpoint should live in the API app but not sure right now
# how to handle the different authotization.
def create_survey(request):
    if request.method == "POST":
        company_name = request.POST.get('name')
        # TODO I should probably should use the model validation here instead of
        # directly checking requests.
        if not company_name:
            return JsonResponse(status=422, data={'error': 'Company name is required'})
        c = Company(company_name=company_name)
        c.save()
        link = '{}?sid={}'.format(SURVEY_URL, c.uid)
        link_sponsor = '{}&sponsor=true'.format(link)

        return JsonResponse ({
            'link': link,
            'link_sponsor': link_sponsor
        })
    else:
        return JsonResponse ({
            'error': '{} method is not supported'.format(request.method)
        })

