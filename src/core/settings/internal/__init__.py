# flake8: noqa
import ads as ads_internal_conf

ADS_INTERNAL = 'ads'

# WIP Name
INTERNAL_TENANTS = {
    ADS_INTERNAL: {
        'key': ADS_INTERNAL,
        'DIMENSIONS': ads_internal_conf.DIMENSIONS,
        'QUALTRICS_SURVEY_ID': 'SV_6yhSDC5FbkxoHS5',
        'WEIGHTS': ads_internal_conf.WEIGHTS,
        'MULTI_ANSWER_QUESTIONS': ads_internal_conf.MULTI_ANSWER_QUESTIONS,
        'EXCLUDED_TIME_THRESHOLD': 5,
    }
}
