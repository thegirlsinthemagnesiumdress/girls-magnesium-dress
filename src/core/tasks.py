import logging

import qualtrics
from core.models import Survey, SurveyResult


def get_results():
    try:
        survey_result = SurveyResult.objects.latest('loaded_at')
        response_id = survey_result.response_id
        logging.info('Some Survey results has already been downloaded, partially download new results.')
    except SurveyResult.DoesNotExist:
        response_id = None
        logging.info('No Survey results has already been downloaded so far, download all the results.')

    results = qualtrics.download_results(response_id=response_id)
    _create_survey_result(results.get('responses'))


def _create_survey_result(results_data):
    """Create `SurveyResult` given a list of `result_data`.

    :param survey: `core.SurveyResult` which `results_data` refers to
    :param results_data: dictionary containing the downloaded response
        from Qualtrics API.
    """
    for data in results_data:
        survey = Survey.objects.filter(sid=data.get('sid')).first()
        SurveyResult.objects.create(
            survey=survey,
            response_id=data.get('ResponseID'),
            data=data,
        )
