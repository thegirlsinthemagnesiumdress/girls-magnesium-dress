/* eslint-disable max-len */

goog.module('dmb.components.tenant.conf.retail');

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
  1: 'This is the second of the four levels of maturity. You are able to drive value from data in some pockets of the business. Leadership recognizes data as a priority, but is unclear on how to unlock the best returns.',
  2: 'This is the third of the four levels of maturity. Data-informed decision-making is the standard across much of your organization. While the technology and tools support various use cases, they are mostly on a project basis and not business as usual.',
  3: 'This is the most advanced of the four levels of maturity. These organizations see data as an integral part of achieving their strategic objectives. They experiment with innovative, data-oriented projects and technologies that help drive the industry forward.',
};

const industryAvgDescription = 'How retailers perform on average; dynamically calculated based on the results of those who have completed this survey.';

const industryBestDescription = 'This is the highest recorded score from a participant who has taken this data maturity survey.';

const dimensions = [
  'strategic_direction',
  'user_engagement',
  'core_sales',
  'emerging_monetization',
];


const dimensionHeadersDescription = {
  'strategic_direction': 'Doing this well means that data is understood universally, it supports key business objectives, and there are robust data resources and technologies in place.',
  'user_engagement': 'Leading Retailers clearly understand the context of the full customer journey and why customers engage. Teams effectively use customer data and insights to design an on-site experience that increases customer engagement and improves the efficiency of their path to purchase.',
  'core_sales': 'Leading Retailers have differentiated features that are relevant to customers across their life cycles. The portfolio of features and products are mutually reinforcing, and it drives loyalty and increases LTV. You frequently use LTV metrics to support business decisions, like providing targeted customer support or pushing tailored promotions to specific customers.',
  'emerging_monetization': 'Best-in-class build unique segments using enriched first-party data that gets to the heart of customer interest and purchase intent. You proactively collaborate with suppliers, non-suppliers, and advertising agencies to craft campaigns that incorporate unique audience insights. You maintain a unified view of customer profiles to support certain online to offline sales activities.',
};


const dimensionLevelDescription = {
  'strategic_direction': {
    0: 'You have limited strategy in connecting data with your overarching business goals.',
    1: 'Leadership have provided an initial articulation of specific and well-defined data initiatives, but there is limited continued focus on this.',
    2: 'There is widespread knowledge and respect for the role data plays in achieving the overall business strategy.',
    3: 'There is universal understanding of how data underpins the overarching business strategy, at all levels.',
  },
  'user_engagement': {
    0: 'You collect basic engagement data (e.g., page views), but do not translate it into customer engagement insights. UI / UX decisions are primarily based on instinct and team experience.',
    1: 'You know what the broad customer segments are and start to uncover discrete customer insights using basic web analytics tools. However, customer experience and UI / UX decisions are made based on qualitative judgment.',
    2: 'You understand how different segments engage with product pages and use these insights to improve engagement. Customer engagement data and insights drive certain design decisions on your digital platforms (e.g., product description length, thumbnail image size).',
    3: 'You clearly understand the context of the full customer journey and why customers engage. Teams effectively use customer data and insights to design an on-site experience that increases customer engagement and improves the efficiency of their path to purchase.',
  },
  'core_sales': {
    0: 'Your product offering is limited to a one size fits all merchandising strategy.',
    1: 'You use metrics to develop recommendations and promotions for your product assortment. You understand and use conversion triggers that signal specific customer actions, like adding items to a basket or completing a transaction.',
    2: 'You use different features to improve the customer’s journey and determine how to bundle these features for different customer segements. Your business uses LTV-focused metrics and has a strong grasp on drivers of key customer actions, like sales conversion and basket abandonment.',
    3: 'You have differentiated features that are relevant to customers across their life cycles. The portfolio of features and products are mutually reinforcing, and it drives loyalty and increases LTV. You frequently use LTV metrics to support business decisions, like providing targeted customer support or pushing tailored promotions to specific customers.',
  },
  'emerging_monetization': {
    0: 'You have basic segments (e.g., demographics, location) created to facilitate targeted marketing efforts for suppliers and non-suppliers.',
    1: 'You use combinations of pre-built segments to assemble campaigns for suppliers and non-suppliers. You have technology tools that allow you to provide performance reporting directly to suppliers and non-suppliers.',
    2: 'You use different data sets to build interest and intent-based segments. You share insights and equip the sales team to clearly communicate the value of different segments to suppliers and non-suppliers. You maintain customer profiles that allow some degree of integration between on-site and offline customer data.',
    3: 'You build unique segments using enriched first-party data that gets to the heart of customer interest and purchase intent. You proactively collaborate with suppliers, non-suppliers, and advertising agencies to craft campaigns that incorporate unique audience insights. You maintain a unified view of customer profiles to support certain online to offline sales activities.',
  },
};

const dataActivationGuideCta = {
  'text': 'Data Activation Guide',
  'link': 'https://www2.deloitte.com/content/dam/Deloitte/us/Documents/consumer-business/us-digital-transformation-through-data-for-retail.pdf',
};

const dimensionLevelRecommendations = {
  'strategic_direction': {
    0: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Articulate your broader organizational mission and identify areas in which data may be able to support or drive efforts to meet the mission.',
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
        'text': 'Many Nascent retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    1: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organization’s approach to handling and activating data.Encourage leadership at all levels to communicate this message to team members.',
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
        'text': 'Many Developing retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    2: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organization’s approach to handling and activating data.Encourage leadership at all levels to communicate this message to team members.',
      },
      {
        'header': 'Foster collaboration and cross-functional teamwork',
        'text': 'Incorporate data strategy messaging in team meetings. Establish key performance indicators (KPIs) that drive collaboration across organizational silos and incentivize cross-functional performance.',
      },
      {
        'header': 'Democratise your data',
        'text': 'Create intuitive tools and portals that enable access to relevant audience data for all team members.  Provide trainings and educational resources to team members and encourage use of available resources.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature retailers have a well-established data strategy but want to see what other retailers are doing. Start with the Data Foundations section of the Data Activation Guide to see how some Leading retailers have developed their cultural, skills-based, data-related, and technological foundations.',
        'cta': dataActivationGuideCta,
      },
    ],
    3: [
      {
        'header': 'Broadcast a thoughtful data strategy',
        'text': 'Craft messaging that captures your organization’s approach to handling and activating data.Encourage leadership at all levels to communicate this message to team members.',
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
        'text': 'Many Leading retailers have a well-established data strategy but want to see what other retailers are doing. Start with the Data Foundations section of the Data Activation Guide to see how other Leading retailers have developed their cultural, skills-based, data-related, and technological foundations.',
        'cta': dataActivationGuideCta,
      },
    ],
  },
  'user_engagement': {
    0: [
      {
        'header': 'Measure it to improve it',
        'text': 'Drive collaboration amongst data teams and business leaders to prioritize data collection activities and measurement capabilities.',
      },
      {
        'header': 'Understand what makes your customers tick',
        'text': 'Develop basic segmentation processes that capture high-level interest-based or behavioral segments for analysis. Understand your different segments of customers and how they engage with your products and your platform.',
      },
      {
        'header': 'Connect data to your products',
        'text': 'Deploy a product tagging technology system and develop a common taxonomy to improve the searchability of your product catalog.',
      },
      {
        'header': 'Make the experience intuitive',
        'text': 'Build your team’s skills in web analytics to better understand and improve pain points in the customer journey.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    1: [
      {
        'header': 'Measure it to improve it',
        'text': 'Identify organizational objectives and tie key performance metrics to those objectives.',
      },
      {
        'header': 'Understand what makes your customers tick',
        'text': 'Build technical teams to enhance segmentation practices and improve on foundational understandings of how customers engage with your platform.',
      },
      {
        'header': 'Connect data to your products',
        'text': 'Deploy technology solutions to support cross-functional collaboration between data and merchandizing teams and help guide product decisions.',
      },
      {
        'header': 'Make the experience intuitive',
        'text': 'Capture and organize customer on-site behavioral data to inform user interface and design decisions.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    2: [
      {
        'header': 'Measure it to improve it',
        'text': 'Make analytics and reporting accessible to relevant team members, so everyone in the organization can understand the health and performance of the digital platform.',
      },
      {
        'header': 'Understand what makes your customers tick',
        'text': 'Build new customer segments and enhance customer profiles to better tailor products and user interface decisions to satisfy specific customer preferences.',
      },
      {
        'header': 'Organize your content for future opportunities',
        'text': 'Maintain your content catalog and provide intuitive tools to editorial teams to help surface insights that can inform content planning activities.',
      },
      {
        'header': 'Promote experimentation',
        'text': 'Use A/B and multivariate tests to frequently identify areas to improve user interface and product options for customers. Promote a culture of testing and learning to drive continual improvement.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature retailers have sophisticated approaches to improving the user experience but want to see what other retailers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading retailers have approached improving the user experience.',
        'cta': dataActivationGuideCta,
      },
    ],
    3: [
      {
        'header': 'Measure it to improve it',
        'text': 'Continue to roll out analytics and reporting tools to support cross-functional and performance-based decision-making.',
      },
      {
        'header': 'Understand what makes your customers tick',
        'text': 'Enhance technological capabilities and data collection efforts to refine the understanding of customer segments and individual customer profiles. Continue to uncover insights that inform best ways to serve customers.',
      },
      {
        'header': 'Individualize customer experiences',
        'text': 'Use customer profile data to inform user interface and navigation decisions for individual customers, based on their needs and preferences; use unique insights to provide a tailored look and feel for loyal customers.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading retailers have a sophisticated approach to improving the user experience but want to see what other retailers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading retailers have approached improving the user experience.',
        'cta': dataActivationGuideCta,
      },
    ],
  },
  'core_sales': {
    0: [
      {
        'header': 'Understand the value of your customers',
        'text': 'Understand your different segments of customers and how they engage with your products and your platform. Implement simple plug-in tools to help you measure and visualize these customer segments and how much value they represent for the business.',
        'cta': {
          'text': 'News Consumer Insights',
          'link': 'https://newsinitiative.withgoogle.com/training/newsconsumerinsights',
        },
      },
      {
        'header': 'Tailor your product recommendation strategy',
        'text': 'Understand the needs and behaviors of your customers and collaborate cross-functionally to develop strategies to recommend the right products for your customers..',
      },
      {
        'header': 'Identify new ways to serve loyal customers',
        'text': 'Identify engaged segments of your customer-base and explore new offerings (i.e., memberships, subscriptions, or auto-renewal programs) that may improve their overall customer experience.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    1: [
      {
        'header': 'Understand the value of your customers ',
        'text': 'Start to layer in more behavioral data that tells you how different customers behave online and how those behaviors can translate to retail value. Use customer insights to identify new ways to increase customer value (i.e., tailored communications, recommendations, and promotional offers).',
      },
      {
        'header': 'Tailor your product recommendation strategy',
        'text': 'Segment your customers based on their browsing behavior and measure how effective your product recommendations are with different customer types. Tailor future recommendations based on the feedback.',
      },
      {
        'header': 'Identify new ways to serve loyal customers',
        'text': 'Integrate your data across different customer offerings (i.e., memberships, subscriptions, or auto-renewal programs) to get an understanding of customer behavior across the whole business. Develop the capability to identify individual customers and structure opportunities to support them across devices and retail platforms.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide details how some Leading retailers have approached enhancing core sales activities.',
        'cta': dataActivationGuideCta,
      },
    ],
    2: [
      {
        'header': 'Understand the value of your customers',
        'text': 'Integrate a view of customer lifetime value(LTV) into core business decision- making.Ensure that core functions in the marketing, merchandising, and product teams consider the impact on customer LTV when making key decisions.',
      },
      {
        'header': 'Tailor your product recommendation strategy',
        'text': 'Employ sophisticated techniques to tailor product promotions and match them to specific segments based on their behavior on your platform. Create a feedback loop to analyze the results and understand points of improvement.',
      },
      {
        'header': 'Develop unique experiences for loyal customers',
        'text': 'Actively cross promote different product offerings or promotions based on customer interests or characteristics. Start to understand the relative value of decisions to direct customers to different products and promotions.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature retailers have created significant revenue from enhancing core sales activities but want to see what other retailers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading retailers have approached enhancing core sales activities.',
        'cta': dataActivationGuideCta,
      },
    ],
    3: [
      {
        'header': 'Understand the value of your customers',
        'text': 'Continue to refine the approach to quantifying customer lifetime value (LTV).  Leverage customer LTV data to inform operational improvements and identify strategic growth opportunities.',
      },
      {
        'header': 'Tailor your product recommendation strategy',
        'text': 'Continually improve the approach to converting customers to purchasers based on updates to predictive models and product promotion strategies.',
      },
      {
        'header': 'Individualize experiences for loyal customers',
        'text': 'Leverage your unique customer insights, and Individualize shopper experiences for loyal customers by using persistent customer identifiers and serving them tailored experiences based on their needs and preferences.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading retailers have a sophisticated approach to enhancing core sales activities but want to see what other retailers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading retailers have approached enhancing core sales activities.',
        'cta': dataActivationGuideCta,
      },
    ],
  },
  'emerging_monetization': {
    0: [
      {
        'header': 'Build and enhance the understanding of your customers',
        'text': 'Develop basic segmentation processes that capture high-level interest-based or behavioral segments for analysis. Understand your different segments of customers and how they engage with your product and your platform.',
      },
      {
        'header': 'Connect the right customers to the right supplier or advertiser',
        'text': 'Collaborate with your suppliers and advertisers to identify the customers they want to reach. Start incorporating advertiser input into customer segmentation practices.',
      },
      {
        'header': 'Know the value of your customers to suppliers and advertisers',
        'text': 'Monitor the performance of different customer segments across your sales mix. Analyze and record insights across segments to develop a long-term understanding of customer segment performance.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Nascent retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    1: [
      {
        'header': 'Build and enhance the understanding of your customers',
        'text': 'Start to layer in data that tells you how different customers behave online and how this impacts the value they bring. Build technical teams to enhance segmentation practices and improve on foundational understandings of how customers engage with your platform.',
      },
      {
        'header': 'Connect the right customers to the right supplier or advertiser',
        'text': 'Collaborate with your suppliers and advertisers to identify the customers they want to reach. Start incorporating advertiser input into customer segmentation practices.',
      },
      {
        'header': 'Know the value of your customers to suppliers and advertisers',
        'text': 'Monitor the performance of different customer segments across your sales mix. Analyze and record insights across segments to develop a long-term understanding of customer segment performance.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Developing retailers still need to get their cultural, skills-based, data-related, and technological foundations right. The Data Foundations section of the Data Activation Guide provides tips and best practices to overcome some of these challenges.',
        'cta': dataActivationGuideCta,
      },
    ],
    2: [
      {
        'header': 'Build and enhance the understanding of your customers',
        'text': 'Integrate a view of customer lifetime value into core business decision-making. Experiment to test the relative value and performance of customer segments to refine high-demand segments. Develop systems to effectively price customer segments based on historical performance and perceived value to suppliers and advertisers.',
      },
      {
        'header': 'Connect the right customers to the right supplier or advertiser',
        'text': 'Continue to foster relationships with key suppliers and advertisers, and collaborate to proactively identify ways to support their future advertising strategies.',
      },
      {
        'header': 'Bring campaigns to life',
        'text': 'Think about digital advertising (for suppliers and non-suppliers) holistically and drive value through the strategic combination of relevant context, creative, advertising placement, and advertising format to create the right balance between high-value advertising and positive customer experiences.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Mature retailers have generated revenue through engaging in emerging monetisation opportunities but want to see what other retailers are doing. The Activating Use Cases section of the Data Activation Guide details how some Leading retailers have approached engaging in emerging monetisation opportunities.',
        'cta': dataActivationGuideCta,
      },
    ],
    3: [
      {
        'header': 'Build and enhance the understanding of your customers',
        'text': 'Integrate a view of customer lifetime value into core business decision-making. Experiment to test the relative value and performance of customer segments to refine high-demand segments. Develop systems to effectively price customer segments based on historical performance and perceived value to suppliers and advertisers.',
      },
      {
        'header': 'Connect the right customers to the right supplier or advertiser',
        'text': 'Continue to foster relationships with key suppliers and advertisers, and collaborate to proactively identify ways to support their future advertising strategies through the strategic combination of relevant context, creative, advertising placement, and advertising format to create the right balance between high-value advertising and positive customer experiences.',
      },
      {
        'header': 'Use technology to scale',
        'text': 'Enhance technological capabilities, including focusing on advertising technology(e.g., supply-side advertising platform), to effectively serve advertisers at scale without sacrificing quality of content or customer experience.',
      },
      {
        'header': 'Data Activation Guide',
        'text': 'Many Leading retailers have a sophisticated approach to engaging in emerging monetisation opportunities but want to see what other retailers are doing. The Activating Use Cases section of the Data Activation Guide details how other Leading retailers have approached engaging in emerging monetization opportunities.',
        'cta': dataActivationGuideCta,
      },
    ],
  },
};


const conf = {
  levels,
  levelDescriptions,
  reportLevelDescriptions,
  industryAvgDescription,
  industryBestDescription,
  dimensions,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelRecommendations,
};


exports = conf;
