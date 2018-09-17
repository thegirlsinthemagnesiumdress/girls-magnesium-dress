/* eslint-disable max-len */

goog.module('dmb.components.dimensionTab.strings');

const dimensionHeaders = {
  attribution: 'Attribution',
  ads: 'Assets and ads',
  audience: 'Audience',
  access: 'Access',
  automation: 'Automation',
  organization: 'Organization',
};

const dimensionHeadersDescription = {
  attribution: 'Great attribution means accurately measuring and ascribing value to all consumer touch-points, so you make informed investment decisions and create even better, even more impactful experiences.',
  ads: 'Reaching consumers is not enough. They demand assistive experiences – fast, frictionless and tailored to their specific needs. You need to deliver intuitive and effective experiences across all brand digital touchpoints, including your website, your app, ads and branded content.',
  audience: 'To reach consumers whenever they need you, you have to organise all data sources to identify, understand and influence the most valuable audiences throughout the sales funnel.',
  access: 'Once you are able to identify your audiences, you have to efficiently reach them and deliver your marketing messages across all inventory types and channels with the right levels of control.',
  automation: 'Tailored experiences typically require your marketing to use multiple data points, including your users’ context, the time of day or the device they’re using. Automation can help you to achieve relevance for users at scale. It enables you to optimise the execution of marketing operations, driving advertising effectiveness, profitability and growth.',
  organization: 'Every marketing decision has goes through a process, is influenced by the way you work across teams and partners, and depends on support by people with specialised skills. So having an advanced data strategy, the right tech platforms and creative ideas only gets you so far: your organisation has to be set up to enable the right decisions to be made and executed.',
};


const dimensionLevelDescription = {
  attribution: {
    0: 'You use a mix of measurement methodologies but results mostly only influence long-term planning. Evaluation of your marketing activities tends to be based on campaign metrics.',
    1: 'You use a variety of measurement methodologies as well as non-last-click attribution models. Results from regular A/B testing are used to inform campaign planning. Evaluation of your marketing activities tends to be based on conversion metrics.',
    2: 'You use a variety of measurement methodologies as well as a custom attribution model. Results from frequent A/B testing are used to optimise campaigns when they\'re running. Evaluation of your marketing activities tends to be based on business outcomes.',
    3: 'You use a variety of measurement methodologies as well as a data-driven attribution model. Results from frequent A/B testing are used for optimisation across campaigns when they\'re running. Evaluation of your marketing activities tends to be based on business outcomes.',
  },
  ads: {
    0: 'The user experience and speed of your website or app is at a basic level. Your creatives are the result of isolated processes and you tend to use the same message for all users. Creative testing happens infrequently or not at all.',
    1: 'You have tried user experience optimisation and personalisation of your website or app. Teams collaborate to build creatives but there\'s limited coordination across channels. You are using insights from analytics and results from A/B tests to improve creative effectiveness. Your messages are tailored to broad segments of your audience.',
    2: 'You are using advanced methods of user experience optimisation and personalisation of your website or app. Teams collaborate to build creatives, coordinated across digital channels. You are using several testing methodologies to improve creative effectiveness. Your messages are tailored to a variety of segments of your audience.',
    3: 'You are using cutting edge technology to create an impactful and tailored user experience across your websites and apps. Teams collaborate to build creatives, which are coordinated across digital and non-digital channels. You share results from several testing methodologies across digital and non-digital teams to improve creative effectiveness. Your messages are tailored to a variety of segments of your audience and influenced by contextual signals.'
  },
  audience: {
    0: 'You mostly use 3rd party data to target your campaigns, relying on broad audience definitions. You tend to focus on a specific part of the marketing funnel.',
    1: 'You use 3rd party and 1st party data to target your campaigns. You have segmented your audience, largely based on demographics and you cover several parts of the marketing funnel.',
    2: 'You use 3rd party and 1st party data to target your campaigns, covering the full marketing funnel. You have started to use insights captured in one channel in another channel. You have segmented your audience based on behavioural and interest data.',
    3: 'You use 3rd party and 1st party data – including offline data – to target your campaigns, covering the full marketing funnel. You are using insights captured in 1 channel in another channel and you have segmented your audience based on advanced analytics or machine learning.',
  },
  access: {
    0: 'Your keyword lists are narrowly defined and most of your digital media buys are direct buys across a limited number of inventory sources and formats. You rely on platform default settings to ensure brand safety and ad viewability and to prevent ad fraud.',
    1: 'Your keyword lists cover your immediate products and most of your digital media buys are auction-based and direct buys across several inventory sources and formats. You rely on platform default settings and some manual adjustment to ensure brand safety and ad viewability and to prevent ad fraud.',
    2: 'Your keyword lists extend well beyond product-related terms and most of your digital media buys are auction-based and direct buys across a variety of inventory sources and formats. You invest resources in systems to ensure brand safety and ad viewability and to prevent ad fraud.',
    3: 'You use extensive and well-maintained keyword lists. Your media buys use a variety of deal types across many ad formats and inventory sources – including TV or OOH – and they are optimised across channels. You invest resources in systems to ensure brand safety and ad viewability and to prevent ad fraud. ',
  },
  automation: {
    0: 'You are planning, creating, monitoring and optimising most of your campaigns manually.',
    1: 'You are using selected automation features for planning, creating, monitoring and optimising some of your campaigns. This may include using ad servers or platform APIs.',
    2: 'You use automation features for planning, creating, monitoring and optimising across many of your campaigns. This may include using ad servers, platform APIs and dynamic data feeds.',
    3: 'Leveraging a variety of data signals, you make use of automation features for planning, creating, monitoring and optimising most or all of your campaigns. This may include the usage of ad servers, platform APIs and dynamic data feeds.',
  },
  organization: {
    0: 'Your business is held back from siloed teams, with agencies working at arm\'s length. You have no fully dedicated resources, and no resources at all for certain marketing specialisms. ',
    1: 'Some of your key business functions work together towards clear objectives, including some of your agency partners. ',
    2: 'You have cross-functional teams with common objectives across all digital channels. Most or all agency partners collaborate with each other.',
    3: 'You have cross-functional teams with common objectives across all digital and non-digital channels. All agency and other partners collaborate with each other, some as virtual teams. Your teams are agile and share best practices. ',
  },
};

const dimensionLevelRecomendations = {
  attribution: {
    0: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
    }],
    1: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
    }],
    2: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
    3: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
  },
  ads: {
    0: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
    }],
    1: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
    }],
    2: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
    3: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
  },
  audience: {
    0: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
    }],
    1: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
    }],
    2: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
    3: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
  },
  access: {
    0: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
    }],
    1: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
    }],
    2: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
    3: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
  },
  automation: {
    0: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
    }],
    1: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
    }],
    2: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
    3: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
  },
  organization: {
    0: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that is not based on the last click. Use metrics that show value beyond clicks or number of conversions, for example, revenue and visits in physical stores.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Make sure you have visibility into the performance of all your campaigns and assets. Assess performance across different digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Invest in tools for tagging and tracking and add more measurement methodologies to your suite of capabilities. Increase the frequency of tests and use the data to optimise campaigns.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and introductory courses of the Analytics Academy. ',
    }],
    1: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Move to an attribution model that fits your particular business. Use metrics that show value beyond revenue, for example, incremental revenue or profit.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance and establish a shared understanding of success metrics – across all device types and across all digital touchpoints.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the beginner and advanced courses of the Analytics Academy.',
    }],
    2: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Consider signals that are specific to your business in your data-driven attribution model. Use metrics that show value beyond revenue, for example, profit or lifetime value.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Create a single source of truth for marketing performance which considers behaviour in digital and non-digital channels.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Add measurement methodologies to your suite of capabilities to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. Increase the frequency of running tests and use the data to optimise campaigns in real-time.',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
    3: [{
      header: 'Measure the true value of your marketing activities',
      text: 'Continue to fine-tune your data-driven attribution model and leverage proprietary insights, data sources and machine learning capabilities. Determine the value of new user interactions, for example, a new feature in your app or added service provided in-store or through a call centre. Feed this value into your measurement models.',
    }, {
      header: 'Capture marketing performance data comprehensively',
      text: 'Add emerging campaign types or activities in new channels, such as a social media platform, to your single source of truth for marketing performance.',
    }, {
      header: 'Expand your measurement capabilities',
      text: 'Establish and iterate on a robust and shared process for your different measurement methodologies to optimise all aspects of digital marketing, including budget allocation, creative impact or the performance of individual channels. ',
    }, {
      header: 'Build your teams\' skills in web analytics',
      text: 'Ask relevant people to take the advanced courses of the Analytics Academy.',
    }],
  },
};


exports = {
  dimensionHeaders,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelRecomendations,
};
