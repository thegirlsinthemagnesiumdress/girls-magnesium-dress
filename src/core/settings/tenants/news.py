# coding=utf-8
# flake8: noqa
from django.utils.translation import gettext_lazy as _

DIMENSION_STRATEGIC_DIRECTION = "strategic_direction"
DIMENSION_READER_ENGAGEMENT = "reader_engagement"
DIMENSION_READER_REVENUE = "reader_revenue"
DIMENSION_ADVERTISING_REVENUE = "advertising_revenue"

LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

WEIGHTS = {
    'Q4': 0.2,
    'Q5': 0.15,
    'Q6': 0.15,
    'Q7': 0.2,
    'Q8': 0.15,
    'Q9': 0.15,
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
    DIMENSION_STRATEGIC_DIRECTION: _('Strategic direction and data foundations'),
    DIMENSION_READER_ENGAGEMENT: _('Reader Engagement'),
    DIMENSION_READER_REVENUE: _('Reader Revenue'),
    DIMENSION_ADVERTISING_REVENUE: _('Advertising Revenue'),
}


DIMENSIONS_ORDER = [
    DIMENSION_STRATEGIC_DIRECTION,
    DIMENSION_READER_ENGAGEMENT,
    DIMENSION_READER_REVENUE,
    DIMENSION_ADVERTISING_REVENUE,
]


# If a question ID is not added to this list the question won't be considered for the final score
DIMENSIONS = {
    DIMENSION_STRATEGIC_DIRECTION: [
        'Q4',
        'Q5',
        'Q6',
        'Q7',
        'Q8',
        'Q9',
        'Q10',
    ],
    DIMENSION_READER_ENGAGEMENT: [
        'Q11',
        'Q12',
        'Q13',
    ],
    DIMENSION_READER_REVENUE: [
        'Q14',
        'Q15',
        'Q16',
    ],
    DIMENSION_ADVERTISING_REVENUE: [
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
        DIMENSION_STRATEGIC_DIRECTION: 0.4,
        DIMENSION_READER_ENGAGEMENT: 0.3,
        DIMENSION_READER_REVENUE: 0.0,
        DIMENSION_ADVERTISING_REVENUE: 0.3,
    },
    2: {
        DIMENSION_STRATEGIC_DIRECTION: 0.4,
        DIMENSION_READER_ENGAGEMENT: 0.3,
        DIMENSION_READER_REVENUE: 0.3,
        DIMENSION_ADVERTISING_REVENUE: 0.0,
    },
    3: {
        DIMENSION_STRATEGIC_DIRECTION: 0.4,
        DIMENSION_READER_ENGAGEMENT: 0.2,
        DIMENSION_READER_REVENUE: 0.2,
        DIMENSION_ADVERTISING_REVENUE: 0.2,
    }
}


LEVELS = {
    LEVEL_0: _('Nascent'),
    LEVEL_1: _('Developing'),
    LEVEL_2: _('Mature'),
    LEVEL_3: _('Leading'),
}


LEVELS_DESCRIPTIONS = {
    LEVEL_0: _('Organizations at this stage have the basic tools, but they often face cultural challenges to truly embracing data-supported decision-making.'),
    LEVEL_1: _('These organizations are able to drive value from data in some pockets of their business. Leadership recognises data as a priority, but is unclear on how to unlock the best returns.'),
    LEVEL_2: _('Data-informed decision making is the standard across much of the business. While the technology and tools support various use cases, they are mostly on a project basis and not business as usual.'),
    LEVEL_3: _('These organizations see data as an integral part of achieving their strategic objectives. They experiment with innovative, data-oriented projects and technologies that help drive the industry forward.'),
}

REPORT_LEVEL_DESCRIPTIONS = {
    LEVEL_0: _('This is the most basic of the four levels of maturity. You have the basic tools, but often face cultural challenges to truly embracing data-supported decision-making.'),
    LEVEL_1: _('This is the second of the four levels of maturity. You are able to drive value from data in some pockets of the business. Leadership recognises data as a priority, but is unclear on how to unlock the best returns.'),
    LEVEL_2: _('This is the third of the four levels of maturity. Data-informed decision-making is the standard across much of your organization. While the technology and tools support various use cases, they are mostly on a project basis and not business as usual.'),
    LEVEL_3: _('This is the most advanced of the four levels of maturity. These organizations see data as an integral part of achieving their strategic objectives. They experiment with innovative, data-oriented projects and technologies that help drive the industry forward.'),
}

DIMENSION_HEADER_DESCRIPTION = {
    DIMENSION_STRATEGIC_DIRECTION: _('Doing this well means that data is understood universally, it supports key business objectives, and there are robust data resources and technologies in place.'),
    DIMENSION_READER_ENGAGEMENT: _('Reader engagement is crucial to acquiring and retaining readers and increasing share of attention. Without an engaged readership, a news company cannot secure the subscription and advertising opportunities it needs to survive and thrive.'),
    DIMENSION_READER_REVENUE: _('News companies that successfully build valuable direct-to-consumer relationships with their readers not only see the near-term benefits of increased revenue but also reduce operating volatility through long-term, recurring revenue streams.'),
    DIMENSION_ADVERTISING_REVENUE: _('Leading news companies know their readers better than anyone, and they create content to attract and retain those readers. They act as advisors in the creative and campaign development process to deliver high-impact, relevant advertising that does not diminish the reader experience.'),
}

DIMENSION_LEVEL_DESCRIPTION = {
    DIMENSION_STRATEGIC_DIRECTION: {
        LEVEL_0: _('You have limited strategy in connecting data with your overarching business goals.'),
        LEVEL_1: _('Leadership have provided an initial articulation of specific and well-defined data initiatives, but there is limited continued focus on this.'),
        LEVEL_2: _('There is widespread knowledge and respect for the role data plays in achieving the overall business strategy.'),
        LEVEL_3: _('There is universal understanding of how data underpins the overarching business strategy, at all levels.'),
    },
    DIMENSION_READER_ENGAGEMENT: {
        LEVEL_0: _('You collect basic engagement data (i.e., page views), but do not translate it into audience insights. Content decisions are primarily based on instinct and editorial experience.'),
        LEVEL_1: _('You know what the broad audience segments are and start to uncover discrete audience insights using basic web analytics tools. However, reader experience and content decisions are still driven by “gut instinct.”'),
        LEVEL_2: _('You understand how different segments engage with content and use these insights to improve engagement. Meanwhile, the editorial team actively use engagement insights and data to improve content format (i.e., headlines, length).'),
        LEVEL_3: _('You clearly understand the context of the full reader journey and why audiences engage. You tailor the reader experience for different segments and occasions. Meanwhile, editorial decisions are generally data-informed.'),
    },
    DIMENSION_READER_REVENUE: {
        LEVEL_0: _('Your paid content offering is limited to one size fits all.'),
        LEVEL_1: _('You use metrics to develop promotions or price tiers for paid content offerings. You understand conversion triggers such as registration, login, and subscription.'),
        LEVEL_2: _('You use different products to improve the reader’s journey and determine how to bundle these products for different audiences. Your business is starting to explore using LTV-focused metrics and beginning to understand subscription and churn drivers.'),
        LEVEL_3: _('You have differentiated products that are relevant to readers across their life cycles. The portfolio of products are mutually reinforcing and drive loyalty and LTV. You understand the needs and behaviors of readers at different stages in their life cycles.'),
    },
    DIMENSION_ADVERTISING_REVENUE: {
        LEVEL_0: _('You have basic segments (demographics, location) in place for audience-based advertising.'),
        LEVEL_1: _('You use combinations of pre-built segments to assemble campaigns for advertisers. Meanwhile, you use exchanges / PMPs in a reactive way, primarily to monetize remnant inventory.'),
        LEVEL_2: _('You use different data sets to build interest and intent-based segments. You share insights and equip the sales team to clearly communicate the value of different segments to advertisers. You use exchanges / PMPs in a strategic way to optimize yield.'),
        LEVEL_3: _('You build unique segments using enriched first party data that gets to the heart of reader interest & intent. You proactively collaborate with advertisers & agencies to craft campaigns that incorporate unique audience insights.'),
    },
}

DATA_FOUNDATION_GUIDE_CTA = {
    'text': _('Data Activation Guide'),
    'link': 'http://www2.deloitte.com/content/dam/Deloitte/us/Documents/technology-media-telecommunications/us-digital-transformation-through-data-for-news.pdf#page=7',
}

ACTIVATING_USE_CASES_GUIDE_CTA = {
    'text': _('Data Activation Guide'),
    'link': 'http://www2.deloitte.com/content/dam/Deloitte/us/Documents/technology-media-telecommunications/us-digital-transformation-through-data-for-news.pdf#page=17',
}

DIMENSION_LEVEL_RECOMMENDATIONS = {
    DIMENSION_STRATEGIC_DIRECTION: {
        LEVEL_0: [{
            'header': _('Broadcast a thoughtful data strategy'),
            'text': _('Articulate your broader organizational mission, and identify areas in which data may be able to support or drive efforts to meet the mission.'),
        }, {
            'header': _('Foster collaboration and cross-functional teamwork'),
            'text': _('Identify opportunities to align data functions with the centers of influence in the organization.'),
        }, {
            'header': _('Embed data-informed decision making'),
            'text': _('Institute systems to evaluate decisions based on empirical analysis. Reward evidence-based rationale for operational decision-making.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_1: [{
            'header': _('Broadcast a thoughtful data strategy'),
            'text': _('Craft messaging that captures your organization`s approach to handling and activating data. Encourage leadership at all levels to communicate this message to team members.'),
        }, {
            'header': _('Foster collaboration and cross-functional teamwork'),
            'text': _('Establish educational sessions in which representatives from the data team provide information and training on key aspects of the data operation to team members throughout the organization.'),
        }, {
            'header': _('Embed data-informed decision making'),
            'text': _('Provide access to tools that enable and encourage colleagues to analyze decision criteria and execute data-supported decisions.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_2: [{
            'header': _('Broadcast a thoughtful data strategy'),
            'text': _('Craft messaging that captures your organization`s approach to handling and activating data. Encourage leadership at all levels to communicate this message to team members.'),
        }, {
            'header': _('Foster collaboration and cross-functional teamwork'),
            'text': _('Incorporate data strategy messaging in team meetings. Establish key performance indicators (KPIs) that drive collaboration across organizational silos and incentivise cross-functional performance.'),
        }, {
            'header': _('Democratize your data'),
            'text': _('Create intuitive tools and portals that enable access to relevant audience data for all team members. Provide trainings and educational resources to team members and encourage use of available resources.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Mature publishers have a well-established data strategy but want to see what other publishers are doing. Start with the Data Foundations section of the Data Activation Guide to see how some Leading publishers have developed their cultural, skills-based, data-related, and technological foundations.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_3: [{
            'header': _('Broadcast a thoughtful data strategy'),
            'text': _('Craft messaging that captures your organization`s approach to handling and activating data. Encourage leadership at all levels to communicate this message to team members.'),
        }, {
            'header': _('Foster collaboration and cross-functional teamwork'),
            'text': _('Continue regular cadence of cross-functional team meetings and craft incentives to encourage further collaboration across the organization.'),
        }, {
            'header': _('Attract the right talent'),
            'text': _('Communicate the unique emphasis your organization places on being data-informed, and establish recruiting partnerships to maintain a strong pipeline of technical professionals.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Leading publishers have a well-established data strategy but want to see what other publishers are doing. Start with the Data Foundations section of the Data Activation Guide to see how other Leading publishers have developed their cultural, skills-based, data-related, and technological foundations.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
    },
    DIMENSION_READER_ENGAGEMENT: {
        LEVEL_0: [{
            'header': _('Measure it to improve it'),
            'text': _('Drive collaboration amongst data teams and business leaders to prioritize data collection activities and measurement capabilities.'),
        }, {
            'header': _('Understand what makes your audience tick'),
            'text': _('Develop basic segmentation processes that capture high-level interest-based or behavioral segments for analysis. Understand your different segments of readers and how they engage with your content and your platform.'),
        }, {
            'header': _('Connect data to your content'),
            'text': _('Deploy a content tagging technology system and develop a common taxonomy to improve the searchability of your content library.'),
        }, {
            'header': _('Make the experience intuitive'),
            'text': _('Build your team`s skills in web analytics to better understand and improve pain points in the reader journey.'),
        }, {
            'header': _('Unlock insights from your Google Analytics data'),
            'text': _('Understand your different segments of readers and how they engage with your site'),
            'cta': {
                'text': _('News Consumer Insights'),
                'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
            },
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_1: [{
            'header': _('Measure it to improve it'),
            'text': _('Identify organizational objectives and tie key performance metrics to those objectives.'),
        }, {
            'header': _('Understand what makes your audience tick'),
            'text': _('Build technical teams to enhance segmentation practices and improve on foundational understandings of how audiences engage with your platform.'),
        }, {
            'header': _('Connect data to your content'),
            'text': _('Deploy technology solutions to support cross-functional collaboration between data and editorial teams and help guide content decisions.'),
        }, {
            'header': _('Make the experience intuitive'),
            'text': _('Capture and organize audience on-site behavioral data to inform user interface and design decisions.'),
        }, {
            'header': _('Unlock insights from your Google Analytics data'),
            'text': _('Understand your different segments of readers and how they engage with your site.'),
            'cta': {
                'text': _('News Consumer Insights'),
                'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
            },
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_2: [{
            'header': _('Measure it to improve it'),
            'text': _('Make analytics and reporting accessible to relevant team members, so everyone in the organization can understand the health and performance of the digital platform.'),
        }, {
            'header': _('Understand what makes your audience tick'),
            'text': _('Build new audience segments and enhance reader profiles to better tailor content and user interface decisions to satisfy specific reader preferences.'),
        }, {
            'header': _('Organize your content for future opportunities'),
            'text': _('Maintain your content catalog and provide intuitive tools to editorial teams to help surface insights that can inform content planning activities.'),
        }, {
            'header': _('Promote experimentation'),
            'text': _('Use A/B and multivariate tests to frequently identify areas to improve user interface and content options for readers. Promote a culture of testing and learning to drive continual improvement.'),
        }, {
            'header': _('Unlock insights from your Google Analytics data'),
            'text': _('Understand your different segments of readers and how they engage with your site.'),
            'cta': {
                'text': _('News Consumer Insights'),
                'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
            },
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Mature publishers have sophisticated approaches to improving overall reader engagement but want to see what other publishers are doing.The Activating Use Cases section of the Data Activation Guide details how some Leading publishers have approached improving overall reader engagement.'),
            'cta': ACTIVATING_USE_CASES_GUIDE_CTA,
        },
        ],
        LEVEL_3: [{
            'header': _('Measure it to improve it'),
            'text': _('Continue to roll out analytics and reporting tools to support cross-functional and performance-based decision-making.'),
        }, {
            'header': _('Understand what makes your audience tick'),
            'text': _('Enhance technological capabilities and data collection efforts to refine the understanding of specific audience segments and individual reader profiles. Continue to uncover insights that inform best ways to serve readers.'),
        }, {
            'header': _('Focus on optimizing the impact of your content'),
            'text': _('Continue to integrate relevant audience insights and tools with the editorial and product teams to serve your readers what they want, while maintaining the integrity of your editorial mission.'),
        }, {
            'header': _('Unlock insights from your Google Analytics data'),
            'text': _('Understand your different segments of readers and how they engage with your site.'),
            'cta': {
                'text': _('News Consumer Insights'),
                'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
            },
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Leading publishers have a sophisticated approach to improving overall reader engagement but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading publishers have approached improving overall reader engagement.'),
            'cta': ACTIVATING_USE_CASES_GUIDE_CTA,
        },
        ],
    },
    DIMENSION_READER_REVENUE: {
        LEVEL_0: [{
            'header': _('Understand the value of your readers'),
            'text': _('Understand your different segments of readers and how they engage with your content and your platform. Implement simple plug-in tools to help you measure and visualize these reader segments and how much value they bring.'),
            'cta': {
                'text': _('News Consumer Insights'),
                'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
            },
        }, {
            'header': _('Tailor your subscription approach'),
            'text': _('Understand the needs and behaviors of your readers and collaborate cross-functionally to develop strategies to convert them into subscribers.'),
        }, {
            'header': _('Identify new revenue models'),
            'text': _('Identify engaged segments of your audience and explore new offerings that they may want. These might be opportunities that you develop on your own, or you may need to seek partners to support.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_1: [{
            'header': _('Understand the value of your readers'),
            'text': _('Start to layer in more behavioral data that tells you how readers behave online and how those behaviors can translate to publisher value. Use reader insights to identify new ways to increase reader value (i.e., tailored communications, recommendations, and subscription offers).'),
        }, {
            'header': _('Tailor your subscription approach'),
            'text': _('Segment your readers based on their behavior and measure how effective your subscription promotions are with different reader types. Tailor how you communicate with them based on the feedback.'),
        }, {
            'header': _('Integrate your different revenue models'),
            'text': _('Integrate your data across different product or service offerings to get an understanding of reader behavior across the whole businesses. Develop the capability to identify readers and structure opportunities to cross-sell.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_2: [{
            'header': _('Understand the value of your readers '),
            'text': _('Integrate a view of reader lifetime value (LTV) into core business decision-making. Ensure that core functions in the marketing, editorial, and product teams consider the impact on reader LTV when making key decisions.'),
        }, {
            'header': _('Tailor your subscription approach'),
            'text': _('Employ sophisticated techniques (e.g., dynamic pricing) to tailor subscription offers and match them to specific segments based on their behavior on your platform. Create a feedback loop to analyze the results and understand points of improvement.'),
        }, {
            'header': _('Develop reinforcing revenue models'),
            'text': _('Actively cross-promote different titles or businesses based on reader interests or characteristics. Start to understand the relative value of decisions to direct readers between sites and products.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Mature publishers have created significant revenue from increasing direct-paying reader relationships but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading publishers have approached increasing direct-paying reader relationships.'),
            'cta': ACTIVATING_USE_CASES_GUIDE_CTA,
        },
        ],
        LEVEL_3: [{
            'header': _('Understand the value of your readers'),
            'text': _('Continue to refine the approach to quantifying reader lifetime value (LTV). Leverage reader LTV data to inform operational improvements and identify strategic growth opportunities.'),
        }, {
            'header': _('Tailor your subscription approach'),
            'text': _('Continually improve the approach to converting and retaining subscribers based on updates to predictive models and subscription pricing strategies.'),
        }, {
            'header': _('Pursue attractive adjacent business opportunities'),
            'text': _('Leverage your unique audience insights to identify and support strategic decisions to pursue opportunities that can generate new revenue for the business.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Leading publishers have a sophisticated approach to increasing direct-paying reader relationships but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading publishers have approached increasing direct-paying reader relationships.'),
            'cta': ACTIVATING_USE_CASES_GUIDE_CTA,
        },
        ],
    },
    DIMENSION_ADVERTISING_REVENUE: {
        LEVEL_0: [{
            'header': _('Measure it to improve it'),
            'text': _('Identify organizational objectives and tie key performance metrics to those objectives.'),
        }, {
            'header': _('Understand what makes your audience tick'),
            'text': _('Build technical teams to enhance segmentation practices and improve on foundational understandings of how audiences engage with your platform.'),
        }, {
            'header': _('Connect data to your content'),
            'text': _('Deploy technology solutions to support cross-functional collaboration between data and editorial teams and help guide content decisions.'),
        }, {
            'header': _('Make the experience intuitive'),
            'text': _('Capture and organize audience on-site behavioral data to inform user interface and design decisions.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_1: [{
            'header': _('Build and enhance the understanding of your audience '),
            'text': _('Start to layer in data that tells you how readers behave online and how this impacts the value they bring.  Build technical teams to enhance segmentation practices and improve on foundational understandings of how audiences engage with your platform.'),
        }, {
            'header': _('Connect the right audience to the right advertiser'),
            'text': _('Collaborate with your advertisers to identify the audiences they want to reach.  Start incorporating advertiser input into audience segmentation practices.'),
        }, {
            'header': _('Know the value of your audience'),
            'text': _('Monitor the performance of different audiences across your sales mix. Analyze and record insights across segments to develop a long-term understanding of audience segment performance.'),
        }, {
            'header': _('Make the most of your platform mix'),
            'text': _('Review historical performance of advertising sales across channels to begin developing a successful sales mix strategy.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.'),
            'cta': DATA_FOUNDATION_GUIDE_CTA,
        },
        ],
        LEVEL_2: [{
            'header': _('Build and enhance the understanding of your audience '),
            'text': _('Integrate a view of reader lifetime value (LTV) into core business decision-making. Experiment to test the relative value and performance of audience segments to refine high demand segments. Develop systems to effectively price audience segments based on historical performance and perceived value.'),
        }, {
            'header': _('Connect the right audience to the right advertiser'),
            'text': _('Continue to foster relationships with key advertisers, and collaborate to proactively identify ways to support their future advertising strategies.'),
        }, {
            'header': _('Bring campaigns to life'),
            'text': _('Think about advertising holistically and drive value through the strategic combination of relevant context, creative, advertising placement, and advertising format.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Mature publishers generate significant revenue through advertising but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading publishers have approached driving revenue from advertisers.'),
            'cta': ACTIVATING_USE_CASES_GUIDE_CTA,
        },
        ],
        LEVEL_3: [{
            'header': _('Build and enhance the understanding of your audience '),
            'text': _('Integrate a view of reader lifetime value (LTV) into core business decision-making. Experiment to test the relative value and performance of audience segments to refine high demand segments. Develop systems to effectively price audience segments based on historical performance and perceived value.'),
        }, {
            'header': _('Connect the right audience to the right advertiser'),
            'text': _('Continue to foster relationships with key advertisers, and collaborate to proactively identify ways to support their future advertising strategies through the strategic combination of relevant context, creative, advertising placement, and advertising format.'),
        }, {
            'header': _('Use technology to scale '),
            'text': _('Enhance technological capabilities, including focusing on direct programmatic, to effectively serve advertisers at scale without sacrificing quality of content or reader experience.'),
        }, {
            'header': _('Data Activation Guide'),
            'text': _('Many Leading publishers have a sophisticated approach to driving revenue from advertisers but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading publishers have approached driving revenue from advertisers.'),
            'cta': ACTIVATING_USE_CASES_GUIDE_CTA,
        },
        ],
    },
}


CONTENT_DATA = {
    'levels': LEVELS,
    'level_descriptions': LEVELS_DESCRIPTIONS,
    'report_level_descriptions': REPORT_LEVEL_DESCRIPTIONS,
    'dimensions': DIMENSIONS_ORDER,
    'dimension_labels': DIMENSION_TITLES,
    'dimension_headers_descriptions': DIMENSION_HEADER_DESCRIPTION,
    'dimension_level_description': DIMENSION_LEVEL_DESCRIPTION,
    'dimension_level_recommendations': DIMENSION_LEVEL_RECOMMENDATIONS,
}
