from core.models import Survey, IndustryBenchmark
from django.conf import settings
from collections import defaultdict


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


def get_path(element, elements, root_element=None):
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
        path.append(root_element)
    return path


def updatable_industries(survey_results):
    """Return a dictionary of industries to be updated with related `core.models.SurveyResult`.

    :param survey_results: list of `core.models.SurveyResult` to be organized by industry.

    :return: a dictionary like object of industry to be updated.
    """
    results_by_industry = defaultdict(list)
    for s in survey_results:
        if s.survey:
            path = get_path(s.survey.industry, settings.INDUSTRIES, settings.ALL_INDUSTRIES[0])
            for industry in path:
                results_by_industry[industry].append(s)

    return results_by_industry


def industry_benchmark(tenant, industry, global_id=settings.ALL_INDUSTRIES[0]):
    """
    Return the digital maturity benchmark and the digital maturity benchmark by
    dimension stored in `core.models.IndustryBenchmark` element given `tenant`
    and `industry` paramenters

    :param tenant: tenant to retrieve the industry for
    :param industry: starting industry to retrieve for `tenant`
    :param global_id: name for the root industry to be returned

    :returns: tuple of three elements (dmb, dmb_d, dmb_industry) where:
        - dmb : represent the dmb stored in `core.models.IndustryBenchmark`
        - dmb_d : represent the dmb by dimension stored in `core.models.IndustryBenchmark`
        - dmb_industry : represent the root industry
    """

    dmb, dmb_d, dmb_industry = None, None, global_id
    for current_industry in get_path(industry, settings.INDUSTRIES, global_id):
        try:
            industry_benchmark = IndustryBenchmark.objects.get(tenant=tenant, industry=current_industry)
            dmb = industry_benchmark.dmb_value
            dmb_d = industry_benchmark.dmb_d_value
            dmb_industry = current_industry
        except IndustryBenchmark.DoesNotExist:
            pass
        if dmb:
            break

    return dmb, dmb_d, dmb_industry


def industry_best_practice(industry, global_id=settings.ALL_INDUSTRIES[0]):
    dmb_bp, dmb_d_bp, dmb_industry = None, None, global_id
    for current_industry in get_path(industry, settings.INDUSTRIES, global_id):
        try:
            industry_benchmark = IndustryBenchmark.objects.get(industry=current_industry)
            dmb_bp = industry_benchmark.dmb_bp_value
            dmb_d_bp = industry_benchmark.dmb_d_bp_value
            dmb_industry = current_industry
        except IndustryBenchmark.DoesNotExist:
            pass
        if dmb_bp:
            break

    return dmb_bp, dmb_d_bp, dmb_industry
