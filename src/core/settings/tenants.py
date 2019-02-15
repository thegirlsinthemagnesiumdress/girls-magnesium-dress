ADS = 'advertisers'
NEWS = 'news'


TENANTS = {
    ADS: {
        'label': 'Advertise',
        'QUALTRICS_SURVEY_ID': 'SV_beH0HTFtnk4A5rD',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
    },
    NEWS: {
        'label': 'News',
        'QUALTRICS_SURVEY_ID': 'SV_4JxgntrYg5uiMyp',
        'EMAIL_TO': 'Q1_4_TEXT',
        'EMAIL_BCC': 'Q1_5_TEXT',
    },
}

ALLOWED_TENANTS = '|'.join(TENANTS.keys())
TENANTS_CHOICES = [(k, v['label']) for k, v in TENANTS.items()]
