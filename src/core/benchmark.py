from core.models import Survey
from django.conf import settings


def children(industry):
    return [k for k, v in settings.INDUSTRIES.items() if v[1] == industry]


def _is_leaf(industry):
    return len(children(industry)) == 0


def descendant(industry, result):
    if _is_leaf(industry):
        result.append(industry)
    for kid in children(industry):
        descendant(kid, result)
    return result


def get_path(industry):
    path = []
    ind = industry
    while ind:
        path.append(ind)
        label, parent = settings.INDUSTRIES.get(ind)
        ind = parent
    else:
        path.append(ind)
    return path


def get_surveys_by_industry(initial_industry):
    if initial_industry not in settings.INDUSTRIES:
        raise ValueError("`{}` is not in `settings.INDUSTRIES`".format(initial_industry))

    for industry in get_path(initial_industry):
        current_industries = descendant(industry, [])
        surveys = Survey.objects.filter(industry__in=current_industries).exclude(last_survey_result__isnull=True)
        if len(surveys) > settings.MIN_ITEMS_INDUSTRY_THRESHOLD:
            break

    return surveys, industry
