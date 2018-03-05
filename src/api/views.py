from django.http import JsonResponse
import logging
from core.models import Company


# This is a view used to investigate and prove we can use qualtrics
# web services to populate the company name
#
# Everything is hardcoded. This has to be taken as a quick prototype.
def company(request):
    # Prototypy token auth
    token = 'vG9r2NgG6Azr'
    request_token = request.META.get('HTTP_X_API_TOKEN')
    logging.info('Request toke %s', request_token)

    # Getting this from query string and not from url pattern
    # because I can't find a way to create the right url from Qualtrics.
    company_id = request.GET.get('id')

    if token != request_token:
        return JsonResponse(status=403, data={'error': 'Forbidden'})

    if not company_id:
        return JsonResponse(status=404, data={'error': 'You need to provide company id'})

    res = Company.objects.filter(uid=company_id)

    if len(res) > 0:
        return JsonResponse({ 'results': [{'name': res[0].company_name}]})
    else:
        return JsonResponse(data={'results': []})
