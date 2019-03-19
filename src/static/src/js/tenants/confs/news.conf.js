/* eslint-disable max-len */

goog.module('dmb.components.tenant.conf.news');

const levels = {
  0: 'Nascent',
  1: 'Developing',
  2: 'Mature',
  3: 'Leading',
};

const levelDescriptions = {
  0: 'Organizations at this stage have the basic tools, but they often face cultural challenges to truly embracing data-supported decision-making.',
  1: 'These organizations are able to drive value from data in some pockets of their business. Leadership recognises data as a priority, but is unclear on how to unlock the best returns.',
  2: 'Data-informed decision making is the standard across much of the business. While the technology and tools support various use cases, they are mostly on a project basis and not business as usual.',
  3: 'These organizations see data as an integral part of achieving their strategic objectives. They experiment with innovative, data-oriented projects and technologies that help drive the industry forward.',
};

const reportLevelDescriptions = {
  0: 'This is the most basic of the four levels of maturity. You have the basic tools, but often face cultural challenges to truly embracing data-supported decision-making.',
  1: 'This is the second of the four levels of maturity. You are able to drive value from data in some pockets of the business. Leadership recognises data as a priority, but is unclear on how to unlock the best returns.',
  2: 'This is the third of the four levels of maturity. Data-informed decision-making is the standard across much of your organization. While the technology and tools support various use cases, they are mostly on a project basis and not business as usual.',
  3: 'This is the most advanced of the four levels of maturity. These organizations see data as an integral part of achieving their strategic objectives. They experiment with innovative, data-oriented projects and technologies that help drive the industry forward.',
};

const dimensions = [
  'strategic_direction',
  'reader_engagement',
  'reader_revenue',
  'advertising_revenue',
];

const dimensionHeadersDescription = {
  'strategic_direction': 'Doing this well means that data is understood universally, it supports key business objectives, and there are robust data resources and technologies in place.',
  'reader_engagement': 'Reader engagement is crucial to acquiring and retaining readers and increasing share of attention. Without an engaged readership, a news company cannot secure the subscription and advertising opportunities it needs to survive and thrive.',
  'reader_revenue': 'News companies that successfully build valuable direct-to-consumer relationships with their readers not only see the near-term benefits of increased revenue but also reduce operating volatility through long-term, recurring revenue streams.',
  'advertising_revenue': 'Leading news companies know their readers better than anyone, and they create content to attract and retain those readers. They act as advisors in the creative and campaign development process to deliver high-impact, relevant advertising that does not diminish the reader experience.',
};


const dimensionLevelDescription = {
  'strategic_direction': {
    0: 'You have limited strategy in connecting data with your overarching business goals.',
    1: 'Leadership have provided an initial articulation of specific and well-defined data initiatives, but there is limited continued focus on this.',
    2: 'There is widespread knowledge and respect for the role data plays in achieving the overall business strategy.',
    3: 'There is universal understanding of how data underpins the overarching business strategy, at all levels.',
  },
  'reader_engagement': {
    0: 'You collect basic engagement data (i.e., page views), but do not translate it into audience insights. Content decisions are primarily based on instinct and editorial experience.',
    1: 'You know what the broad audience segments are and start to uncover discrete audience insights using basic web analytics tools. However, reader experience and content decisions are still driven by “gut instinct.”',
    2: 'You understand how different segments engage with content and use these insights to improve engagement. Meanwhile, the editorial team actively use engagement insights and data to improve content format (i.e., headlines, length).',
    3: 'You clearly understand the context of the full reader journey and why audiences engage. You tailor the reader experience for different segments and occasions. Meanwhile, editorial decisions are generally data-informed.',
  },
  'reader_revenue': {
    0: 'Your paid content offering is limited to one size fits all.',
    1: 'You use metrics to develop promotions or price tiers for paid content offerings. You understand conversion triggers such as registration, login, and subscription.',
    2: 'You use different products to improve the reader’s journey and determine how to bundle these products for different audiences. Your business is starting to explore using LTV-focused metrics and beginning to understand subscription and churn drivers.',
    3: 'You have differentiated products that are relevant to readers across their life cycles. The portfolio of products are mutually reinforcing and drive loyalty and LTV. You understand the needs and behaviors of readers at different stages in their life cycles.',
  },
  'advertising_revenue': {
    0: 'You have basic segments (demographics, location) in place for audience-based advertising.',
    1: 'You use combinations of pre-built segments to assemble campaigns for advertisers. Meanwhile, you use exchanges / PMPs in a reactive way, primarily to monetize remnant inventory.',
    2: 'You use different data sets to build interest and intent-based segments. You share insights and equip the sales team to clearly communicate the value of different segments to advertisers. You use exchanges / PMPs in a strategic way to optimize yield.',
    3: 'You build unique segments using enriched first party data that gets to the heart of reader interest & intent. You proactively collaborate with advertisers & agencies to craft campaigns that incorporate unique audience insights.',
  },
};

const dataFoundationsGuideCta = {
  'text': 'Data Activation Guide',
  'link': 'http://www2.deloitte.com/content/dam/Deloitte/us/Documents/technology-media-telecommunications/us-digital-transformation-through-data-for-news.pdf#page=7',
};

const activatingUseCasesGuideCta = {
  'text': 'Data Activation Guide',
  'link': 'http://www2.deloitte.com/content/dam/Deloitte/us/Documents/technology-media-telecommunications/us-digital-transformation-through-data-for-news.pdf#page=17',
};

const dimensionLevelRecommendations = {
  'strategic_direction': {
    0: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Articulate your broader organizational mission, and identify areas in which data may be able to support or drive efforts to meet the mission.',
      },
      {
        'header': 'Foster collaboration and cross-functional teamwork',
        'text': 'Identify opportunities to align data functions with the centers of influence in the organization.',
      },
      {
        'header': 'Embed data-informed decision making',
        'text': 'Institute systems to evaluate decisions based on empirical analysis. Reward evidence-based rationale for operational decision-making.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    1: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organization`s approach to handling and activating data. Encourage leadership at all levels to communicate this message to team members.',
      },
      {
        'header': 'Foster collaboration and cross-functional teamwork',
        'text': 'Establish educational sessions in which representatives from the data team provide information and training on key aspects of the data operation to team members throughout the organization.',
      },
      {
        'header': 'Embed data-informed decision making',
        'text': 'Provide access to tools that enable and encourage colleagues to analyze decision criteria and execute data-supported decisions.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    2: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organization`s approach to handling and activating data. Encourage leadership at all levels to communicate this message to team members.',
      },
      {
        'header': 'Foster collaboration and cross-functional teamwork',
        'text': 'Incorporate data strategy messaging in team meetings. Establish key performance indicators (KPIs) that drive collaboration across organizational silos and incentivise cross-functional performance.',
      },
      {
        'header': 'Democratize your data',
        'text': 'Create intuitive tools and portals that enable access to relevant audience data for all team members. Provide trainings and educational resources to team members and encourage use of available resources.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature publishers have a well-established data strategy but want to see what other publishers are doing. Start with the Data Foundations section of the Data Activation Guide to see how some Leading publishers have developed their cultural, skills-based, data-related, and technological foundations.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    3: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organization`s approach to handling and activating data. Encourage leadership at all levels to communicate this message to team members.',
      },
      {
        'header': 'Foster collaboration and cross-functional teamwork',
        'text': 'Continue regular cadence of cross-functional team meetings and craft incentives to encourage further collaboration across the organization.',
      },
      {
        'header': 'Attract the right talent',
        'text': 'Communicate the unique emphasis your organization places on being data-informed, and establish recruiting partnerships to maintain a strong pipeline of technical professionals.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading publishers have a well-established data strategy but want to see what other publishers are doing. Start with the Data Foundations section of the Data Activation Guide to see how other Leading publishers have developed their cultural, skills-based, data-related, and technological foundations.',
        'cta': dataFoundationsGuideCta,
      },
    ],
  },
  'reader_engagement': {
    0: [
      {
        'header': 'Measure it to improve it',
        'text': 'Drive collaboration amongst data teams and business leaders to prioritize data collection activities and measurement capabilities.',
      },
      {
        'header': 'Understand what makes your audience tick',
        'text': 'Develop basic segmentation processes that capture high-level interest-based or behavioral segments for analysis. Understand your different segments of readers and how they engage with your content and your platform.',
      },
      {
        'header': 'Connect data to your content',
        'text': 'Deploy a content tagging technology system and develop a common taxonomy to improve the searchability of your content library.',
      },
      {
        'header': 'Make the experience intuitive',
        'text': 'Build your team`s skills in web analytics to better understand and improve pain points in the reader journey.',
      },
      {
        'header': 'Unlock insights from your Google Analytics data',
        'text': 'Understand your different segments of readers and how they engage with your site',
        'cta': {
          'text': 'News Consumer Insights',
          'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
        },
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    1: [
      {
        'header': 'Measure it to improve it',
        'text': 'Identify organizational objectives and tie key performance metrics to those objectives.',
      },
      {
        'header': 'Understand what makes your audience tick',
        'text': 'Build technical teams to enhance segmentation practices and improve on foundational understandings of how audiences engage with your platform.',
      },
      {
        'header': 'Connect data to your content',
        'text': 'Deploy technology solutions to support cross-functional collaboration between data and editorial teams and help guide content decisions.',
      },
      {
        'header': 'Make the experience intuitive',
        'text': 'Capture and organize audience on-site behavioral data to inform user interface and design decisions.',
      },
      {
        'header': 'Unlock insights from your Google Analytics data',
        'text': 'Understand your different segments of readers and how they engage with your site.',
        'cta': {
          'text': 'News Consumer Insights',
          'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
        },
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    2: [
      {
        'header': 'Measure it to improve it',
        'text': 'Make analytics and reporting accessible to relevant team members, so everyone in the organization can understand the health and performance of the digital platform.',
      },
      {
        'header': 'Understand what makes your audience tick',
        'text': 'Build new audience segments and enhance reader profiles to better tailor content and user interface decisions to satisfy specific reader preferences.',
      },
      {
        'header': 'Organize your content for future opportunities',
        'text': 'Maintain your content catalog and provide intuitive tools to editorial teams to help surface insights that can inform content planning activities.',
      },
      {
        'header': 'Promote experimentation',
        'text': 'Use A/B and multivariate tests to frequently identify areas to improve user interface and content options for readers. Promote a culture of testing and learning to drive continual improvement.',
      },
      {
        'header': 'Unlock insights from your Google Analytics data',
        'text': 'Understand your different segments of readers and how they engage with your site.',
        'cta': {
          'text': 'News Consumer Insights',
          'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
        },
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature publishers have sophisticated approaches to improving overall reader engagement but want to see what other publishers are doing.The Activating Use Cases section of the Data Activation Guide details how some Leading publishers have approached improving overall reader engagement.',
        'cta': activatingUseCasesGuideCta,
      },
    ],
    3: [
      {
        'header': 'Measure it to improve it',
        'text': 'Continue to roll out analytics and reporting tools to support cross-functional and performance-based decision-making.',
      },
      {
        'header': 'Understand what makes your audience tick',
        'text': 'Enhance technological capabilities and data collection efforts to refine the understanding of specific audience segments and individual reader profiles. Continue to uncover insights that inform best ways to serve readers.',
      },
      {
        'header': 'Focus on optimizing the impact of your content',
        'text': 'Continue to integrate relevant audience insights and tools with the editorial and product teams to serve your readers what they want, while maintaining the integrity of your editorial mission.',
      },
      {
        'header': 'Unlock insights from your Google Analytics data',
        'text': 'Understand your different segments of readers and how they engage with your site.',
        'cta': {
          'text': 'News Consumer Insights',
          'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
        },
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading publishers have a sophisticated approach to improving overall reader engagement but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading publishers have approached improving overall reader engagement.',
        'cta': activatingUseCasesGuideCta,
      },
    ],
  },
  'reader_revenue': {
    0: [
      {
        'header': 'Understand the value of your readers',
        'text': 'Understand your different segments of readers and how they engage with your content and your platform. Implement simple plug-in tools to help you measure and visualize these reader segments and how much value they bring.',
        'cta': {
          'text': 'News Consumer Insights',
          'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
        },
      },
      {
        'header': 'Tailor your subscription approach',
        'text': 'Understand the needs and behaviors of your readers and collaborate cross-functionally to develop strategies to convert them into subscribers.',
      },
      {
        'header': 'Identify new revenue models',
        'text': 'Identify engaged segments of your audience and explore new offerings that they may want. These might be opportunities that you develop on your own, or you may need to seek partners to support.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    1: [
      {
        'header': 'Understand the value of your readers',
        'text': 'Start to layer in more behavioral data that tells you how readers behave online and how those behaviors can translate to publisher value. Use reader insights to identify new ways to increase reader value (i.e., tailored communications, recommendations, and subscription offers).',
      },
      {
        'header': 'Tailor your subscription approach',
        'text': 'Segment your readers based on their behavior and measure how effective your subscription promotions are with different reader types. Tailor how you communicate with them based on the feedback.',
      },
      {
        'header': 'Integrate your different revenue models',
        'text': 'Integrate your data across different product or service offerings to get an understanding of reader behavior across the whole businesses. Develop the capability to identify readers and structure opportunities to cross-sell.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    2: [
      {
        'header': 'Understand the value of your readers ',
        'text': 'Integrate a view of reader lifetime value (LTV) into core business decision-making. Ensure that core functions in the marketing, editorial, and product teams consider the impact on reader LTV when making key decisions.',
      },
      {
        'header': 'Tailor your subscription approach',
        'text': 'Employ sophisticated techniques (e.g., dynamic pricing) to tailor subscription offers and match them to specific segments based on their behavior on your platform. Create a feedback loop to analyze the results and understand points of improvement.',
      },
      {
        'header': 'Develop reinforcing revenue models',
        'text': 'Actively cross-promote different titles or businesses based on reader interests or characteristics. Start to understand the relative value of decisions to direct readers between sites and products.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature publishers have created significant revenue from increasing direct-paying reader relationships but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading publishers have approached increasing direct-paying reader relationships.',
        'cta': activatingUseCasesGuideCta,
      },
    ],
    3: [
      {
        'header': 'Understand the value of your readers',
        'text': 'Continue to refine the approach to quantifying reader lifetime value (LTV). Leverage reader LTV data to inform operational improvements and identify strategic growth opportunities.',
      },
      {
        'header': 'Tailor your subscription approach',
        'text': 'Continually improve the approach to converting and retaining subscribers based on updates to predictive models and subscription pricing strategies.',
      },
      {
        'header': 'Pursue attractive adjacent business opportunities',
        'text': 'Leverage your unique audience insights to identify and support strategic decisions to pursue opportunities that can generate new revenue for the business.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading publishers have a sophisticated approach to increasing direct-paying reader relationships but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading publishers have approached increasing direct-paying reader relationships.',
        'cta': activatingUseCasesGuideCta,
      },
    ],
  },
  'advertising_revenue': {
    0: [
      {
        'header': 'Measure it to improve it',
        'text': 'Identify organizational objectives and tie key performance metrics to those objectives.',
      },
      {
        'header': 'Understand what makes your audience tick',
        'text': 'Build technical teams to enhance segmentation practices and improve on foundational understandings of how audiences engage with your platform.',
      },
      {
        'header': 'Connect data to your content',
        'text': 'Deploy technology solutions to support cross-functional collaboration between data and editorial teams and help guide content decisions.',
      },
      {
        'header': 'Make the experience intuitive',
        'text': 'Capture and organize audience on-site behavioral data to inform user interface and design decisions.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    1: [
      {
        'header': 'Build and enhance the understanding of your audience ',
        'text': 'Start to layer in data that tells you how readers behave online and how this impacts the value they bring.  Build technical teams to enhance segmentation practices and improve on foundational understandings of how audiences engage with your platform.',
      },
      {
        'header': 'Connect the right audience to the right advertiser',
        'text': 'Collaborate with your advertisers to identify the audiences they want to reach.  Start incorporating advertiser input into audience segmentation practices.',
      },
      {
        'header': 'Know the value of your audience',
        'text': 'Monitor the performance of different audiences across your sales mix. Analyze and record insights across segments to develop a long-term understanding of audience segment performance.',
      },
      {
        'header': 'Make the most of your platform mix',
        'text': 'Review historical performance of advertising sales across channels to begin developing a successful sales mix strategy.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing publishers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataFoundationsGuideCta,
      },
    ],
    2: [
      {
        'header': 'Build and enhance the understanding of your audience ',
        'text': 'Integrate a view of reader lifetime value (LTV) into core business decision-making. Experiment to test the relative value and performance of audience segments to refine high demand segments. Develop systems to effectively price audience segments based on historical performance and perceived value.',
      },
      {
        'header': 'Connect the right audience to the right advertiser',
        'text': 'Continue to foster relationships with key advertisers, and collaborate to proactively identify ways to support their future advertising strategies.',
      },
      {
        'header': 'Bring campaigns to life',
        'text': 'Think about advertising holistically and drive value through the strategic combination of relevant context, creative, advertising placement, and advertising format.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature publishers generate significant revenue through advertising but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading publishers have approached driving revenue from advertisers.',
        'cta': activatingUseCasesGuideCta,
      },
    ],
    3: [
      {
        'header': 'Build and enhance the understanding of your audience ',
        'text': 'Integrate a view of reader lifetime value (LTV) into core business decision-making. Experiment to test the relative value and performance of audience segments to refine high demand segments. Develop systems to effectively price audience segments based on historical performance and perceived value.',
      },
      {
        'header': 'Connect the right audience to the right advertiser',
        'text': 'Continue to foster relationships with key advertisers, and collaborate to proactively identify ways to support their future advertising strategies through the strategic combination of relevant context, creative, advertising placement, and advertising format.',
      },
      {
        'header': 'Use technology to scale ',
        'text': 'Enhance technological capabilities, including focusing on direct programmatic, to effectively serve advertisers at scale without sacrificing quality of content or reader experience.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading publishers have a sophisticated approach to driving revenue from advertisers but want to see what other publishers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading publishers have approached driving revenue from advertisers.',
        'cta': activatingUseCasesGuideCta,
      },
    ],
  },
};


const conf = {
  levels,
  levelDescriptions,
  reportLevelDescriptions,
  dimensions,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelRecommendations,
};


exports = conf;
