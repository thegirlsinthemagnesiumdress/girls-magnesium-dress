/* eslint-disable max-len */

goog.module('dmb.components.dimensionTab.strings');

const dimensionHeaders = {
  'attribution': 'Attribution',
  'ads': 'Assets and ads',
  'audience': 'Audience',
  'access': 'Access',
  'automation': 'Automation',
  'organization': 'Organization',
};

const dimensionHeadersDescription = {
  'attribution': 'Great attribution means accurately measuring and ascribing value to all consumer touch-points, so you make informed investment decisions and create even better, even more impactful experiences.',
  'ads': 'Reaching consumers is not enough. They demand assistive experiences – fast, frictionless and tailored to their specific needs. You need to deliver intuitive and effective experiences across all brand digital touchpoints, including your website, your app, ads and branded content.',
  'audience': 'To reach consumers whenever they need you, you have to organise all data sources to identify, understand and influence the most valuable audiences throughout the sales funnel.',
  'access': 'Once you are able to identify your audiences, you have to efficiently reach them and deliver your marketing messages across all inventory types and channels with the right levels of control.',
  'automation': 'Tailored experiences typically require your marketing to use multiple data points, including your users’ context, the time of day or the device they’re using. Automation can help you to achieve relevance for users at scale. It enables you to optimise the execution of marketing operations, driving advertising effectiveness, profitability and growth.',
  'organization': 'Every marketing decision has goes through a process, is influenced by the way you work across teams and partners, and depends on support by people with specialised skills. So having an advanced data strategy, the right tech platforms and creative ideas only gets you so far: your organisation has to be set up to enable the right decisions to be made and executed.',
};


const dimensionLevelDescription = {
  'attribution': {
    0: 'You use a mix of measurement methodologies but results mostly only influence long-term planning. Evaluation of your marketing activities tends to be based on campaign metrics.',
    1: 'You use a variety of measurement methodologies as well as non-last-click attribution models. Results from regular A/B testing are used to inform campaign planning. Evaluation of your marketing activities tends to be based on conversion metrics.',
    2: 'You use a variety of measurement methodologies as well as a custom attribution model. Results from frequent A/B testing are used to optimise campaigns when they\'re running. Evaluation of your marketing activities tends to be based on business outcomes.',
    3: 'You use a variety of measurement methodologies as well as a data-driven attribution model. Results from frequent A/B testing are used for optimisation across campaigns when they\'re running. Evaluation of your marketing activities tends to be based on business outcomes.',
  },
  'ads': {
    0: 'The user experience and speed of your website or app is at a basic level. Your creatives are the result of isolated processes and you tend to use the same message for all users. Creative testing happens infrequently or not at all.',
    1: 'You have tried user experience optimisation and personalisation of your website or app. Teams collaborate to build creatives but there\'s limited coordination across channels. You are using insights from analytics and results from A/B tests to improve creative effectiveness. Your messages are tailored to broad segments of your audience.',
    2: 'You are using advanced methods of user experience optimisation and personalisation of your website or app. Teams collaborate to build creatives, coordinated across digital channels. You are using several testing methodologies to improve creative effectiveness. Your messages are tailored to a variety of segments of your audience.',
    3: 'You are using cutting edge technology to create an impactful and tailored user experience across your websites and apps. Teams collaborate to build creatives, which are coordinated across digital and non-digital channels. You share results from several testing methodologies across digital and non-digital teams to improve creative effectiveness. Your messages are tailored to a variety of segments of your audience and influenced by contextual signals.'
  },
  'audience': {
    0: 'You mostly use 3rd party data to target your campaigns, relying on broad audience definitions. You tend to focus on a specific part of the marketing funnel.',
    1: 'You use 3rd party and 1st party data to target your campaigns. You have segmented your audience, largely based on demographics and you cover several parts of the marketing funnel.',
    2: 'You use 3rd party and 1st party data to target your campaigns, covering the full marketing funnel. You have started to use insights captured in one channel in another channel. You have segmented your audience based on behavioural and interest data.',
    3: 'You use 3rd party and 1st party data – including offline data – to target your campaigns, covering the full marketing funnel. You are using insights captured in 1 channel in another channel and you have segmented your audience based on advanced analytics or machine learning.',
  },
  'access': {
    0: 'Your keyword lists are narrowly defined and most of your digital media buys are direct buys across a limited number of inventory sources and formats. You rely on platform default settings to ensure brand safety and ad viewability and to prevent ad fraud.',
    1: 'Your keyword lists cover your immediate products and most of your digital media buys are auction-based and direct buys across several inventory sources and formats. You rely on platform default settings and some manual adjustment to ensure brand safety and ad viewability and to prevent ad fraud.',
    2: 'Your keyword lists extend well beyond product-related terms and most of your digital media buys are auction-based and direct buys across a variety of inventory sources and formats. You invest resources in systems to ensure brand safety and ad viewability and to prevent ad fraud.',
    3: 'You use extensive and well-maintained keyword lists. Your media buys use a variety of deal types across many ad formats and inventory sources – including TV or OOH – and they are optimised across channels. You invest resources in systems to ensure brand safety and ad viewability and to prevent ad fraud. ',
  },
  'automation': {
    0: 'You are planning, creating, monitoring and optimising most of your campaigns manually.',
    1: 'You are using selected automation features for planning, creating, monitoring and optimising some of your campaigns. This may include using ad servers or platform APIs.',
    2: 'You use automation features for planning, creating, monitoring and optimising across many of your campaigns. This may include using ad servers, platform APIs and dynamic data feeds.',
    3: 'Leveraging a variety of data signals, you make use of automation features for planning, creating, monitoring and optimising most or all of your campaigns. This may include the usage of ad servers, platform APIs and dynamic data feeds.',
  },
  'organization': {
    0: 'Your business is held back from siloed teams, with agencies working at arm\'s length. You have no fully dedicated resources, and no resources at all for certain marketing specialisms. ',
    1: 'Some of your key business functions work together towards clear objectives, including some of your agency partners. ',
    2: 'You have cross-functional teams with common objectives across all digital channels. Most or all agency partners collaborate with each other.',
    3: 'You have cross-functional teams with common objectives across all digital and non-digital channels. All agency and other partners collaborate with each other, some as virtual teams. Your teams are agile and share best practices. ',
  },
};

const dimensionLevelRecomendations = {
  'attribution': {
    0: [{
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
    }],
    1: [{
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
    }],
    2: [{
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
    }],
    3: [{
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
    }],
  },
  'ads': {
    0: [{
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
    }, {
      'header': 'Remove friction from the user experience of your mobile assets',
      'text': 'Consider these best practices and implement them.',
    }, {
      'header': 'Connect different teams of your company',
      'text': 'Foster collaboration between different marketing teams that are responsible for creating your creatives, for example, digital and non-digital teams, media and creative teams. Encourage them to work together and share best practices.',
    }],
    1: [{
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
    }, {
      'header': 'Remove friction from the user experience of your mobile assets',
      'text': 'Consider these best practices and implement those where you still have gaps.',
    }, {
      'header': 'Improve collaboration of teams that are responsible for creatives',
      'text': 'Consider establishing timelines that are shared between media and creative teams. Explore using the same toolset, for example, for managing creative projects. Encourage best practice sharing across these teams.',
    }],
    2: [{
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
    }, {
      'header': 'Remove friction from the entire user experience',
      'text': 'Consider these best practices and implement those where you still have gaps. Use current mobile techniques such as progressive web apps or single sign-on. Create links between your mobile assets and non-digital touchpoints, like stores or call centres.',
    }, {
      'header': 'Improve collaboration of teams that are responsible for creatives',
      'text': 'Enable media and creative teams to work hand-in-hand and to use collaborative tools. Establish connections between digital and non-digital teams.',
    }],
    3: [{
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
    }, {
      'header': 'Review the entire user experience to identify friction points',
      'text': 'Keep up to date with emerging trends in UX and web technologies. Explore further possibilities to improve the user experience as people move between digital touchpoints and between digital and non-digital touchpoints.',
    }, {
      'header': 'Improve collaboration of teams that are responsible for creatives',
      'text': 'Connect teams who are responsible for your creatives with newly hired specialists or teams.',
    }],

  },
  'audience': {
    0: [{
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
    1: [{
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
    2: [{
      'header': 'Use more signals to reach your audience',
      'text': 'In addition to 3rd party data, use 1st party data across different digital and non-digital channels to build meaningful audience segments. Update these segments automatically, based on a set of rules that you actively maintain.',
    }, {
      'header': 'Leverage insights from the entire company',
      'text': 'Share insights you gain in 1 channel, for example linear TV, to improve how you reach your audience in another channel, for example online video. Consider feeding in other types of data, for example, sales data.',
    }, {
      'header': 'Enhance segmentation capabilities',
      'text': 'Extend your proficiency in using tools that allow you to capture and analyse user insights, for example a CRM system or Data Management Platform. Connect tools with each other. Leverage machine learning technology improve your audience segmentation.',
    }],
    3: [{
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
  'access': {
    0: [{
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
    }],
    1: [{
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
    }],
    2: [{
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
    }],
    3: [{
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
    }],
  },
  'automation': {
    0: [{
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
    }],
    1: [{
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
    }],
    2: [{
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
    }],
    3: [{
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
    }],
  },
  'organization': {
    0: [{
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
    }],
    1: [{
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
    }],
    2: [{
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
    }],
    3: [{
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
    }],
  },
};


exports = {
  dimensionHeaders,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelRecomendations,
};
