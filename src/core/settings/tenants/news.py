WEIGHTS = {
    'Q4': 0.2,
    'Q5': 0.15,
    'Q7': 0.20,
    'Q9': 0.15,
    'Q6': 0.15,
    'Q8': 0.15,
    'Q10': 0,

    'Q11': 0.5,
    'Q12': 0.2,
    'Q13': 0.3,

    'Q14': 0.5,
    'Q15': 0.3,
    'Q16': 0.2,

    'Q17': 0.5,
    'Q18': 0.3,
    'Q19': 0.2,
}

DIMENSION_TITLES = {
    'strategic_direction': 'Strategic direction and data foundations',
    'reader_engagement': 'Reader Engagement',
    'reader_revenue': 'Reader Revenue',
    'advertising_revenue': 'Advertising Revenue',
}


# If a question ID is not added to this list the question won't be considered for the final score
DIMENSIONS = {
    'strategic_direction': [
        'Q4',
        'Q5',
        'Q6',
        'Q7',
        'Q8',
        'Q9',
        'Q10',
    ],
    'reader_engagement': [
        'Q11',
        'Q12',
        'Q13',
    ],
    'reader_revenue': [
        'Q14',
        'Q15',
        'Q16',
    ],
    'advertising_revenue': [
        'Q17',
        'Q18',
        'Q19',
    ]
}

MULTI_ANSWER_QUESTIONS = [
    'Q10',
]

DIMENSIONS_WEIGHTS_QUESTION_ID = 'Q2'

DIMENSIONS_WEIGHTS = {
    1: {
        'strategic_direction': 0.4,
        'reader_engagement': 0.3,
        'reader_revenue': 0.0,
        'advertising_revenue': 0.3,
    },
    2: {
        'strategic_direction': 0.4,
        'reader_engagement': 0.3,
        'reader_revenue': 0.3,
        'advertising_revenue': 0.0,
    },
    3: {
        'strategic_direction': 0.4,
        'reader_engagement': 0.2,
        'reader_revenue': 0.2,
        'advertising_revenue': 0.2,
    }
}
