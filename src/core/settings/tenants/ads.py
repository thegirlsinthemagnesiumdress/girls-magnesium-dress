# coding=utf-8
# flake8: noqa
DIMENSION_ADS = 'ads'
DIMENSION_ACCESS = 'access'
DIMENSION_AUDIENCE = 'audience'
DIMENSION_ATTRIBUTION = 'attribution'
DIMENSION_AUTOMATION = 'automation'
DIMENSION_ORGANIZATION = 'organization'

LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3


WEIGHTS = {
    'Q106': 0.25,
    'Q107': 0.25,
    'Q109': 0.3,
    'Q110': 0.3,
    'Q112': 0.3,
    'Q113': 0.3,
    'Q114': 0.3,
    'Q122': 0.5,
    'Q123': 0.5,
    'Q124': 0.5,
    'Q125': 0.5,
    'Q127': 0.4,
    'Q128': 0.6,
    'Q136': 1.25,
    'Q137': 1.25,
    'Q138': 1.25,
    'Q144': 0.5,
    'Q145': 0.5,
    'Q148': 0.5,
    'Q149': 1.25,
    'Q150': 0.75,
    'Q153': 0.5,
    'Q155': 2,
    'Q163': 1.25,
}

DIMENSION_TITLES = {
    DIMENSION_ADS: 'Assets and ads',
    DIMENSION_ACCESS: 'Access',
    DIMENSION_AUDIENCE: 'Audience',
    DIMENSION_ATTRIBUTION: 'Attribution',
    DIMENSION_AUTOMATION: 'Automation',
    DIMENSION_ORGANIZATION: 'Organization',
}

# If a question ID is not added to this list the question won't be considered for the final score
DIMENSIONS = {
    DIMENSION_ADS: [
        'Q102',
        'Q103',
        'Q104',
        'Q105',
        'Q106',
        'Q107',
        'Q108',
        'Q109',
        'Q110',
        'Q112',
        'Q113',
        'Q114',
        'Q115',
    ],
    DIMENSION_ACCESS: [
        'Q116',
        'Q117',
        'Q118',
        'Q119',
        'Q161',
        'Q120',
        'Q162',
        'Q121',
    ],
    DIMENSION_AUDIENCE: [
        'Q122',
        'Q123',
        'Q124',
        'Q125',
        'Q126',
        'Q127',
        'Q128',
        'Q129',
        'Q130',
        'Q131',
        'Q132',
    ],
    DIMENSION_AUTOMATION: [
        'Q133',
        'Q134',
        'Q135',
        'Q136',
        'Q137',
        'Q138',
        'Q163',
    ],
    DIMENSION_ATTRIBUTION: [
        'Q139',
        'Q140',
        'Q141',
        'Q142',
        'Q143',
        'Q144',
        'Q145',
        'Q146',
        'Q147',
    ],
    DIMENSION_ORGANIZATION: [
        'Q148',
        'Q149',
        'Q150',
        'Q151',
        'Q152',
        'Q153',
        'Q154',
        'Q155',
    ],
}


MULTI_ANSWER_QUESTIONS = [
    'Q128',
    'Q140',
    'Q143',
    'Q145',
    'Q155',
]

LEVELS = {
    LEVEL_0: 'Nascent',
    LEVEL_1: 'Emerging',
    LEVEL_2: 'Connected',
    LEVEL_3: 'Multi-moment',
}

LEVELS_DESCRIPTIONS = {
    LEVEL_0: 'Marketing campaigns use mainly external data and direct buys, with limited links to sales.',
    LEVEL_1: 'Some use of owned data in automated buying with single-channel optimisation and testing.',
    LEVEL_2: 'Data integrated and activated across channels with demonstrated link to ROI or sales proxies.',
    LEVEL_3: 'Dynamic execution across multiple channels, optimised toward individual customer business outcomes and transactions.',
}

DIMENSION_HEADER_DESCRIPTION = {
    DIMENSION_ATTRIBUTION: 'Great attribution means accurately measuring and ascribing value to all consumer touch-points, so you make informed investment decisions and create even better, even more impactful experiences.',
    DIMENSION_ADS: 'Reaching consumers is not enough. They demand assistive experiences – fast, frictionless and tailored to their specific needs. You need to deliver intuitive and effective experiences across all brand digital touchpoints, including your website, your app, ads and branded content.',
    DIMENSION_AUDIENCE: 'To reach consumers whenever they need you, you have to organise all data sources to identify, understand and influence the most valuable audiences throughout the sales funnel.',
    DIMENSION_ACCESS: 'Once you are able to identify your audiences, you have to efficiently reach them and deliver your marketing messages across all inventory types and channels with the right levels of control.',
    DIMENSION_AUTOMATION: 'Tailored experiences typically require your marketing to use multiple data points, including your users’ context, the time of day or the device they’re using. Automation can help you to achieve relevance for users at scale. It enables you to optimise the execution of marketing operations, driving advertising effectiveness, profitability and growth.',
    DIMENSION_ORGANIZATION: 'Every marketing decision has goes through a process, is influenced by the way you work across teams and partners, and depends on support by people with specialised skills. So having an advanced data strategy, the right tech platforms and creative ideas only gets you so far: your organisation has to be set up to enable the right decisions to be made and executed.',
}

DIMENSION_LEVEL_DESCRIPTION = {
    DIMENSION_ATTRIBUTION: {
        LEVEL_0: 'You use a mix of measurement methodologies but results mostly only influence long-term planning. Evaluation of your marketing activities tends to be based on campaign metrics.',
        LEVEL_1: 'You use a variety of measurement methodologies as well as non-last-click attribution models. Results from regular A/B testing are used to inform campaign planning. Evaluation of your marketing activities tends to be based on conversion metrics.',
        LEVEL_2: 'You use a variety of measurement methodologies as well as a custom attribution model. Results from frequent A/B testing are used to optimise campaigns when they\'re running. Evaluation of your marketing activities tends to be based on business outcomes.',
        LEVEL_3: 'You use a variety of measurement methodologies as well as a data-driven attribution model. Results from frequent A/B testing are used for optimisation across campaigns when they\'re running. Evaluation of your marketing activities tends to be based on business outcomes.',
    },
    DIMENSION_ADS: {
        LEVEL_0: 'The user experience and speed of your website or app is at a basic level. Your creatives are the result of isolated processes and you tend to use the same message for all users. Creative testing happens infrequently or not at all.',
        LEVEL_1: 'You have tried user experience optimisation and personalisation of your website or app. Teams collaborate to build creatives but there\'s limited coordination across channels. You are using insights from analytics and results from A/B tests to improve creative effectiveness. Your messages are tailored to broad segments of your audience.',
        LEVEL_2: 'You are using advanced methods of user experience optimisation and personalisation of your website or app. Teams collaborate to build creatives, coordinated across digital channels. You are using several testing methodologies to improve creative effectiveness. Your messages are tailored to a variety of segments of your audience.',
        LEVEL_3: 'You are using cutting edge technology to create an impactful and tailored user experience across your websites and apps. Teams collaborate to build creatives, which are coordinated across digital and non-digital channels. You share results from several testing methodologies across digital and non-digital teams to improve creative effectiveness. Your messages are tailored to a variety of segments of your audience and influenced by contextual signals.',
    },
    DIMENSION_AUDIENCE: {
        LEVEL_0: 'You mostly use 3rd party data to target your campaigns, relying on broad audience definitions. You tend to focus on a specific part of the marketing funnel.',
        LEVEL_1: 'You use 3rd party and 1st party data to target your campaigns. You have segmented your audience, largely based on demographics and you cover several parts of the marketing funnel.',
        LEVEL_2: 'You use 3rd party and 1st party data to target your campaigns, covering the full marketing funnel. You have started to use insights captured in one channel in another channel. You have segmented your audience based on behavioural and interest data.',
        LEVEL_3: 'You use 3rd party and 1st party data – including offline data – to target your campaigns, covering the full marketing funnel. You are using insights captured in 1 channel in another channel and you have segmented your audience based on advanced analytics or machine learning.',
    },
    DIMENSION_ACCESS: {
        LEVEL_0: 'Your keyword lists are narrowly defined and most of your digital media buys are direct buys across a limited number of inventory sources and formats. You rely on platform default settings to ensure brand safety and ad viewability and to prevent ad fraud.',
        LEVEL_1: 'Your keyword lists cover your immediate products and most of your digital media buys are auction-based and direct buys across several inventory sources and formats. You rely on platform default settings and some manual adjustment to ensure brand safety and ad viewability and to prevent ad fraud.',
        LEVEL_2: 'Your keyword lists extend well beyond product-related terms and most of your digital media buys are auction-based and direct buys across a variety of inventory sources and formats. You invest resources in systems to ensure brand safety and ad viewability and to prevent ad fraud.',
        LEVEL_3: 'You use extensive and well-maintained keyword lists. Your media buys use a variety of deal types across many ad formats and inventory sources – including TV or OOH – and they are optimised across channels. You invest resources in systems to ensure brand safety and ad viewability and to prevent ad fraud. ',
    },
    DIMENSION_AUTOMATION: {
        LEVEL_0: 'You are planning, creating, monitoring and optimising most of your campaigns manually.',
        LEVEL_1: 'You are using selected automation features for planning, creating, monitoring and optimising some of your campaigns. This may include using ad servers or platform APIs.',
        LEVEL_2: 'You use automation features for planning, creating, monitoring and optimising across many of your campaigns. This may include using ad servers, platform APIs and dynamic data feeds.',
        LEVEL_3: 'Leveraging a variety of data signals, you make use of automation features for planning, creating, monitoring and optimising most or all of your campaigns. This may include the usage of ad servers, platform APIs and dynamic data feeds.',
    },
    DIMENSION_ORGANIZATION: {
        LEVEL_0: 'Your business is held back from siloed teams, with agencies working at arm\'s length. You have no fully dedicated resources, and no resources at all for certain marketing specialisms. ',
        LEVEL_1: 'Some of your key business functions work together towards clear objectives, including some of your agency partners. ',
        LEVEL_2: 'You have cross-functional teams with common objectives across all digital channels. Most or all agency partners collaborate with each other.',
        LEVEL_3: 'You have cross-functional teams with common objectives across all digital and non-digital channels. All agency and other partners collaborate with each other, some as virtual teams. Your teams are agile and share best practices. ',
    },
}

DIMENSION_LEVEL_RECOMMENDATIONS = {
    DIMENSION_ATTRIBUTION: {
        LEVEL_0: [{
            'header': 'Measure the true value of your marketing activities',
            'text': 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
        }, {
            'header': 'Capture marketing performance data comprehensively',
            'text': 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
        }, {
            'header': 'Expand your measurement capabilities',
            'text': 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
        }, {
            'header': 'Build your teams\' skills in web analytics',
            'text': 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
            'cta': {
                'text': 'Analytics Academy',
                'link': 'https://analytics.google.com/analytics/academy/',
                'class': 'analytics',
            },
        }],
        LEVEL_1: [{
            'header': 'Measure the true value of your marketing activities',
            'text': 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
        }, {
            'header': 'Capture marketing performance data comprehensively',
            'text': 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
        }, {
            'header': 'Expand your measurement capabilities',
            'text': 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
        }, {
            'header': 'Build your teams\' skills in web analytics',
            'text': 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
            'cta': {
                'text': 'Analytics Academy',
                'link': 'https://analytics.google.com/analytics/academy/',
                'class': 'analytics',
            },
        }],
        LEVEL_2: [{
            'header': 'Measure the true value of your marketing activities',
            'text': 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
        }, {
            'header': 'Capture marketing performance data comprehensively',
            'text': 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
        }, {
            'header': 'Expand your measurement capabilities',
            'text': 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
        }, {
            'header': 'Build your teams\' skills in web analytics',
            'text': 'Ask relevant people to take the advanced courses of the Analytics Academy.',
            'cta': {
                'text': 'Analytics Academy',
                'link': 'https://analytics.google.com/analytics/academy/',
                'class': 'analytics',
            },
        }],
        LEVEL_3: [{
            'header': 'Measure the true value of your marketing activities',
            'text': 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
        }, {
            'header': 'Capture marketing performance data comprehensively',
            'text': 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
        }, {
            'header': 'Expand your measurement capabilities',
            'text': 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
        }, {
            'header': 'Build your teams\' skills in web analytics',
            'text': 'Ask relevant people to take the advanced courses of the Analytics Academy.',
            'cta': {
                'text': 'Analytics Academy',
                'link': 'https://analytics.google.com/analytics/academy/',
                'class': 'analytics',
            },
        }],
    },
    DIMENSION_ADS: {
        LEVEL_0: [{
            'header': 'Make ads more relevant for different types of users',
            'text': 'Segment your users into different audiences, for example, new users and existing customers. Create ads that align with their respective expectations.',
        }, {
            'header': 'Tailor the user experience of your assets',
            'text': 'Tailor your website or app to the expectations of different audiences, for example, existing customer may benefit from more specific information whereas new users may need a broader picture.',
        }, {
            'header': 'Start using technology',
            'text': 'Use web analytics tools and A/B testing tools to continually improve the performance of your assets.',
        }, {
            'header': 'Improve the speed of your mobile assets',
            'text': 'Take the mobile speed test and get recommendations to implement right away.',
            'cta': {
                'text': 'Mobile speed test',
                'link': 'https://testmysite.withgoogle.com/',
                'class': 'speed-test',
            },
        }, {
            'header': 'Remove friction from the user experience of your mobile assets',
            'text': 'Consider these best practices and implement them.',
            'cta': {
                'text': 'Mobile UX best practices',
                'link': 'https://developers.google.com/web/fundamentals/design-and-ux/principles/',
                'class': 'ux-bp',
            },
        }, {
            'header': 'Connect different teams of your company',
            'text': 'Foster collaboration between different marketing teams that are responsible for creating your creatives, for example, digital and non-digital teams, media and creative teams. Encourage them to work together and share best practices.',
        }],
        LEVEL_1: [{
            'header': 'Improve the relevance of your ads for different types of users',
            'text': 'Refine the segmentation of your users into different audiences and create ads that match their characteristics.',
        }, {
            'header': 'Tailor the user experience of your assets',
            'text': 'Expand tailoring your website beyond basic personalisation, for example, create tailored experiences for more of your audience segments or use real-time predictive modelling to suggest products.',
        }, {
            'header': 'Expand your creative testing capabilities',
            'text': 'Add more methods such as multivariate tests or consumer surveys to your testing suite.',
        }, {
            'header': 'Improve the speed of your mobile assets',
            'text': 'Take the mobile speed test and get recommendations to implement right away.',
            'cta': {
                'text': 'Mobile speed test',
                'link': 'https://testmysite.withgoogle.com/',
                'class': 'speed-test',
            },
        }, {
            'header': 'Remove friction from the user experience of your mobile assets',
            'text': 'Consider these best practices and implement those where you still have gaps.',
            'cta': {
                'text': 'Mobile UX best practices',
                'link': 'https://developers.google.com/web/fundamentals/design-and-ux/principles/',
                'class': 'ux-bp',
            },
        }, {
            'header': 'Improve collaboration of teams that are responsible for creatives',
            'text': 'Consider establishing timelines that are shared between media and creative teams. Explore using the same toolset, for example, for managing creative projects. Encourage best practice sharing across these teams.',
        }],
        LEVEL_2: [{
            'header': 'Improve the relevance of your ads for different types of users',
            'text': 'Use additional data signals such as time of day or user location in your audience segmentation to create ads that are even more relevant.',
        }, {
            'header': 'Tailor the user experience of your assets',
            'text': 'Expand tailoring your website to include data signals from internal systems like your CRM or loyalty programme.',
        }, {
            'header': 'Maximise the impact of your creative tests',
            'text': 'Share the results of your tests widely, for example with non-digital teams. Establish a feedback loop so all teams can learn from each other.',
        }, {
            'header': 'Improve the speed of your mobile assets',
            'text': 'Take the mobile speed test and get recommendations to implement right away.',
            'cta': {
                'text': 'Mobile speed test',
                'link': 'https://testmysite.withgoogle.com/',
                'class': 'speed-test',
            },
        }, {
            'header': 'Remove friction from the entire user experience',
            'text': 'Consider these best practices and implement those where you still have gaps. Use current mobile techniques such as progressive web apps or single sign-on. Create links between your mobile assets and non-digital touchpoints, like stores or call centres.',
            'cta': {
                'text': 'Mobile UX best practices',
                'link': 'https://developers.google.com/web/fundamentals/design-and-ux/principles/',
                'class': 'ux-bp',
            },
        }, {
            'header': 'Improve collaboration of teams that are responsible for creatives',
            'text': 'Enable media and creative teams to work hand-in-hand and to use collaborative tools. Establish connections between digital and non-digital teams.',
        }],
        LEVEL_3: [{
            'header': 'Improve the relevance of your ads for different types of users',
            'text': 'Keep up to date with the latest research and industry best practices to find new ways of increasing the relevance of your ads.',
        }, {
            'header': 'Tailor the user experience of your assets',
            'text': 'Continue to invest in tailoring your website to the expectations of different audiences. Leverage new data signals as they become available, for example, from emerging device types or internal tools.as they become available',
        }, {
            'header': 'Maximise the impact of your creative tests',
            'text': 'Continue to share the results of your tests widely and build a robust data set of creative performance. Iterate feedback and sharing processes to ensure continued improvement off your creatives',
        }, {
            'header': 'Continue to invest in the speed of your mobile assets',
            'text': 'Every fraction of a second counts. Take the mobile speed test regularly to identify areas of improvement.',
            'cta': {
                'text': 'Mobile speed test',
                'link': 'https://testmysite.withgoogle.com/',
                'class': 'speed-test',
            },
        }, {
            'header': 'Review the entire user experience to identify friction points',
            'text': 'Keep up to date with emerging trends in UX and web technologies. Explore further possibilities to improve the user experience as people move between digital touchpoints and between digital and non-digital touchpoints.',
        }, {
            'header': 'Improve collaboration of teams that are responsible for creatives',
            'text': 'Connect teams who are responsible for your creatives with newly hired specialists or teams.',
        }],
    },
    DIMENSION_AUDIENCE: {
        LEVEL_0: [{
            'header': 'Use more signals to reach your audience',
            'text': 'In addition to 3rd party data, use 1st party data (i.e. your own data) to decide which users you want to reach online. Segment users into different audiences and optimise this segmentation regularly.',
        }, {
            'header': 'Leverage insights across channels',
            'text': 'Share insights you gain in 1 channel, for example search, to improve how you reach your audience in another channel, for example email.',
        }, {
            'header': 'Find additional opportunities to reach users',
            'text': 'Cover all parts of the marketing funnel, starting from creating awareness, to building consideration, to driving purchases and, finally, repeat purchasing.',
        }, {
            'header': 'Invest in technology',
            'text': 'Build or buy tools that allow you to capture and analyse user insights, for example, a CRM or Data Management Platform.',
        }],
        LEVEL_1: [{
            'header': 'Use more signals to reach your audience',
            'text': 'In addition to 3rd party data, use 1st party data across different digital channels to decide which users you want to reach online. Use that data to create additional audience segments and update this segmentation while campaigns are running.',
        }, {
            'header': 'Leverage insights across digital and non-digital channels',
            'text': 'Share insights you gain in 1 channel, for example linear TV, to improve how you reach your audience in another channel, for example online video.',
        }, {
            'header': 'Find additional opportunities to reach users',
            'text': 'Cover all parts of the marketing funnel, starting from creating awareness, to building consideration, to driving purchases and, finally, repeat purchasing.as they become available.',
        }, {
            'header': 'Enhance segmentation capabilities',
            'text': 'Extend your proficiency in using tools that allow you to capture and analyse user insights, for example, a CRM system or Data Management Platform.',
        }],
        LEVEL_2: [{
            'header': 'Use more signals to reach your audience',
            'text': 'In addition to 3rd party data, use 1st party data across different digital and non-digital channels to build meaningful audience segments. Update these segments automatically, based on a set of rules that you actively maintain.',
        }, {
            'header': 'Leverage insights from the entire company',
            'text': 'Share insights you gain in 1 channel, for example linear TV, to improve how you reach your audience in another channel, for example online video. Consider feeding in other types of data, for example, sales data.',
        }, {
            'header': 'Enhance segmentation capabilities',
            'text': 'Extend your proficiency in using tools that allow you to capture and analyse user insights, for example a CRM system or Data Management Platform. Connect tools with each other. Leverage machine learning technology improve your audience segmentation.',
        }],
        LEVEL_3: [{
            'header': 'Update the types of signals you use to reach your audience',
            'text': 'Consider new signals as they become available to build your audience segments. Continue to update these segments based on the value they deliver to your business.',
        }, {
            'header': 'Leverage insights from the entire company',
            'text': 'Assess if insights from new marketing channels, device types, ad formats and business systems can be used to improve how you reach users.',
        }, {
            'header': 'Enhance segmentation capabilities',
            'text': 'Stay close to developments in the tool landscape and explore opportunities related to improving the actionability of insights. For example, check if insights gained in 1 tool, like your Data Management Platform, could be used in another tool, like the 1 where you build and run your campaigns. Leverage emerging machine learning technology to improve your audience segmentation.',
        }],
    },
    DIMENSION_ACCESS: {
        LEVEL_0: [{
            'header': 'Extend your reach and optimise performance',
            'text': 'Extend your keyword lists to capture relevant queries related to all your products and to your product category. Buy video and display media across desktop and mobile platforms, using direct buys or programmatic buying methods such as open auction or programmatic direct. Optimise your media buys.',
        }, {
            'header': 'Ensure quality control',
            'text': 'Monitor brand safety, viewability, ad quality and keyword performance in your campaigns. Start acting on the results, for example, by building negative keyword lists or adding websites to a blacklist.',
        }],
        LEVEL_1: [{
            'header': 'Extend your reach and optimise performance',
            'text': 'Extend your keyword lists to capture relevant queries related to all your products, your product category, your brand and other relevant areas. Buy a larger percentage of video and display media using programmatic buying methods, such as open auction or programmatic direct. Optimise performance across digital channels.',
        }, {
            'header': 'Ensure quality control',
            'text': 'Monitor brand safety, viewability, ad quality and keyword performance in your campaigns. Use the results to optimise your bidding strategy, your media buys and your budget allocation.',
        }, {
            'header': 'Increase the variety of ad formats',
            'text': 'Use specialised formats, such as shopping ads on search, native ads and mobile app formats.',
        }],
        LEVEL_2: [{
            'header': 'Extend your reach and optimise performance',
            'text': 'In addition to your extensive keyword list, use automated features that capture unpredictable demand, for example, search queries generated by current events. Increase the percentage of video and display media you buy programmatically and consider additional deal types such as preferred or guaranteed. Consider buying some of your non-digital media programmatically.',
        }, {
            'header': 'Ensure quality control',
            'text': 'Monitor brand safety, viewability, ad quality and keyword performance in your campaigns. Feed the results directly into your algorithms that optimise bidding, your media buys and your budget allocation. Actively engage with ecosystem partners to prevent future issues.',
        }, {
            'header': 'Increase the variety of ad formats',
            'text': 'Use digital TV and digital out-of-home formats.',
        }],
        LEVEL_3: [{
            'header': 'Extend your reach and optimise performance',
            'text': 'Establish processes and improve internal systems that help you to capture new demand. Evaluate emerging deal types or features that help you to maximise reach while generating impact on your bottom line. Optimise your media buys across digital and non-digital channels.',
        }, {
            'header': 'Ensure quality control',
            'text': 'Assess and iterate your tools and internal processes to monitor brand safety, viewability, ad quality and keyword performance. Continue to automate the usage of the results in your bidding, buying and optimisation algorithms. Actively engage with ecosystem partners and industry associations to share best practices and prevent future issues.',
        }, {
            'header': 'Increase the variety of ad formats',
            'text': 'Experiment with ad formats in channels that have just recently become accessible through digital buying methods, for example radio ads.',
        }],
    },
    DIMENSION_AUTOMATION: {
        LEVEL_0: [{
            'header': 'Leverage technology',
            'text': 'Use tools that make setting up and managing campaigns more efficient, for example, using an ad server for your creatives and a Demand SIde Platform (DSP) for your media buys. Check if the tools you are already using provide an API to reduce the number of manual tasks.',
        }, {
            'header': 'Automate high volume tasks',
            'text': 'Aim for fully automated, real-time bidding across platforms to make the most out of your ad spend. As a first step, move to automated bid adjustments for search and display campaigns. Gain experience with campaign management features that automatically select targeting criteria, such as the websites your ads appear on, how much you bid and the exact makeup of your creatives (for example by testing several headlines).',
        }, {
            'header': 'Automate asset optimisation',
            'text': 'Use dynamic feeds to test variations of your creative assets, for example, ad copy that depends on a user\'s location or the user\'s keyword. Aim to automate at least half of your creative optimisation decisions.',
        }],
        LEVEL_1: [{
            'header': 'Leverage technology',
            'text': 'Expand your use of tools that make setting up and managing campaigns more efficient, for example use an ad server for an increased percentage of your ads, use your Demand Side Platform (DSP) for more of your media buys and increase your use of media platform APIs.',
        }, {
            'header': 'Automate high volume tasks',
            'text': 'Aim for fully automated, real-time bidding across platforms to make the most out of your ad spend. As a next step, add more signals to your automated bid adjustments across search and display campaigns. Expand your use of automated campaign features that automatically select targeting criteria, such as the websites your ads appear on, how much you bid and the exact makeup of your creatives (for example by testing several headlines).',
        }, {
            'header': 'Automate asset optimisation',
            'text': 'Use dynamic feeds and behavioural signals to automatically find the best-performing variation of your creative. Automate the optimisation of your creatives across several digital channels.',
        }],
        LEVEL_2: [{
            'header': 'Leverage technology',
            'text': 'Expand your use of tools that make setting up and managing campaigns more efficient, for example use an ad server beyond static creatives, use your Demand Side Platform (DSP) for more of your media buys and increase your use of platform APIs to include setup, maintenance, reporting and optimisation.',
        }, {
            'header': 'Automate high volume tasks',
            'text': 'Move to fully automated bidding which considers a variety of signals, including cross-device behaviour and insights from data-driven attribution models. Continue to explore new features that can automate targeting decisions.',
        }, {
            'header': 'Automate assets that have many variables',
            'text': 'Use dynamic feeds, behavioural signals from your website as well as cross-channel behavioural signals to automatically find the best-performing variation of your creative. Aim for a high percentage of automated creative optimisation.',
        }],
        LEVEL_3: [{
            'header': 'Stay on top of new technology',
            'text': 'Stay close to new platform features that make setting up and managing campaigns more efficient, for example, start buying media on new channels or platforms to go through your Demand Side Platform (DSP) as soon as it\'s feasible. Leverage new features of platform APIs to automate more tasks in campaign setup, maintenance, reporting and optimisation.',
        }, {
            'header': 'Automate high volume tasks',
            'text': 'Actively look for repetitive tasks that could be automated and identify tasks that are already automated but may benefit from more data inputs, for example, if your bids are already being set automatically, integrate additional relevant data signals as they become available.',
        }, {
            'header': 'Automate assets that have many variables',
            'text': 'Pay attention to new data signals that may help to improve the algorithms in your creative optimisation technology. Aim for a high percentage of automated creative optimisation.',
        }],
    },
    DIMENSION_ORGANIZATION: {
        LEVEL_0: [{
            'header': 'Devote specialist resources to digital marketing',
            'text': 'Hire people who specialise in a specific channel, in data science and measurement technologies. Make sure these people can spend enough or even all their time on digital marketing.',
        }, {
            'header': 'Increase coordination and collaboration',
            'text': 'Identify a senior sponsor who champions data-driven marketing, for example a VP of marketing. Coordinate and agree on marketing objectives across several digital channels. Enable collaboration between functional teams, starting with large campaign launches. Consider creating roles that are responsible for more than 1 digital marketing channel.',
        }, {
            'header': 'Improve partner management and ways of working',
            'text': 'Foster collaboration between different agencies. Increase your ability to work in agile ways, for example, devote budget to running experiments and encourage best practice sharing across functions or departments.',
        }],
        LEVEL_1: [{
            'header': 'Expand specialist resources',
            'text': 'Increase the number of specialists for specific digital marketing channels, for data science and for measurement technologies.',
        }, {
            'header': 'Increase coordination and collaboration',
            'text': 'Investigate if data-driven marketing could be sponsored by a more senior person, for example the CMO. Coordinate and agree on marketing objectives across all digital channels. Set up processes that allow day-to-day collaboration across teams, functions and between your organisation and your most important partners.',
        }, {
            'header': 'Improve partner management and ways of working',
            'text': 'Improve collaboration between different agencies and establish regular touchpoints. Increase your ability to work in agile ways, for example, devote more budget to running experiments and encourage best practice sharing across functions, brands, departments and regions.',
        }],
        LEVEL_2: [{
            'header': 'Expand specialist resources',
            'text': 'Increase the number of specialists for specific digital marketing channels, for data science and measurement technologies. ',
        }, {
            'header': 'Increase coordination and collaboration',
            'text': 'Investigate if data-driven marketing could be sponsored by a more senior person, for example by the CEO. Coordinate and agree on marketing objectives across digital and non-digital channels. Link your marketing objectives to business results. Improve processes that enable day-to-day collaboration across teams, functions and between your organisation and all relevant ecosystem partners.',
        }, {
            'header': 'Improve partner management and ways of working',
            'text': 'Improve collaboration between all relevant agencies and from virtual campaign teams. Increase your ability to work in agile ways, for example, devote more budget to running experiments and refine processes around best practice sharing across functions, brands, departments and regions.',
        }],
        LEVEL_3: [{
            'header': 'Expand specialist resources',
            'text': 'Increase the number of specialists for specific digital marketing channels, for data science, measurement technologies and emerging fields of specialisms.',
        }, {
            'header': 'Fine-tune coordination and collaboration',
            'text': 'Continue to iterate on how you coordinate and agree on marketing objectives across digital and non-digital channels. Find new links between marketing objectives and business performance. Improve processes that enable day-to-day collaboration across teams, functions and between your organisation and all relevant ecosystem partners.',
        }, {
            'header': 'Improve partner management and ways of working',
            'text': 'Regularly evaluate collaboration between all relevant agencies and help them to be more impactful and efficient. Continue to review your ability to work in agile ways, for example evaluate how you allocate budget to running experiments and refine processes around best practice sharing across functions, brands, departments and regions.',
        }],
    },
}

CONTENT_DATA = {
    'levels': LEVELS,
    'level_descriptions': LEVELS_DESCRIPTIONS,
    'report_level_descriptions': None,
    'dimensions': DIMENSION_TITLES.keys(),
    'dimension_labels': DIMENSION_TITLES,
    'dimension_headers_descriptions': DIMENSION_HEADER_DESCRIPTION,
    'dimension_level_description': DIMENSION_LEVEL_DESCRIPTION,
    'dimension_level_recommendations': DIMENSION_LEVEL_RECOMMENDATIONS,
}
