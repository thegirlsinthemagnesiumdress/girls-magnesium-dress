/* eslint-disable max-len */

goog.module('dmb.components.tenant.conf.news');

const levels = {
  0: 'Nascent',
  1: 'Developing',
  2: 'Mature',
  3: 'Leading',
};


const dimensionHeaders = {
  'strategic-direction': 'Strategic direction and data foundations',
  'reader-engagement': 'Reader engagement',
  'reader-revenue': 'Reader revenue',
  'ad-revenue': 'Advertising revenue',
};

const dimensionHeadersDescription = {
  'strategic-direction': 'Doing this well means that data is understood universally, it supports key business objectives, and there are robust data resources and technologies in place.',
  'reader-engagement': 'Reader engagement is crucial to acquiring and retaining readers and increasing share of attention. Without an engaged readership, a news company cannot secure the subscription and advertising opportunities it needs to survive and thrive.',
  'reader-revenue': 'News companies that successfully build valuable direct-to-consumer relationships with their readers not only see the near-term benefits of increased revenue but also reduce operating volatility through long-term, recurring revenue streams.',
  'ad-revenue': 'Leading news companies know their readers better than anyone, and they create content to attract and retain those readers. They act as advisors in the creative and campaign development process to deliver high-impact, relevant advertising that does not diminish the reader experience.',
};


const dimensionLevelDescription = {
  'strategic-direction': {
    0: 'You have limited strategy in connecting data with your overarching business goals.',
    1: 'Leadership have provided an initial articulation of specific and well-defined data initiatives, but there is limited continued focus on this.',
    2: 'There is widespread knowledge and respect for the role data plays in achieving the overall business strategy.',
    3: 'There is universal understanding of how data underpins the overarching business strategy, at all levels.',
  },
  'reader-engagement': {
    0: 'You collect basic engagement data (i.e., page views), but do not translate it into audience insights. Content decisions are primarily based on instinct and editorial experience.',
    1: 'You know what the broad audience segments are and start to uncover discrete audience insights using basic web analytics tools. However, reader experience and content decisions are still driven by “gut instinct.”',
    2: 'You understand how different segments engage with content and use these insights to improve engagement. Meanwhile, the editorial team actively use engagement insights and data to improve content format (i.e., headlines, length).',
    3: 'You clearly understand the context of the full reader journey and why audiences engage. You tailor the reader experience for different segments and occasions. Meanwhile, editorial decisions are generally data-informed.',
  },
  'reader-revenue': {
    0: 'Your paid content offering is limited to one size fits all.',
    1: 'You use metrics to develop promotions or price tiers for paid content offerings. You understand conversion triggers such as registration, login, and subscription.',
    2: 'You use different products to improve the reader’s journey and determine how to bundle these products for different audiences. Your business is starting to explore using LTV-focused metrics and beginning to understand subscription and churn drivers.',
    3: 'You have differentiated products that are relevant to readers across their life cycles. The portfolio of products are mutually reinforcing and drive loyalty and LTV. You understand the needs and behaviors of readers at different stages in their life cycles.',
  },
  'ad-revenue': {
    0: 'You have basic segments (demographics, location) in place for audience-based advertising.',
    1: 'You use combinations of pre-built segments to assemble campaigns for advertisers. Meanwhile, you use exchanges / PMPs in a reactive way, primarily to monetize remnant inventory.',
    2: 'You use different data sets to build interest and intent-based segments. You share insights and equip the sales team to clearly communicate the value of different segments to advertisers. You use exchanges / PMPs in a strategic way to optimize yield.',
    3: 'You build unique segments using enriched first party data that gets to the heart of reader interest & intent. You proactively collaborate with advertisers & agencies to craft campaigns that incorporate unique audience insights.',
  },
};

const dimensionLevelRecommendations = {
  'strategic-direction': {
    0: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Articulate your broader organisational mission, and identify areas in which data may be able to support or drive efforts to meet the mission.',
      },
      {
        'header': 'Foster collaboration and cross-functional teamwork',
        'text': 'Identify opportunities to align data functions with the centers of influence in the organisation.',
      },
      {
        'header': 'Embed data-informed decision making',
        'text': 'Institute systems to evaluate decisions based on empirical analysis.  Reward evidence-based rationale for operational decision-making.',
      },
    ],
    1: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organisation’s approach to handling and activating data.Encourage leadership at all levels to communicate this message to team members.',
      },
      {
        'header': 'Capture marketing performance data comprehensively',
        'text': 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
      },
      {
        'header': 'Expand your measurement capabilities',
        'text': 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
      },
      {
        'header': 'Build your teams\' skills in web analytics',
        'text': 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
        'cta': {
          'text': 'Analytics Academy',
          'link': 'https://analytics.google.com/analytics/academy/',
          'class': 'analytics',
        },
      },
    ],
    2: [
      {
        'header': 'Measure the true value of your marketing activities',
        'text': 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
      },
      {
        'header': 'Capture marketing performance data comprehensively',
        'text': 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
      },
      {
        'header': 'Expand your measurement capabilities',
        'text': 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
      },
      {
        'header': 'Build your teams\' skills in web analytics',
        'text': 'Ask relevant people to take the advanced courses of the Analytics Academy.',
        'cta': {
          'text': 'Analytics Academy',
          'link': 'https://analytics.google.com/analytics/academy/',
          'class': 'analytics',
        },
      },
    ],
    3: [
      {
        'header': 'Measure the true value of your marketing activities',
        'text': 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
      },
      {
        'header': 'Capture marketing performance data comprehensively',
        'text': 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
      },
      {
        'header': 'Expand your measurement capabilities',
        'text': 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
      },
      {
        'header': 'Build your teams\' skills in web analytics',
        'text': 'Ask relevant people to take the advanced courses of the Analytics Academy.',
        'cta': {
          'text': 'Analytics Academy',
          'link': 'https://analytics.google.com/analytics/academy/',
          'class': 'analytics',
        },
      },
    ],
  },
  'reader-engagement': {
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
  'reader-revenue': {
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
  'ad-revenue': {
    0: [{
      'header': 'Extend your reach and optimise performance',
      'text': 'Extend your keyword lists to capture relevant queries related to all your products and to your product category. Buy video and display media across desktop and mobile platforms, using direct buys or programmatic buying methods such as open auction or programmatic direct. Optimise your media buys.',
    }, {
      'header': 'Ensure quality control',
      'text': 'Monitor brand safety, viewability, ad quality and keyword performance in your campaigns. Start acting on the results, for example, by building negative keyword lists or adding websites to a blacklist.',
    }],
    1: [{
      'header': 'Extend your reach and optimise performance',
      'text': 'Extend your keyword lists to capture relevant queries related to all your products, your product category, your brand and other relevant areas. Buy a larger percentage of video and display media using programmatic buying methods, such as open auction or programmatic direct. Optimise performance across digital channels.',
    }, {
      'header': 'Ensure quality control',
      'text': 'Monitor brand safety, viewability, ad quality and keyword performance in your campaigns. Use the results to optimise your bidding strategy, your media buys and your budget allocation.',
    }, {
      'header': 'Increase the variety of ad formats',
      'text': 'Use specialised formats, such as shopping ads on search, native ads and mobile app formats.',
    }],
    2: [{
      'header': 'Extend your reach and optimise performance',
      'text': 'In addition to your extensive keyword list, use automated features that capture unpredictable demand, for example, search queries generated by current events. Increase the percentage of video and display media you buy programmatically and consider additional deal types such as preferred or guaranteed. Consider buying some of your non-digital media programmatically.',
    }, {
      'header': 'Ensure quality control',
      'text': 'Monitor brand safety, viewability, ad quality and keyword performance in your campaigns. Feed the results directly into your algorithms that optimise bidding, your media buys and your budget allocation. Actively engage with ecosystem partners to prevent future issues.',
    }, {
      'header': 'Increase the variety of ad formats',
      'text': 'Use digital TV and digital out-of-home formats.',
    }],
    3: [{
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
};


const conf = {
  levels,
  dimensionHeaders,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelRecommendations,
};


exports = conf;
