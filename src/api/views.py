from django.http import JsonResponse

def company(request, company_id):
    return JsonResponse({'name': 'Capybara'})