from core.models import Survey


def generate_surveys():
    companies_name = ['1', '2', '3']
    surveys = []

    for company_name in companies_name:
        s = Survey(company_name=company_name)
        s.save()
        surveys.append(s)

    return surveys
