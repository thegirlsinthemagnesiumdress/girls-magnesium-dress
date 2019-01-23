from core.models import Survey
from django.conf import settings


def children(industry, elements):
    return [k for k, v in elements.items() if v[1] == industry]


def _is_leaf(industry, elements):
    return len(children(industry, elements)) == 0


def descendant(industry, elements, result):
    """Given an industry, it returns all the descendant from that industry.

    :param industry: the industry to get the descendant from.
    :returns: all the descendant from taht element
    """
    if _is_leaf(industry, elements):
        result.append(industry)
    for kid in children(industry, elements):
        descendant(kid, elements, result)
    return result


def _get_path(element, elements):
    """Given an element it returns the path from that element to the root element.

    `element` must be a part of `elements`.
    :param element: The element to get the path for
    :param elements: the graph of elements where to search for `element`
    :returns: Path from `element` to `root` element.`.
    """
    path = []
    current_element = element
    while current_element:
        path.append(current_element)
        label, parent = elements.get(current_element)
        current_element = parent
    else:
        path.append(current_element)
    return path


def get_surveys_by_industry(initial_industry):
    if initial_industry not in settings.INDUSTRIES:
        raise ValueError("`{}` is not in `settings.INDUSTRIES`".format(initial_industry))

    for industry in _get_path(initial_industry, settings.INDUSTRIES):
        current_industries = descendant(industry, settings.INDUSTRIES, [])
        surveys = Survey.objects.filter(industry__in=current_industries).exclude(last_survey_result__isnull=True)
        if len(surveys) > settings.MIN_ITEMS_INDUSTRY_THRESHOLD:
            break

    return surveys, industry
