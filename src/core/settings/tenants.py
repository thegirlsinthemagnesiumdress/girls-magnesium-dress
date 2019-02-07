ADS = 'ads'
PUBLISHERS = 'publishers'


TENANTS = {
    ADS: {
        'label': 'Advertise',
        'QUALTRICS_SURVEY_ID': 'SV_beH0HTFtnk4A5rD',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
    },
    PUBLISHERS: {
        'label': 'Publishers',
        'QUALTRICS_SURVEY_ID': None,
        'EMAIL_TO': None,
        'EMAIL_BCC': None,
    },
}

ALLOWED_TENANTS = '|'.join(TENANTS.keys())
TENANTS_CHOICES = [(k, v['label']) for k, v in TENANTS.items()]
