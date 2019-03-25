import ads as advertisers_conf
import news as news_conf
import retail as retail_conf

ADS = 'ads'
NEWS = 'news'
RETAIL = 'retail'


TENANTS = {
    ADS: {
        'key': ADS,
        'label': 'Advertise',
        'slug': 'advertisers',
        'QUALTRICS_SURVEY_ID': 'SV_beH0HTFtnk4A5rD',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
        'DIMENSIONS': advertisers_conf.DIMENSIONS,
        'DIMENSION_TITLES': advertisers_conf.DIMENSION_TITLES,
        'MULTI_ANSWER_QUESTIONS': advertisers_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': advertisers_conf.WEIGHTS,
        'EXCLUDED_TIME_THRESHOLD': 5,
    },
    NEWS: {
        'key': NEWS,
        'label': 'News',
        'slug': 'news',
        'QUALTRICS_SURVEY_ID': 'SV_4JxgntrYg5uiMyp',
        'EMAIL_TO': 'Q1_4_TEXT',
        'EMAIL_BCC': 'Q1_5_TEXT',
        'DIMENSIONS': news_conf.DIMENSIONS,
        'DIMENSION_TITLES': news_conf.DIMENSION_TITLES,
        'MULTI_ANSWER_QUESTIONS': news_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': news_conf.WEIGHTS,
        'DIMENSIONS_WEIGHTS_QUESTION_ID': news_conf.DIMENSIONS_WEIGHTS_QUESTION_ID,
        'DIMENSIONS_WEIGHTS': news_conf.DIMENSIONS_WEIGHTS,
        'FORCED_INDUSTRY': 'ic-bnpj',
        'EXCLUDED_TIME_THRESHOLD': 2,
    },
    RETAIL: {
        'key': RETAIL,
        'label': 'Retail',
        'slug': 'retail',
        'QUALTRICS_SURVEY_ID': 'SV_b1OV8m7xVD337rD',
        'EMAIL_TO': None,
        'EMAIL_BCC': None,
        'DIMENSIONS': retail_conf.DIMENSIONS,
        'DIMENSION_TITLES': retail_conf.DIMENSION_TITLES,
        'MULTI_ANSWER_QUESTIONS': retail_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': retail_conf.WEIGHTS,
        'FORCED_INDUSTRY': 'ic-bnpj',
    },
}


DEFAULT_TENANT = ADS

ALLOWED_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items()])
TENANTS_SLUG_TO_KEY = {v['slug']: k for k, v in TENANTS.items()}
TENANTS_CHOICES = [(k, v['label']) for k, v in TENANTS.items()]
