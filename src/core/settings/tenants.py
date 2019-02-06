TENANTS = {
    'ads': {
        'label': 'Advertise',
        'QUALTRICS_SURVEY_ID': 'SV_beH0HTFtnk4A5rD',
        'QUALTRICS_EMAIL_TO': 'Q97_4_TEXT',
        'QUALTRICS_EMAIL_BCC': 'Q97_5_TEXT',
    },
    'publishers': {
        'label': 'Publishers',
        'QUALTRICS_SURVEY_ID': None,
        'QUALTRICS_EMAIL_TO': None,
        'QUALTRICS_EMAIL_BCC': None,
    },
}

ALLOWED_TENANTS = '|'.join(TENANTS.keys())
TENANTS_CHOICES = [(k, v['label']) for k, v in TENANTS.items()]
