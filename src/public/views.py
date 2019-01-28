# coding=utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from angular.shortcuts import render
from api.serializers import SurveyWithResultSerializer

from core.auth import survey_admin_required
from core.models import Survey, SurveyResult
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.http import Http404
from core.response_detail import get_response_detail



INDUSTRIES_TUPLE = [(k, v)for k, v in settings.INDUSTRIES.items()]
COUNTRIES_TUPLE = [(k, v)for k, v in settings.COUNTRIES.items()]


def registration(request):
    return render(request, 'public/registration.html', {
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
    })


def report_static(request, sid):
    survey = get_object_or_404(Survey, sid=sid)
    if not survey.last_survey_result:
        raise Http404

    return render(request, 'public/report-static.html', {})


def index_static(request):
    return render(request, 'public/index.html', {})


@login_required
@survey_admin_required
def reports_admin(request):

    if request.user.is_super_admin:
        surveys = Survey.objects.all()
    else:
        surveys = Survey.objects.filter(engagement_lead=request.user.engagement_lead)

    serialized_data = SurveyWithResultSerializer(surveys, many=True)

    return render(request, 'public/reports-list.html', {
        'surveys': surveys,
        'engagement_lead': request.user.engagement_lead,
        'industries': INDUSTRIES_TUPLE,
        'countries': COUNTRIES_TUPLE,
        'create_survey_url': request.build_absolute_uri(reverse('registration')),
        'bootstrap_data': JSONRenderer().render({
            'surveys': serialized_data.data
        }),
    })


@login_required
@survey_admin_required
def result_detail(request, response_id):
    result_data = {
        "Q102": {
            "choices_text": [
            "Creatives are based mainly on insights from all relevant digital channels and advanced analytics."
            ],
            "value": [
            2.0
            ]
        },
        "Q103": {
            "choices_text": [
            "Coordinated across online channels without shared timeline."
            ],
            "value": [
            1.33
            ]
        },
        "Q104": {
            "choices_text": [
            "Some formalised media and creative collaboration, separate toolsets in place."
            ],
            "value": [
            1.33
            ]
        },
        "Q105": {
            "choices_text": [
            "Regular A/B testing. Results are often fed back into next campaign. No or limited sharing across teams."
            ],
            "value": [
            2.0
            ]
        },
        "Q106": {
            "choices_text": [
            "3 seconds or faster."
            ],
            "value": [
            4.0
            ]
        },
        "Q107": {
            "choices_text": [
            "Our experience leverages latest mobile capabilities (e.g. single sign-on, Accelerated Mobile Pages, Progressive Web Apps, Instant apps) and is considered best-in-class."
            ],
            "value": [
            4.0
            ]
        },
        "Q108": {
            "choices_text": [
            "Basic site personalisation based on a few customer segments (e.g. new and signed-in users)."
            ],
            "value": [
            1.33
            ]
        },
        "Q109": {
            "choices_text": [
            "Messages tailored by all available segments."
            ],
            "value": [
            2.67
            ]
        },
        "Q110": {
            "choices_text": [
            "Messages tailored by broad types of segments (e.g. existing customers and potential customers)."
            ],
            "value": [
            1.33
            ]
        },
        "Q112": {
            "choices_text": [
            "Messages tailored by all available segments."
            ],
            "value": [
            2.67
            ]
        },
        "Q113": {
            "choices_text": [
            "Same message served to all users."
            ],
            "value": [
            0.0
            ]
        },
        "Q114": {
            "choices_text": [
            "Messages tailored by broad types of segments (e.g. existing customers and potential customers)."
            ],
            "value": [
            1.33
            ]
        },
        "Q115": {
            "choices_text": [
            "We have a robust process in place and have connected online and offline systems, (e.g. using web analytics data to provide tailored in-store experiences)."
            ],
            "value": [
            4.0
            ]
        },
        "Q116": {
            "choices_text": [
            "We set frequency caps based on our own path-to-conversion reports."
            ],
            "value": [
            1.33
            ]
        },
        "Q117": {
            "choices_text": [
            "We mainly buy programmatically, using a variety of deal types (e.g. open and private auction, preferred and guaranteed deals). Our media buys are optimised across digital channels. Some non-digital media is bought programmatically."
            ],
            "value": [
            4.0
            ]
        },
        "Q118": {
            "choices_text": [
            "We buy display and video across desktop, mobile websites, mobile apps, as native and non-native media. We apply audience and targeting strategies across some of our our channels or formats."
            ],
            "value": [
            2.67
            ]
        },
        "Q119": {
            "choices_text": [
            "We advertise on keywords that are related to our brand, all of our products and product categories as well as other relevant terms. We use a mix of standard search ads and specialised formats (e.g. shopping ads or local ads)."
            ],
            "value": [
            2.67
            ]
        },
        "Q120": {
            "choices_text": [
            "Viewability metrics inform future media buys (e.g. by shifting budget)."
            ],
            "value": [
            2.67
            ]
        },
        "Q121": {
            "choices_text": [
            "We build negative keyword lists based on industry best practices and anecdotal evidence."
            ],
            "value": [
            1.33
            ]
        },
        "Q122": {
            "choices_text": [
            "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour."
            ],
            "value": [
            4.0
            ]
        },
        "Q123": {
            "choices_text": [
            "We use 3rd party data and 1st party data we capture within this channel and in other channels."
            ],
            "value": [
            2.67
            ]
        },
        "Q124": {
            "choices_text": [
            "We use 3rd party data and 1st party data (our own data) we capture within this channel."
            ],
            "value": [
            1.33
            ]
        },
        "Q125": {
            "choices_text": [
            "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour."
            ],
            "value": [
            4.0
            ]
        },
        "Q126": {
            "choices_text": [
            "A number of segments, based on socio-demographic data or spend data."
            ],
            "value": [
            1.33
            ]
        },
        "Q127": {
            "choices_text": [
            "4 or 5 segments."
            ],
            "value": [
            2.67
            ]
        },
        "Q128": {
            "choices_text": [
            "",
            "",
            ""
            ],
            "value": [
            1.33,
            1.33,
            1.33
            ]
        },
        "Q129": {
            "choices_text": [
            "No."
            ],
            "value": [
            0.0
            ]
        },
        "Q130": {
            "choices_text": [
            "Retrospective audience maintenance (e.g. target list updated after the campaign has ended)."
            ],
            "value": [
            1.33
            ]
        },
        "Q131": {
            "choices_text": [
            "Online and offline systems connected (e.g. direct mail systems linked to systems that manage 1st party digital data)."
            ],
            "value": [
            2.67
            ]
        },
        "Q132": {
            "choices_text": [
            "Yes, operated by us."
            ],
            "value": [
            2.0
            ]
        },
        "Q133": {
            "choices_text": [
            "All static creatives in an ad-sever."
            ],
            "value": [
            2.67
            ]
        },
        "Q134": {
            "choices_text": [
            "Don't know."
            ],
            "value": [
            0.0
            ]
        },
        "Q135": {
            "choices_text": [
            "We use the platform user interface but also leverage platform APIs for campaign setup and reporting."
            ],
            "value": [
            2.0
            ]
        },
        "Q136": {
            "choices_text": [
            "Bid adjustments (bid multipliers) based on signals such as usage of mobile devices or user location. Adjustments are updated frequently."
            ],
            "value": [
            1.33
            ]
        },
        "Q137": {
            "choices_text": [
            "Bid adjustments (bid multipliers) based on signals such as usage of mobile devices or user location. Adjustments are updated frequently."
            ],
            "value": [
            1.33
            ]
        },
        "Q138": {
            "choices_text": [
            "We make full use of automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search or display."
            ],
            "value": [
            2.67
            ]
        },
        "Q139": {
            "choices_text": [
            "Unified naming conventions for digital tracking and tagging across all channels and for major events on our websites."
            ],
            "value": [
            2.67
            ]
        },
        "Q140": {
            "choices_text": [
            "",
            "",
            "",
            "",
            ""
            ],
            "value": [
            0.25,
            1.25,
            0.0,
            1.0,
            0.0
            ]
        },
        "Q141": {
            "choices_text": [
            "No, or don't know."
            ],
            "value": [
            0.0
            ]
        },
        "Q142": {
            "choices_text": [
            "We have a comprehensive single-source of truth for digital. All digital media touchpoints and website behaviour are considered. Some non-digital data such as CRM or store visits are considered."
            ],
            "value": [
            2.67
            ]
        },
        "Q143": {
            "choices_text": [
            "",
            "",
            "",
            "",
            ""
            ],
            "value": [
            1.0,
            0.0,
            0.0,
            0.5,
            0.5
            ]
        },
        "Q144": {
            "choices_text": [
            "We don't have an attribution model."
            ],
            "value": [
            0.0
            ]
        },
        "Q145": {
            "choices_text": [
            "",
            "",
            "",
            "",
            ""
            ],
            "value": [
            0.0,
            1.0,
            0.0,
            0.0,
            0.5
            ]
        },
        "Q146": {
            "choices_text": [
            "Once a month."
            ],
            "value": [
            1.33
            ]
        },
        "Q147": {
            "choices_text": [
            "Regular use of testing. Results influence next campaign."
            ],
            "value": [
            1.33
            ]
        },
        "Q148": {
            "choices_text": [
            "Sponsored by senior leadership (e.g. CMO, CTO, COO)."
            ],
            "value": [
            3.0
            ]
        },
        "Q149": {
            "choices_text": [
            "Yes, but not fully dedicated."
            ],
            "value": [
            2.0
            ]
        },
        "Q150": {
            "choices_text": [
            "Yes, but not fully dedicated."
            ],
            "value": [
            2.0
            ]
        },
        "Q151": {
            "choices_text": [
            "No."
            ],
            "value": [
            0.0
            ]
        },
        "Q152": {
            "choices_text": [
            "Common objectives across multiple channels (e.g. across all digital channels)."
            ],
            "value": [
            2.67
            ]
        },
        "Q153": {
            "choices_text": [
            "Relevant cross-channel roles and partners collaborate for large campaign launches. Day-to-day interaction is limited."
            ],
            "value": [
            1.33
            ]
        },
        "Q154": {
            "choices_text": [
            "Some cross-agency collaboration (e.g. creatives work with display but not with search)"
            ],
            "value": [
            1.33
            ]
        },
        "Q155": {
            "choices_text": [
            "",
            "",
            "",
            ""
            ],
            "value": [
            0.0,
            0.0,
            0.5,
            0.5
            ]
        },
        "Q161": {
            "choices_text": [
            "We use a dedicated brand safety solution across all channels, monitor reports, update category filters and generate insights to improve our brand safety solution."
            ],
            "value": [
            4.0
            ]
        },
        "Q162": {
            "choices_text": [
            "Active monitoring and optimising of media buys. Actively engaged with publishers on fraud prevention."
            ],
            "value": [
            4.0
            ]
        },
        "Q163": {
            "choices_text": [
            "Dynamic creatives using mostly data feeds (e.g ad copy tailored based on user location or users keyword). We use automated and manual optimisation equally. Automation mostly focused on one channel."
            ],
            "value": [
            2.0
            ]
        }
    }

    definition = {
        "id": "SV_beH0HTFtnk4A5rD",
        "name": "DMB Survey - Staging",
        "ownerId": "UR_eQjASeYvNZoXnPD",
        "organizationId": "google",
        "isActive": True,
        "creationDate": "2018-11-29T13:27:15Z",
        "lastModifiedDate": "2018-12-11T17:22:31Z",
        "expiration": {
            "startDate": None,
            "endDate": None
        },
        "questions": {
            "QID97": {
                "questionType": {
                    "type": "TE",
                    "selector": "FORM",
                    "subSelector": None
                },
                "questionText": "Where should we send your results once you've finished?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": False,
                    "type": "CustomValidation"
                },
                "questionName": "Q97",
                "choices": {
                    "4": {
                        "description": "Enter your email address (required)",
                        "choiceText": "Enter your email address (required)",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True
                    },
                    "5": {
                        "description": "Who else should be emailed the report? (optional)",
                        "choiceText": "Who else should be emailed the report? (optional)",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True
                    }
                }
            },
            "QID173": {
                "questionType": {
                    "type": "MC",
                    "selector": "MAVR",
                    "subSelector": "TX"
                },
                "questionText": "Privacy policy\n<p class=\"dmb-privacy__description h-c-copy\">\nYou’ll need to agree to the use of your responses so we can create the report for you.\n</p>\n\n            <a class=\"dmb-button dmb-button--secondary dmb-button--external\"           href=\"https://policies.google.com/privacy\"\n            target=\"_blank\"> <svg class=\"dmb-button__icon h-c-icon h-c-icon--18px\" role=\"img\" viewbox=\"0 0 24 24\"><path d=\"M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z\"></path></svg> <span class=\"dmb-button__text\">View statement</span> </a> \n            </button>",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": False,
                    "type": "CustomValidation"
                },
                "questionName": "Q173",
                "choices": {
                    "1": {
                        "recode": "1",
                        "description": "Agree to our privacy statement",
                        "choiceText": "Agree to our privacy statement",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True
                    }
                }
            },
            "QID102": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "<h2 class=\"dmb-dimension-header\">Assets &amp; Ads</h2>\nWhich of the following best describes the extent to which your organisation uses data to inform creative development?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q102",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Creatives are based mainly on brand and product principles.",
                        "choiceText": "Creatives are based mainly on brand and product principles.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1",
                        "description": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                        "choiceText": "Creatives are based mainly on insights from a specific digital channel and advanced analytics.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Creatives are based mainly on insights from all relevant digital channels and advanced analytics.",
                        "choiceText": "Creatives are based mainly on insights from all relevant digital channels and advanced analytics.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Creatives are based on insights from digital and non-digital channels, balanced with brand and product principles.",
                        "choiceText": "Creatives are based on insights from digital and non-digital channels, balanced with brand and product principles.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID103": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How would you describe the connection between your communication channels?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q103",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Run largely independently by channel (e.g. display, search, social, email etc.)",
                        "choiceText": "Run largely independently by channel (e.g. display, search, social, email etc.)",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Coordinated across online channels without shared timeline.",
                        "choiceText": "Coordinated across online channels without shared timeline.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Coordinated and across online channels with shared timeline.",
                        "choiceText": "Coordinated and across online channels with shared timeline.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Coordinated across online and offline channels with shared timeline.",
                        "choiceText": "Coordinated across online and offline channels with shared timeline.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID104": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do your media buying and creative origination teams collaborate?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q104",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Little or no collaboration, separate or siloed creative processes with separate toolsets in place.",
                        "choiceText": "Little or no collaboration, separate or siloed creative processes with separate toolsets in place.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Some formalised media and creative collaboration, separate toolsets in place.",
                        "choiceText": "Some formalised media and creative collaboration, separate toolsets in place.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Media and creative teams working in conjunction using shared project management tools.",
                        "choiceText": "Media and creative teams working in conjunction using shared project management tools.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Media and creative teams working hand in hand from planning to execution using collaborative tools such as a Creative Management Platform (CMP).",
                        "choiceText": "Media and creative teams working hand in hand from planning to execution using collaborative tools such as a Creative Management Platform (CMP).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID105": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How would you decribe your methods to test and improve creative effectiveness?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": False
                },
                "questionName": "Q105",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Limited or no testing done.",
                        "choiceText": "Limited or no testing done.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1",
                        "description": "Individual efforts that are not part of a larger test plan.",
                        "choiceText": "Individual efforts that are not part of a larger test plan.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Regular A/B testing. Results are often fed back into next campaign. No or limited sharing across teams.",
                        "choiceText": "Regular A/B testing. Results are often fed back into next campaign. No or limited sharing across teams.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "3",
                        "description": "Mix of robust A/B tests, consumer surveys and real-time optimisation. Results are always fed back into next campaign and shared across digital teams.",
                        "choiceText": "Mix of robust A/B tests, consumer surveys and real-time optimisation. Results are always fed back into next campaign and shared across digital teams.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "3"
                            }
                        ]
                    },
                    "5": {
                        "recode": "4",
                        "description": "Mix of robust A/B tests, consumer surveys and real-time optimisation. Results are fed back into next campaign and shared across digital and non-digital teams.",
                        "choiceText": "Mix of robust A/B tests, consumer surveys and real-time optimisation. Results are fed back into next campaign and shared across digital and non-digital teams.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID106": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How fast do your primary owned channels load on mobile (e.g. msite, native app, web app)?\n<p class=\"h-c-footnote\">You can <a href=\"https://testmysite.withgoogle.com/\" target=\"_blank\" rel=\"noopener\">run a test using this tool.</a></p>",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q106",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "8 or more seconds.",
                        "choiceText": "8 or more seconds.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Between 8 and 5.1 seconds.",
                        "choiceText": "Between 8 and 5.1 seconds.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Between 5 and 3.1 seconds.",
                        "choiceText": "Between 5 and 3.1 seconds.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "3 seconds or faster.",
                        "choiceText": "3 seconds or faster.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID107": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How user friendly is the mobile user experience of your primary owned channels?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q107",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We haven't invested in an experience specific for mobile.",
                        "choiceText": "We haven't invested in an experience specific for mobile.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Basic functionalities work well on mobile, but overall not optimised for mobile usage.",
                        "choiceText": "Basic functionalities work well on mobile, but overall not optimised for mobile usage.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "All parts of our experience are convenient for mobile users.",
                        "choiceText": "All parts of our experience are convenient for mobile users.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Our experience leverages latest mobile capabilities (e.g. single sign-on, Accelerated Mobile Pages, Progressive Web Apps, Instant apps) and is considered best-in-class.",
                        "choiceText": "Our experience leverages latest mobile capabilities (e.g. single sign-on, Accelerated Mobile Pages, Progressive Web Apps, Instant apps) and is considered best-in-class.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID108": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which methods does your organisation use to tailor your primary owned channel (e.g. website, native app, web app)?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q108",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We don't use site personalisation.",
                        "choiceText": "We don't use site personalisation.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Basic site personalisation based on a few customer segments (e.g. new and signed-in users).",
                        "choiceText": "Basic site personalisation based on a few customer segments (e.g. new and signed-in users).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "3.33",
                        "description": "Advanced site personalisation using always-on testing that is based on cookied historical data and real-time predictive modelling (e.g. item recommendation). Primarily using online data.",
                        "choiceText": "Advanced site personalisation using always-on testing that is based on cookied historical data and real-time predictive modelling (e.g. item recommendation). Primarily using online data.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "3.33"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Advanced site personalisation using always-on testing that is based on cookied historical data and real-time predictive modelling (e.g. item recommendation). Using online and offline data (e.g. system or retail loyalty programmes).",
                        "choiceText": "Advanced site personalisation using always-on testing that is based on cookied historical data and real-time predictive modelling (e.g. item recommendation). Using online and offline data (e.g. system or retail loyalty programmes).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID109": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What level of tailoring does your organisation use for audience messaging in Display?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q109",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Same message served to all users.",
                        "choiceText": "Same message served to all users.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "choiceText": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Messages tailored by all available segments.",
                        "choiceText": "Messages tailored by all available segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "choiceText": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID110": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What level of tailoring does your organisation use for audience messaging in Video?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q110",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Same message served to all users.",
                        "choiceText": "Same message served to all users.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "choiceText": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Messages tailored by all available segments.",
                        "choiceText": "Messages tailored by all available segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "choiceText": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID112": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What level of tailoring does your organisation use for audience messaging in Search?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q112",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Same message served to all users.",
                        "choiceText": "Same message served to all users.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "choiceText": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Messages tailored by all available segments.",
                        "choiceText": "Messages tailored by all available segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "choiceText": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID113": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What level of tailoring does your organisation use for audience messaging in Social?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q113",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Same message served to all users.",
                        "choiceText": "Same message served to all users.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "choiceText": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Messages tailored by all available segments.",
                        "choiceText": "Messages tailored by all available segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "choiceText": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID114": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What level of tailoring does your organisation use for audience messaging in Email?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q114",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Same message served to all users.",
                        "choiceText": "Same message served to all users.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "choiceText": "Messages tailored by broad types of segments (e.g. existing customers and potential customers).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Messages tailored by all available segments.",
                        "choiceText": "Messages tailored by all available segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "choiceText": "Messages tailored by all available segments and other inputs such as location or time of day.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID115": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do you use insights from online assets to improve experiences in the offline world, (e.g. in stores, at events or in call centres)?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q115",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Limited or no use of insights from online assets.",
                        "choiceText": "Limited or no use of insights from online assets.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We occasionally share insights from online channels with offline teams.",
                        "choiceText": "We occasionally share insights from online channels with offline teams.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We have a robust process in place to improve people's experiences as they move from online assets to offline touchpoints.",
                        "choiceText": "We have a robust process in place to improve people's experiences as they move from online assets to offline touchpoints.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We have a robust process in place and have connected online and offline systems, (e.g. using web analytics data to provide tailored in-store experiences).",
                        "choiceText": "We have a robust process in place and have connected online and offline systems, (e.g. using web analytics data to provide tailored in-store experiences).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID116": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "<h2 class=\"dmb-dimension-header\">Access </h2>\nHow does your organisation approach frequency capping?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q116",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We usually set an arbitrary number or don't use frequency capping at all.",
                        "choiceText": "We usually set an arbitrary number or don't use frequency capping at all.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We set frequency caps based on our own path-to-conversion reports.",
                        "choiceText": "We set frequency caps based on our own path-to-conversion reports.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Frequency caps are based on insights from our own campaigns. We run tests to find the optimal balance between frequency and reach across all media buys.",
                        "choiceText": "Frequency caps are based on insights from our own campaigns. We run tests to find the optimal balance between frequency and reach across all media buys.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Frequency caps are based on insights from our own campaigns. We have consolidated nearly all media buys and we actively manage frequency across these media buys to achieve maximum reach and performance.",
                        "choiceText": "Frequency caps are based on insights from our own campaigns. We have consolidated nearly all media buys and we actively manage frequency across these media buys to achieve maximum reach and performance.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID117": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes how you buy digital media?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q117",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We mainly buy directly from publishers (reservation) or from ad networks.",
                        "choiceText": "We mainly buy directly from publishers (reservation) or from ad networks.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We mainly buy programmatically, using open auctions and programmatic direct. We optimise these buys separately for each channel.",
                        "choiceText": "We mainly buy programmatically, using open auctions and programmatic direct. We optimise these buys separately for each channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We mainly buy programmatically, using open auctions and programmatic direct. We optimise these buys across digital channels.",
                        "choiceText": "We mainly buy programmatically, using open auctions and programmatic direct. We optimise these buys across digital channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We mainly buy programmatically, using a variety of deal types (e.g. open and private auction, preferred and guaranteed deals). Our media buys are optimised across digital channels. Some non-digital media is bought programmatically.",
                        "choiceText": "We mainly buy programmatically, using a variety of deal types (e.g. open and private auction, preferred and guaranteed deals). Our media buys are optimised across digital channels. Some non-digital media is bought programmatically.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID118": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How diverse is your display and video marketing strategy?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q118",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We mostly buy desktop display and video.",
                        "choiceText": "We mostly buy desktop display and video.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We buy display and video across desktop and mobile websites. We follow an audience strategy for each within channel or format.",
                        "choiceText": "We buy display and video across desktop and mobile websites. We follow an audience strategy for each within channel or format.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We buy display and video across desktop, mobile websites, mobile apps, as native and non-native media. We apply audience and targeting strategies across some of our our channels or formats.",
                        "choiceText": "We buy display and video across desktop, mobile websites, mobile apps, as native and non-native media. We apply audience and targeting strategies across some of our our channels or formats.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We buy across all relevant channels, devices and formats. This includes digital TV and digital out-of-home. We follow a comprehensive audience strategy across all of them.",
                        "choiceText": "We buy across all relevant channels, devices and formats. This includes digital TV and digital out-of-home. We follow a comprehensive audience strategy across all of them.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID119": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How diverse is your search marketing strategy?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q119",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We advertise on keywords that are related to our brand and our most important products. We mostly rely on standard search ads.",
                        "choiceText": "We advertise on keywords that are related to our brand and our most important products. We mostly rely on standard search ads.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We advertise on keywords that are related to our brand, all of our products and product categories. We mainly use standard search ads and have started using specialised formats (e.g. shopping ads or local ads).",
                        "choiceText": "We advertise on keywords that are related to our brand, all of our products and product categories. We mainly use standard search ads and have started using specialised formats (e.g. shopping ads or local ads).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We advertise on keywords that are related to our brand, all of our products and product categories as well as other relevant terms. We use a mix of standard search ads and specialised formats (e.g. shopping ads or local ads).",
                        "choiceText": "We advertise on keywords that are related to our brand, all of our products and product categories as well as other relevant terms. We use a mix of standard search ads and specialised formats (e.g. shopping ads or local ads).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We advertise on an extensive set of keywords, covering all relevant terms, across all available search ad formats (e.g standard ads, shopping ads, local ads), all relevant platforms and device types. We make use of automated keyword selection where available (e.g. dynamic search ads).",
                        "choiceText": "We advertise on an extensive set of keywords, covering all relevant terms, across all available search ad formats (e.g standard ads, shopping ads, local ads), all relevant platforms and device types. We make use of automated keyword selection where available (e.g. dynamic search ads).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID161": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do you approach brand safety for digital media buys?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q161",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We use measures available in the platform's default settings.",
                        "choiceText": "We use measures available in the platform's default settings.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We use the platform's default settings and evaluate brand safety in our reports to add or remove individual sites to our whitelist or blacklist.",
                        "choiceText": "We use the platform's default settings and evaluate brand safety in our reports to add or remove individual sites to our whitelist or blacklist.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We use a dedicated brand safety solution on our most important channels and monitor reports to update our category filters.",
                        "choiceText": "We use a dedicated brand safety solution on our most important channels and monitor reports to update our category filters.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We use a dedicated brand safety solution across all channels, monitor reports, update category filters and generate insights to improve our brand safety solution.",
                        "choiceText": "We use a dedicated brand safety solution across all channels, monitor reports, update category filters and generate insights to improve our brand safety solution.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID120": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do you ensure sufficient viewability for your display and video buys?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q120",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No use of viewability measurement.",
                        "choiceText": "No use of viewability measurement.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We measure viewability in post-campaign reporting.",
                        "choiceText": "We measure viewability in post-campaign reporting.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Viewability metrics inform future media buys (e.g. by shifting budget).",
                        "choiceText": "Viewability metrics inform future media buys (e.g. by shifting budget).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Viewability metrics are actively used as a buying signal on programmatic platforms.",
                        "choiceText": "Viewability metrics are actively used as a buying signal on programmatic platforms.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID162": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do you ensure ad quality for display and video buys?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q162",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No or very little relevance for us as we buy media mostly on sites we know and trust (e.g. on reservation).",
                        "choiceText": "No or very little relevance for us as we buy media mostly on sites we know and trust (e.g. on reservation).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We are aware of ads.txt to declare authorised sellers and we monitor for potential fraud in our reports when we become aware of an issue.",
                        "choiceText": "We are aware of ads.txt to declare authorised sellers and we monitor for potential fraud in our reports when we become aware of an issue.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We regularly monitor fraud reports and optimise our media buys (e.g. by removing individual sites or sellers of aggregated inventory).",
                        "choiceText": "We regularly monitor fraud reports and optimise our media buys (e.g. by removing individual sites or sellers of aggregated inventory).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Active monitoring and optimising of media buys. Actively engaged with publishers on fraud prevention.",
                        "choiceText": "Active monitoring and optimising of media buys. Actively engaged with publishers on fraud prevention.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID121": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do you ensure ad quality for search?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q121",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We rely mostly on default methods by platforms, (e.g. disabling keyword combinations with low performance).",
                        "choiceText": "We rely mostly on default methods by platforms, (e.g. disabling keyword combinations with low performance).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We build negative keyword lists based on industry best practices and anecdotal evidence.",
                        "choiceText": "We build negative keyword lists based on industry best practices and anecdotal evidence.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We build negative keyword lists based on search query reports of previous campaigns.",
                        "choiceText": "We build negative keyword lists based on search query reports of previous campaigns.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We actively research potential negative keywords, monitor performance and share keyword lists across all campaigns.",
                        "choiceText": "We actively research potential negative keywords, monitor performance and share keyword lists across all campaigns.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID122": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "<h2 class=\"dmb-dimension-header\"> Audience </h2>\nWhat sources of insights do you use to build your audiences for display and video campaigns?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q122",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "choiceText": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We use 3rd party data and 1st party data (our own data) we capture within each channel.",
                        "choiceText": "We use 3rd party data and 1st party data (our own data) we capture within each channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We use 3rd party data and 1st party data we capture within this channel and from other channels.",
                        "choiceText": "We use 3rd party data and 1st party data we capture within this channel and from other channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "choiceText": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID123": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What sources of insights do you use to build your audiences for search campaigns?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q123",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "choiceText": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We use 3rd party data and 1st party data (our own data) we capture within this channel.",
                        "choiceText": "We use 3rd party data and 1st party data (our own data) we capture within this channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We use 3rd party data and 1st party data we capture within this channel and in other channels.",
                        "choiceText": "We use 3rd party data and 1st party data we capture within this channel and in other channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "choiceText": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID124": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What sources of insights do you use to build your audiences for social campaigns?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q124",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "choiceText": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We use 3rd party data and 1st party data (our own data) we capture within this channel.",
                        "choiceText": "We use 3rd party data and 1st party data (our own data) we capture within this channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We use 3rd party data and 1st party data we capture within this channel and in other channels.",
                        "choiceText": "We use 3rd party data and 1st party data we capture within this channel and in other channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "choiceText": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID125": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What sources of insights do you use to build your audiences for email campaigns?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q125",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "choiceText": "We rely mostly on 3rd party data, provided by platforms we advertise on.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We use 3rd party data and 1st party data (our own data) we capture within this channel.",
                        "choiceText": "We use 3rd party data and 1st party data (our own data) we capture within this channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We use 3rd party data and 1st party data we capture within this channel and in other channels.",
                        "choiceText": "We use 3rd party data and 1st party data we capture within this channel and in other channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "choiceText": "We use 3rd party data and 1st party data, creating a comprehensive source of insights that cover both online and offline behaviour.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID126": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes your audience definitions?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q126",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Audience is treated as a single segment.",
                        "choiceText": "Audience is treated as a single segment.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "A number of segments, based on socio-demographic data or spend data.",
                        "choiceText": "A number of segments, based on socio-demographic data or spend data.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "1.67",
                        "description": "A number of segments, based on personas (which are defined by their common behaviours or interests).",
                        "choiceText": "A number of segments, based on personas (which are defined by their common behaviours or interests).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "A number segments based on advanced analytics including machine learning methods.",
                        "choiceText": "A number segments based on advanced analytics including machine learning methods.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID127": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How many strategic audience segments do you have in your organisation?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q127",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We don't use audience segmentation.",
                        "choiceText": "We don't use audience segmentation.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "2 or 3 segments.",
                        "choiceText": "2 or 3 segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "4 or 5 segments.",
                        "choiceText": "4 or 5 segments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "6 segments or more.",
                        "choiceText": "6 segments or more.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID128": {
                "questionType": {
                    "type": "MC",
                    "selector": "MAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following targeting methods do you use?  (Select all that apply)",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q128",
                "choices": {
                    "1": {
                        "recode": "133.1",
                        "description": "Upper funnel targeting (e.g. to drive awareness).",
                        "choiceText": "Upper funnel targeting (e.g. to drive awareness).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "2": {
                        "recode": "133.2",
                        "description": "Lower funnel targeting (e.g. to drive sales).",
                        "choiceText": "Lower funnel targeting (e.g. to drive sales).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "133.3",
                        "description": "Mid funnel targeting (e.g. to drive consideration).",
                        "choiceText": "Mid funnel targeting (e.g. to drive consideration).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    }
                }
            },
            "QID129": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Do you use a Data Management Platform (DMP)?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q129",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No.",
                        "choiceText": "No.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "0",
                        "description": "Yes, operated by an external partner (e.g. an agency).",
                        "choiceText": "Yes, operated by an external partner (e.g. an agency).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Yes, operated by us.",
                        "choiceText": "Yes, operated by us.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Yes, operated by us and connected to other systems (e.g. a CRM tool).",
                        "choiceText": "Yes, operated by us and connected to other systems (e.g. a CRM tool).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID130": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How do you maintain your audience lists?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q130",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No audience maintenance (e.g. bespoke lists created for every campaign).",
                        "choiceText": "No audience maintenance (e.g. bespoke lists created for every campaign).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Retrospective audience maintenance (e.g. target list updated after the campaign has ended).",
                        "choiceText": "Retrospective audience maintenance (e.g. target list updated after the campaign has ended).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Audiences updated while campaign is running.",
                        "choiceText": "Audiences updated while campaign is running.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Continuous audience maintenance (e.g. rule-based and automated updates to target lists).",
                        "choiceText": "Continuous audience maintenance (e.g. rule-based and automated updates to target lists).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID131": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes how your organisation connects systems to get from data to insights that improve marketing activation?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q131",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Limited connectivity. Data used independently by channel, (e.g. 3rd party data for display or CRM data for email marketing).",
                        "choiceText": "Limited connectivity. Data used independently by channel, (e.g. 3rd party data for display or CRM data for email marketing).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Connectivity in online channels (e.g. building look-a-like audiences with a combination of 1st and 3rd party data).",
                        "choiceText": "Connectivity in online channels (e.g. building look-a-like audiences with a combination of 1st and 3rd party data).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Online and offline systems connected (e.g. direct mail systems linked to systems that manage 1st party digital data).",
                        "choiceText": "Online and offline systems connected (e.g. direct mail systems linked to systems that manage 1st party digital data).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Connected online and offline systems and include other contextual data (e.g. 1st party, 3rd party, business performance and weather data managed in a Data Management Platform).",
                        "choiceText": "Connected online and offline systems and include other contextual data (e.g. 1st party, 3rd party, business performance and weather data managed in a Data Management Platform).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID132": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Does your organisation or your agency use a CRM suite?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q132",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No.",
                        "choiceText": "No.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "0",
                        "description": "Yes, operated by an external partner (e.g. an agency).",
                        "choiceText": "Yes, operated by an external partner (e.g. an agency).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Yes, operated by us.",
                        "choiceText": "Yes, operated by us.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Yes, operated by us and connected to other systems (e.g. a Data Management Platform).",
                        "choiceText": "Yes, operated by us and connected to other systems (e.g. a Data Management Platform).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID133": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "<h2 class=\"dmb-dimension-header\">Automation</h2>\nHow do you manage hosting and delivering your creatives?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q133",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Don't know.",
                        "choiceText": "Don't know.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Some creatives are hosted in an ad-server.",
                        "choiceText": "Some creatives are hosted in an ad-server.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "All static creatives in an ad-sever.",
                        "choiceText": "All static creatives in an ad-sever.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "All creatives hosted in an ad-server including some of our dynamic assets.",
                        "choiceText": "All creatives hosted in an ad-server including some of our dynamic assets.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID134": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Do you use a DSP (Demand Side Platform)?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q134",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Don't know.",
                        "choiceText": "Don't know.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "0",
                        "description": "Yes, operated by an external partner (e.g. an agency).",
                        "choiceText": "Yes, operated by an external partner (e.g. an agency).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Yes, operated by us.",
                        "choiceText": "Yes, operated by us.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Yes, operated by us and connected to other systems (e.g. a web analytics tool).",
                        "choiceText": "Yes, operated by us and connected to other systems (e.g. a web analytics tool).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID135": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes how you setup and manage campaigns?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q135",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Don't know, or all campaign setup and management done by an agency partner.",
                        "choiceText": "Don't know, or all campaign setup and management done by an agency partner.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1",
                        "description": "We mainly use the existing ad platform user interface to setup and manage our campaigns.",
                        "choiceText": "We mainly use the existing ad platform user interface to setup and manage our campaigns.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "We use the platform user interface but also leverage platform APIs for campaign setup and reporting.",
                        "choiceText": "We use the platform user interface but also leverage platform APIs for campaign setup and reporting.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "3",
                        "description": "We make heavy use of platform APIs and structured data files for campaign setup and reporting.",
                        "choiceText": "We make heavy use of platform APIs and structured data files for campaign setup and reporting.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "3"
                            }
                        ]
                    },
                    "5": {
                        "recode": "4",
                        "description": "We make full use of various platform APIs and structured data files for campaigns setup, maintenance, optimisation and reporting.",
                        "choiceText": "We make full use of various platform APIs and structured data files for campaigns setup, maintenance, optimisation and reporting.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID136": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes your search bidding technique?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q136",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We mostly set bids manually.",
                        "choiceText": "We mostly set bids manually.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Bid adjustments (bid multipliers) based on signals such as usage of mobile devices or user location. Adjustments are updated frequently.",
                        "choiceText": "Bid adjustments (bid multipliers) based on signals such as usage of mobile devices or user location. Adjustments are updated frequently.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Bid adjustments based on several signals using simple automated rules.",
                        "choiceText": "Bid adjustments based on several signals using simple automated rules.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Use of automated bidding based on a multitude of factors such as user location, device type, cross-device behaviour, data-driven attribution and other signals.",
                        "choiceText": "Use of automated bidding based on a multitude of factors such as user location, device type, cross-device behaviour, data-driven attribution and other signals.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID137": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes your display and video bidding technique?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q137",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We mostly set bids manually.",
                        "choiceText": "We mostly set bids manually.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Bid adjustments (bid multipliers) based on signals such as usage of mobile devices or user location. Adjustments are updated frequently.",
                        "choiceText": "Bid adjustments (bid multipliers) based on signals such as usage of mobile devices or user location. Adjustments are updated frequently.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Bid adjustments based on several signals using simple automated rules.",
                        "choiceText": "Bid adjustments based on several signals using simple automated rules.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Use of automated bidding based on a multitude of factors such as user location, device type, cross-device behaviour, data-driven attribution and other signals.",
                        "choiceText": "Use of automated bidding based on a multitude of factors such as user location, device type, cross-device behaviour, data-driven attribution and other signals.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID138": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "To what extent have you automated your targeting?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q138",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We select most targeting criteria such as keywords and websites where our ads are running manually.",
                        "choiceText": "We select most targeting criteria such as keywords and websites where our ads are running manually.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "15": {
                        "recode": "1.33",
                        "description": "We have started using automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search or display.",
                        "choiceText": "We have started using automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search or display.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True
                    },
                    "16": {
                        "recode": "2.67",
                        "description": "We make full use of automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search or display.",
                        "choiceText": "We make full use of automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search or display.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True
                    },
                    "17": {
                        "recode": "4",
                        "description": "We make full use of automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search and display.",
                        "choiceText": "We make full use of automated targeting capabilities, providing only a campaign objective (e.g. target CPA), budget and creative assets across search and display.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True
                    }
                }
            },
            "QID163": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "To what extent have you automated optimising your creatives effectiveness?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q163",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Ads are created manually and optimised manually.",
                        "choiceText": "Ads are created manually and optimised manually.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1",
                        "description": "We create most ads manually and use standard platform features such as creative rotation. We optimise effectiveness manually.",
                        "choiceText": "We create most ads manually and use standard platform features such as creative rotation. We optimise effectiveness manually.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Dynamic creatives using mostly data feeds (e.g ad copy tailored based on user location or users' keyword). We use automated and manual optimisation equally. Automation mostly focused on one channel.",
                        "choiceText": "Dynamic creatives using mostly data feeds (e.g ad copy tailored based on user location or users' keyword). We use automated and manual optimisation equally. Automation mostly focused on one channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "3",
                        "description": "Dynamic creatives that use real-time messaging, based on data feeds and behavioural signals from within the channel and/or 3rd party data. Optimisation is mostly automated across several channels.",
                        "choiceText": "Dynamic creatives that use real-time messaging, based on data feeds and behavioural signals from within the channel and/or 3rd party data. Optimisation is mostly automated across several channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "3"
                            }
                        ]
                    },
                    "5": {
                        "recode": "4",
                        "description": "Dynamic creatives that use real-time messaging, based on cross-channel behavioural signals (e.g. shopping cart abandonment, products viewed) and/or 3rd party data. Optimisation is mostly automated across all channels.",
                        "choiceText": "Dynamic creatives that use real-time messaging, based on cross-channel behavioural signals (e.g. shopping cart abandonment, products viewed) and/or 3rd party data. Optimisation is mostly automated across all channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID139": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "<h2 class=\"dmb-dimension-header\">Attribution</h2>\nWhat tracking and tagging do you have in place?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q139",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Digital tracking and tagging in some channels.",
                        "choiceText": "Digital tracking and tagging in some channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Different forms of digital tracking and tagging in place across all channels.",
                        "choiceText": "Different forms of digital tracking and tagging in place across all channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Unified naming conventions for digital tracking and tagging across all channels and for major events on our websites.",
                        "choiceText": "Unified naming conventions for digital tracking and tagging across all channels and for major events on our websites.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Consistent digital tracking using container tags across all websites and apps, all campaigns are tagged. Important offline events are being captured.",
                        "choiceText": "Consistent digital tracking using container tags across all websites and apps, all campaigns are tagged. Important offline events are being captured.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID140": {
                "questionType": {
                    "type": "MC",
                    "selector": "MAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following performance metrics do you use to assess your marketing effectiveness? (select all that apply)",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q140",
                "choices": {
                    "1": {
                        "recode": "025.1",
                        "description": "Campaign metrics (e.g. Cost-per-Click).",
                        "choiceText": "Campaign metrics (e.g. Cost-per-Click).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0.25"
                            }
                        ]
                    },
                    "2": {
                        "recode": "050.2",
                        "description": "Conversion metrics (e.g. number of conversions).",
                        "choiceText": "Conversion metrics (e.g. number of conversions).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0.5"
                            }
                        ]
                    },
                    "3": {
                        "recode": "100.3",
                        "description": "Metrics that are proxies for conversions (e.g. footfall to physical stores or leads for test drives).",
                        "choiceText": "Metrics that are proxies for conversions (e.g. footfall to physical stores or leads for test drives).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "4": {
                        "recode": "100.4",
                        "description": "Revenue or profitability metrics (e.g. total revenue or return on ad spend).",
                        "choiceText": "Revenue or profitability metrics (e.g. total revenue or return on ad spend).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "5": {
                        "recode": "125.5",
                        "description": "Incremental revenue and customer lifetime value.",
                        "choiceText": "Incremental revenue and customer lifetime value.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.25"
                            }
                        ]
                    }
                }
            },
            "QID141": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Does your organisation or your agency have a consistent web analytics suite?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q141",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No, or don't know.",
                        "choiceText": "No, or don't know.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "0",
                        "description": "Yes, operated by an external partner (e.g. an agency).",
                        "choiceText": "Yes, operated by an external partner (e.g. an agency).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Yes, operated by us.",
                        "choiceText": "Yes, operated by us.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Yes, operated by us and connected to other systems (e.g. a demand side platform).",
                        "choiceText": "Yes, operated by us and connected to other systems (e.g. a demand side platform).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID142": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How consolidated and integrated is your reporting?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q142",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Reporting is done separately for each channel and platform. Performance is evaluated on a campaign level.",
                        "choiceText": "Reporting is done separately for each channel and platform. Performance is evaluated on a campaign level.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "We do some deduplication across search and display and we consider cross-device behaviour.",
                        "choiceText": "We do some deduplication across search and display and we consider cross-device behaviour.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "We have a comprehensive single-source of truth for digital. All digital media touchpoints and website behaviour are considered. Some non-digital data such as CRM or store visits are considered.",
                        "choiceText": "We have a comprehensive single-source of truth for digital. All digital media touchpoints and website behaviour are considered. Some non-digital data such as CRM or store visits are considered.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "We have a comprehensive single-source of truth for digital and non-digital channels. This includes consumer behaviour in stores, product data and CRM data.",
                        "choiceText": "We have a comprehensive single-source of truth for digital and non-digital channels. This includes consumer behaviour in stores, product data and CRM data.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID143": {
                "questionType": {
                    "type": "MC",
                    "selector": "MAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of these measurement methodologies do you use? (select all that apply)",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q143",
                "choices": {
                    "1": {
                        "recode": "050.1",
                        "description": "Brand tracking.",
                        "choiceText": "Brand tracking.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0.5"
                            }
                        ]
                    },
                    "2": {
                        "recode": "050.2",
                        "description": "Consumer surveys.",
                        "choiceText": "Consumer surveys.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0.5"
                            }
                        ]
                    },
                    "3": {
                        "recode": "100.3",
                        "description": "Marketing mix modelling (econometrics).",
                        "choiceText": "Marketing mix modelling (econometrics).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "4": {
                        "recode": "100.4",
                        "description": "Controlled experiments (e.g. geo experiments).",
                        "choiceText": "Controlled experiments (e.g. geo experiments).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "5": {
                        "recode": "100.5",
                        "description": "Attribution modelling.",
                        "choiceText": "Attribution modelling.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    }
                }
            },
            "QID144": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "What kind of attribution model does your organisation primarily use for digital channels?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q144",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We don't have an attribution model.",
                        "choiceText": "We don't have an attribution model.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "0",
                        "description": "Last-click model.",
                        "choiceText": "Last-click model.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "1.33",
                        "description": "Standard rule-based model (e.g. time decay).",
                        "choiceText": "Standard rule-based model (e.g. time decay).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "4": {
                        "recode": "2.67",
                        "description": "Custom rule-based model developed to our specifications.",
                        "choiceText": "Custom rule-based model developed to our specifications.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "5": {
                        "recode": "4",
                        "description": "Algorithmic or data-driven, fractional, multi-touch model.",
                        "choiceText": "Algorithmic or data-driven, fractional, multi-touch model.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID145": {
                "questionType": {
                    "type": "MC",
                    "selector": "MAVR",
                    "subSelector": "TX"
                },
                "questionText": "What data points do you consider in your attribution model? (select all that apply)",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q145",
                "choices": {
                    "1": {
                        "recode": "000.1",
                        "description": "We don't have an attribution model.",
                        "choiceText": "We don't have an attribution model.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "050.2",
                        "description": "We use data from several digital channels (e.g. video, search and display).",
                        "choiceText": "We use data from several digital channels (e.g. video, search and display).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "100.3",
                        "description": "We use data from all digital channels.",
                        "choiceText": "We use data from all digital channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "4": {
                        "recode": "100.4",
                        "description": "We consider cross-device behaviour.",
                        "choiceText": "We consider cross-device behaviour.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "5": {
                        "recode": "100.5",
                        "description": "We consider offline behaviour such as visits in retail locations or call centre interactions.",
                        "choiceText": "We consider offline behaviour such as visits in retail locations or call centre interactions.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID146": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How frequently do you run A/B tests? (Select the most relevant option)",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q146",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "We don't run A/B tests.",
                        "choiceText": "We don't run A/B tests.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "0",
                        "description": "Less than once a quarter.",
                        "choiceText": "Less than once a quarter.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "3": {
                        "recode": "1.33",
                        "description": "Once a month.",
                        "choiceText": "Once a month.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "4": {
                        "recode": "2.67",
                        "description": "Once a week.",
                        "choiceText": "Once a week.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "5": {
                        "recode": "4",
                        "description": "More than once a week.",
                        "choiceText": "More than once a week.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID147": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How would you describe the feedback mechanisms you have in place in your organisation's marketing activation?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q147",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Limited test and learn efforts. Results influence annual planning.",
                        "choiceText": "Limited test and learn efforts. Results influence annual planning.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Regular use of testing. Results influence next campaign.",
                        "choiceText": "Regular use of testing. Results influence next campaign.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Always-on testing. Results are used to optimise campaigns while they're running.",
                        "choiceText": "Always-on testing. Results are used to optimise campaigns while they're running.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Always-on testing. Results influence campaigns across channels while they're running.",
                        "choiceText": "Always-on testing. Results influence campaigns across channels while they're running.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID148": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "<h2 class=\"dmb-dimension-header\">Organisation</h2>\nAt what level in your organisation is data-driven marketing championed?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q148",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Limited senior sponsorship.",
                        "choiceText": "Limited senior sponsorship.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1",
                        "description": "Sponsored by mid-management (e.g. local director).",
                        "choiceText": "Sponsored by mid-management (e.g. local director).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2",
                        "description": "Sponsored by extended leadership (e.g. VP).",
                        "choiceText": "Sponsored by extended leadership (e.g. VP).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "4": {
                        "recode": "3",
                        "description": "Sponsored by senior leadership (e.g. CMO, CTO, COO).",
                        "choiceText": "Sponsored by senior leadership (e.g. CMO, CTO, COO).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "3"
                            }
                        ]
                    },
                    "5": {
                        "recode": "4",
                        "description": "Sponsored by CEO.",
                        "choiceText": "Sponsored by CEO.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID149": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Within your organisation do you have data scientists that support digital marketing activity?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q149",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No.",
                        "choiceText": "No.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "2",
                        "description": "Yes, but not fully dedicated.",
                        "choiceText": "Yes, but not fully dedicated.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "3": {
                        "recode": "4",
                        "description": "Yes, fully dedicated resource.",
                        "choiceText": "Yes, fully dedicated resource.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID150": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Within your organisation do you have dedicated measurement personnel that support digital marketing activity?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q150",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No.",
                        "choiceText": "No.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "2",
                        "description": "Yes, but not fully dedicated.",
                        "choiceText": "Yes, but not fully dedicated.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "3": {
                        "recode": "4",
                        "description": "Yes, fully dedicated resource.",
                        "choiceText": "Yes, fully dedicated resource.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID151": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Within your organisation do you have channel specialists (e.g. search, social, programmatic) that support digital marketing activity?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q151",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "No.",
                        "choiceText": "No.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "2",
                        "description": "Yes, but not fully dedicated.",
                        "choiceText": "Yes, but not fully dedicated.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2"
                            }
                        ]
                    },
                    "3": {
                        "recode": "4",
                        "description": "Yes, fully dedicated resource.",
                        "choiceText": "Yes, fully dedicated resource.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID152": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "How are the objectives of marketing channels in your organisation set?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q152",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Independent objectives by channel.",
                        "choiceText": "Independent objectives by channel.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Largely independent with some common objectives across channels.",
                        "choiceText": "Largely independent with some common objectives across channels.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Common objectives across multiple channels (e.g. across all digital channels).",
                        "choiceText": "Common objectives across multiple channels (e.g. across all digital channels).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Common objectives across all digital and non-digital channels, linked to overall business performance.",
                        "choiceText": "Common objectives across all digital and non-digital channels, linked to overall business performance.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID153": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes your organisation's process for marketing activation?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q153",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Marketing activation conducted at arm’s length through siloed teams or internal resources.",
                        "choiceText": "Marketing activation conducted at arm’s length through siloed teams or internal resources.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Relevant cross-channel roles and partners collaborate for large campaign launches. Day-to-day interaction is limited.",
                        "choiceText": "Relevant cross-channel roles and partners collaborate for large campaign launches. Day-to-day interaction is limited.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Established day-to-day processes and touchpoints across cross-channel roles and external partners.",
                        "choiceText": "Established day-to-day processes and touchpoints across cross-channel roles and external partners.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "Fully integrated and agile ways of working across channel teams, including all relevant eco-system partners.",
                        "choiceText": "Fully integrated and agile ways of working across channel teams, including all relevant eco-system partners.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID154": {
                "questionType": {
                    "type": "MC",
                    "selector": "SAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following best describes how your agency partners work together?",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q154",
                "choices": {
                    "1": {
                        "recode": "0",
                        "description": "Agencies work mostly independently.",
                        "choiceText": "Agencies work mostly independently.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "0"
                            }
                        ]
                    },
                    "2": {
                        "recode": "1.33",
                        "description": "Some cross-agency collaboration (e.g. creatives work with display but not with search).",
                        "choiceText": "Some cross-agency collaboration (e.g. creatives work with display but not with search).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1.33"
                            }
                        ]
                    },
                    "3": {
                        "recode": "2.67",
                        "description": "Cross-agency collaboration with regular all-agency meetings (e.g. for campaign planning).",
                        "choiceText": "Cross-agency collaboration with regular all-agency meetings (e.g. for campaign planning).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "2.67"
                            }
                        ]
                    },
                    "4": {
                        "recode": "4",
                        "description": "All agencies collaborate actively (e.g. on joint multi-agency projects or as virtual campaign teams).",
                        "choiceText": "All agencies collaborate actively (e.g. on joint multi-agency projects or as virtual campaign teams).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "4"
                            }
                        ]
                    }
                }
            },
            "QID155": {
                "questionType": {
                    "type": "MC",
                    "selector": "MAVR",
                    "subSelector": "TX"
                },
                "questionText": "Which of the following ways of working are consistently followed in your organisation? (Select all that apply)",
                "questionLabel": None,
                "validation": {
                    "doesForceResponse": True
                },
                "questionName": "Q155",
                "choices": {
                    "1": {
                        "recode": "050.1",
                        "description": "We have agile ways of working, (e.g. cross-functional teams working in sprints).",
                        "choiceText": "We have agile ways of working, (e.g. cross-functional teams working in sprints).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "2": {
                        "recode": "150.2",
                        "description": "We have a test and learn culture and there is budget set aside for running experiments.",
                        "choiceText": "We have a test and learn culture and there is budget set aside for running experiments.",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "3": {
                        "recode": "050.3",
                        "description": "We share marketing best practices, (e.g. between campaigns or across regions).",
                        "choiceText": "We share marketing best practices, (e.g. between campaigns or across regions).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    },
                    "4": {
                        "recode": "150.4",
                        "description": "We co-locate as part of cross-functional teams, (e.g. we sit together on one floor).",
                        "choiceText": "We co-locate as part of cross-functional teams, (e.g. we sit together on one floor).",
                        "imageDescription": None,
                        "variableName": None,
                        "analyze": True,
                        "scoring": [
                            {
                                "category": "SC_577ByjK0PVdnw69",
                                "value": "1"
                            }
                        ]
                    }
                }
            }
        },
        "exportColumnMap": {
            "Q97_4_TEXT": {
                "question": "QID97",
                "choice": "QID97.choices.4"
            },
            "Q97_5_TEXT": {
                "question": "QID97",
                "choice": "QID97.choices.5"
            },
            "Q173_1": {
                "question": "QID173",
                "choice": "QID173.choices.1"
            },
            "Q102": {
                "question": "QID102"
            },
            "Q103": {
                "question": "QID103"
            },
            "Q104": {
                "question": "QID104"
            },
            "Q105": {
                "question": "QID105"
            },
            "Q106": {
                "question": "QID106"
            },
            "Q107": {
                "question": "QID107"
            },
            "Q108": {
                "question": "QID108"
            },
            "Q109": {
                "question": "QID109"
            },
            "Q110": {
                "question": "QID110"
            },
            "Q112": {
                "question": "QID112"
            },
            "Q113": {
                "question": "QID113"
            },
            "Q114": {
                "question": "QID114"
            },
            "Q115": {
                "question": "QID115"
            },
            "Q116": {
                "question": "QID116"
            },
            "Q117": {
                "question": "QID117"
            },
            "Q118": {
                "question": "QID118"
            },
            "Q119": {
                "question": "QID119"
            },
            "Q161": {
                "question": "QID161"
            },
            "Q120": {
                "question": "QID120"
            },
            "Q162": {
                "question": "QID162"
            },
            "Q121": {
                "question": "QID121"
            },
            "Q122": {
                "question": "QID122"
            },
            "Q123": {
                "question": "QID123"
            },
            "Q124": {
                "question": "QID124"
            },
            "Q125": {
                "question": "QID125"
            },
            "Q126": {
                "question": "QID126"
            },
            "Q127": {
                "question": "QID127"
            },
            "Q128_133.1": {
                "question": "QID128",
                "choice": "QID128.choices.1"
            },
            "Q128_133.2": {
                "question": "QID128",
                "choice": "QID128.choices.2"
            },
            "Q128_133.3": {
                "question": "QID128",
                "choice": "QID128.choices.3"
            },
            "Q129": {
                "question": "QID129"
            },
            "Q130": {
                "question": "QID130"
            },
            "Q131": {
                "question": "QID131"
            },
            "Q132": {
                "question": "QID132"
            },
            "Q133": {
                "question": "QID133"
            },
            "Q134": {
                "question": "QID134"
            },
            "Q135": {
                "question": "QID135"
            },
            "Q136": {
                "question": "QID136"
            },
            "Q137": {
                "question": "QID137"
            },
            "Q138": {
                "question": "QID138"
            },
            "Q163": {
                "question": "QID163"
            },
            "Q139": {
                "question": "QID139"
            },
            "Q140_025.1": {
                "question": "QID140",
                "choice": "QID140.choices.1"
            },
            "Q140_050.2": {
                "question": "QID140",
                "choice": "QID140.choices.2"
            },
            "Q140_100.3": {
                "question": "QID140",
                "choice": "QID140.choices.3"
            },
            "Q140_100.4": {
                "question": "QID140",
                "choice": "QID140.choices.4"
            },
            "Q140_125.5": {
                "question": "QID140",
                "choice": "QID140.choices.5"
            },
            "Q141": {
                "question": "QID141"
            },
            "Q142": {
                "question": "QID142"
            },
            "Q143_050.1": {
                "question": "QID143",
                "choice": "QID143.choices.1"
            },
            "Q143_050.2": {
                "question": "QID143",
                "choice": "QID143.choices.2"
            },
            "Q143_100.3": {
                "question": "QID143",
                "choice": "QID143.choices.3"
            },
            "Q143_100.4": {
                "question": "QID143",
                "choice": "QID143.choices.4"
            },
            "Q143_100.5": {
                "question": "QID143",
                "choice": "QID143.choices.5"
            },
            "Q144": {
                "question": "QID144"
            },
            "Q145_000.1": {
                "question": "QID145",
                "choice": "QID145.choices.1"
            },
            "Q145_050.2": {
                "question": "QID145",
                "choice": "QID145.choices.2"
            },
            "Q145_100.3": {
                "question": "QID145",
                "choice": "QID145.choices.3"
            },
            "Q145_100.4": {
                "question": "QID145",
                "choice": "QID145.choices.4"
            },
            "Q145_100.5": {
                "question": "QID145",
                "choice": "QID145.choices.5"
            },
            "Q146": {
                "question": "QID146"
            },
            "Q147": {
                "question": "QID147"
            },
            "Q148": {
                "question": "QID148"
            },
            "Q149": {
                "question": "QID149"
            },
            "Q150": {
                "question": "QID150"
            },
            "Q151": {
                "question": "QID151"
            },
            "Q152": {
                "question": "QID152"
            },
            "Q153": {
                "question": "QID153"
            },
            "Q154": {
                "question": "QID154"
            },
            "Q155_050.1": {
                "question": "QID155",
                "choice": "QID155.choices.1"
            },
            "Q155_150.2": {
                "question": "QID155",
                "choice": "QID155.choices.2"
            },
            "Q155_050.3": {
                "question": "QID155",
                "choice": "QID155.choices.3"
            },
            "Q155_150.4": {
                "question": "QID155",
                "choice": "QID155.choices.4"
            }
        },
        "blocks": {
            "BL_4OcGZZcRLl0cRYp": {
                "description": "User Details",
                "elements": [
                    {
                        "type": "Question",
                        "questionId": "QID97"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID173"
                    }
                ]
            },
            "BL_d4IXvKmLwWF9lo9": {
                "description": "Real questions",
                "elements": [
                    {
                        "type": "Question",
                        "questionId": "QID102"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID103"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID104"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID105"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID106"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID107"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID108"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID109"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID110"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID112"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID113"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID114"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID115"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID116"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID117"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID118"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID119"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID161"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID120"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID162"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID121"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID122"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID123"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID124"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID125"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID126"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID127"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID128"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID129"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID130"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID131"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID132"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID133"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID134"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID135"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID136"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID137"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID138"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID163"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID139"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID140"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID141"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID142"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID143"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID144"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID145"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID146"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID147"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID148"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID149"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID150"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID151"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID152"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID153"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID154"
                    },
                    {
                        "type": "Question",
                        "questionId": "QID155"
                    }
                ]
            }
        },
        "flow": [
            {
                "type": "EmbeddedData"
            },
            {
                "type": "WebService"
            },
            {
                "id": "BL_4OcGZZcRLl0cRYp",
                "type": "Block"
            },
            {
                "id": "BL_d4IXvKmLwWF9lo9",
                "type": "Block"
            },
            {
                "type": "EmbeddedData"
            },
            {
                "type": "EndSurvey"
            }
        ],
        "embeddedData": [
            {
                "name": "sid"
            },
            {
                "name": "Enter Embedded Data Field Name Here..."
            },
            {
                "name": "sponsor"
            },
            {
                "name": "company_name",
                "type": "Custom"
            },
            {
                "name": "dmb",
                "defaultValue": "${gr://SC_577ByjK0PVdnw69/WeightedMean}"
            }
        ],
        "comments": {
            "QID3": {
                "commentList": [
                    {
                        "userId": "UR_eQjASeYvNZoXnPD",
                        "message": "Hero element",
                        "timestamp": 1519214611
                    }
                ]
            }
        },
        "loopAndMerge": {},
        "responseCounts": {
            "auditable": 256,
            "generated": 0,
            "deleted": 104
        }
    }

    survey_result = get_object_or_404(SurveyResult, response_id=response_id)
    # serializer_survey_result = SurveyResultSerializer(survey_result)
    # serialized_survey = SurveySerializer(survey_result.survey)


    return render(request, 'public/result-detail.html', {
        'result_detail': get_response_detail(definition, result_data),
        'survey_result': survey_result,
        'survey': survey_result.survey,
    })


def handler404(request):
    return render(request, 'public/error.html', {
        'title': '404',
        'subtitle': "Woops.. that page doesn't seem to exist, or the link is broken.",
        'text': 'Try returning to the homepage.',
        'cta': 'Return to homepage',
    }, status=404)


def handler500(request):
    return render(request, 'public/error.html', {
        'title': '500',
        'subtitle': 'Woops.. there was an internal server error.',
        'text': 'Try returning to the homepage.',
        'cta': 'Return to homepage',
    }, status=500)
