# coding=utf-8
# flake8: noqa
from . import GOOGLE_SHEET_BASE_SURVEY_FIELDS, GOOGLE_SHEET_BASE_RESULT_FIELDS

# DIMENSIONS
DIMENSION_LEARN = 'learn'
DIMENSION_LEAD = 'lead'
DIMENSION_SCALE = 'scale'
DIMENSION_SECURE = 'secure'

# SUBDIMENSIONS
SUBDIMENSION_EXTERNAL_EXPERIENCE = 'external_experience'
SUBDIMENSION_UPSKILLING = 'upskilling'
SUBDIMENSION_TEAMWORK = 'teamwork'
SUBDIMENSION_SPONSORSHIP = 'sponsorship'
SUBDIMENSION_INFRASTRUCTURE_AS_CODE = 'infrastructure_as_code'
SUBDIMENSION_RESOURCE_MANAGEMENT = 'resource_management'
SUBDIMENSION_CI_CD = 'ci_cd'
SUBDIMENSION_ARCHITECTURE = 'architecture'
SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT = 'identity_and_access_management'
SUBDIMENSION_DATA_MANAGEMENT = 'data_management'
SUBDIMENSION_ACCESS_MANAGEMENT = 'access_management'
SUBDIMENSION_IDENTITY_MANAGEMENT = 'identity_management'
SUBDIMENSION_NETWORKING = 'networking'


# LEVELS
LEVEL_0 = 0
LEVEL_1 = 0.5
LEVEL_2 = 1
LEVEL_3 = 1.5
LEVEL_4 = 2
LEVELS_MAX = 3

# WEIGHTS
WEIGHTS = {}

DIMENSION_TITLES = {
    DIMENSION_LEARN: 'Learn',
    DIMENSION_LEAD: 'Lead',
    DIMENSION_SCALE: 'Scale',
    DIMENSION_SECURE: 'Secure',
}

DIMENSION_ORDER = [
    DIMENSION_LEARN,
    DIMENSION_LEAD,
    DIMENSION_SCALE,
    DIMENSION_SECURE,
]


SUBDIMENSION_TITLES = {
    SUBDIMENSION_EXTERNAL_EXPERIENCE: 'External Experience',
    SUBDIMENSION_UPSKILLING: 'Upskilling',
    SUBDIMENSION_TEAMWORK: 'Teamwork',
    SUBDIMENSION_SPONSORSHIP: 'Sponsorship',
    SUBDIMENSION_INFRASTRUCTURE_AS_CODE: 'Infrastructure_as_code',
    SUBDIMENSION_RESOURCE_MANAGEMENT: 'Resource Management',
    SUBDIMENSION_CI_CD: 'Ci/Cd',
    SUBDIMENSION_ARCHITECTURE: 'Architecture',
    SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT: 'Identity And Access Management',
    SUBDIMENSION_DATA_MANAGEMENT: 'Data Management',
    SUBDIMENSION_ACCESS_MANAGEMENT: 'Access Management',
    SUBDIMENSION_IDENTITY_MANAGEMENT: 'Identity Management',
    SUBDIMENSION_NETWORKING: 'Networking',
}

SUBDIMENSION_ORDER = {
    DIMENSION_LEARN: [
        SUBDIMENSION_EXTERNAL_EXPERIENCE,
        SUBDIMENSION_UPSKILLING,
    ],
    DIMENSION_LEAD: [
        SUBDIMENSION_TEAMWORK,
        SUBDIMENSION_SPONSORSHIP,
    ],
    DIMENSION_SCALE: [
        SUBDIMENSION_INFRASTRUCTURE_AS_CODE,
        SUBDIMENSION_RESOURCE_MANAGEMENT,
        SUBDIMENSION_CI_CD,
        SUBDIMENSION_ARCHITECTURE,
    ],
    DIMENSION_SECURE:[
        SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT,
        SUBDIMENSION_DATA_MANAGEMENT,
        SUBDIMENSION_ACCESS_MANAGEMENT,
        SUBDIMENSION_IDENTITY_MANAGEMENT,
        SUBDIMENSION_NETWORKING,
    ]
}

DIMENSIONS = {
    DIMENSION_LEARN: [
        'Q7',
        'Q8',
        'Q9',
        'Q10',
        'Q11',
    ],
    DIMENSION_LEAD: [
        'Q13',
        'Q14',
        'Q15',
        'Q16',
        'Q17',
        'Q18',
    ],
    DIMENSION_SCALE: [
        'Q20',
        'Q21',
        'Q22',
        'Q23',
        'Q24',
        'Q25',
    ],
    DIMENSION_SECURE: [
        'Q27',
        'Q28',
        'Q29',
        'Q30',
        'Q31',
        'Q32',
        'Q33',
        'Q34',
    ],
    SUBDIMENSION_EXTERNAL_EXPERIENCE: [
        'Q7',
        'Q11',
    ],
    SUBDIMENSION_UPSKILLING: [
        'Q8',
        'Q9',
        'Q10',
    ],
    SUBDIMENSION_TEAMWORK: [
        'Q13',
        'Q15',
        'Q16',
        'Q18',
    ],
    SUBDIMENSION_SPONSORSHIP: [
        'Q14',
        'Q17',
    ],
    SUBDIMENSION_INFRASTRUCTURE_AS_CODE: [
        'Q20',
    ],
    SUBDIMENSION_RESOURCE_MANAGEMENT: [
        'Q21',
        'Q22',
    ],
    SUBDIMENSION_CI_CD: [
        'Q23',
        'Q24',
    ],
    SUBDIMENSION_ARCHITECTURE: [
        'Q25'
    ],
    SUBDIMENSION_DATA_MANAGEMENT: [
        'Q27',
        'Q29',
        'Q33',
    ],
    SUBDIMENSION_IDENTITY_AND_ACCESS_MANAGEMENT: [
        'Q28',
        'Q30',
    ],
    SUBDIMENSION_ACCESS_MANAGEMENT: [
        'Q32',
    ],
    SUBDIMENSION_IDENTITY_MANAGEMENT: [
        'Q31',
    ],
    SUBDIMENSION_NETWORKING: [
        'Q34',
    ],
}

MULTI_ANSWER_QUESTIONS = []


LEVELS = {
    LEVEL_0: 'Tactical',
    LEVEL_2: 'Strategic',
    LEVEL_4: 'Transformational',
}

LEVELS_DESCRIPTIONS = {
    LEVEL_0: 'Organizations in this phase often have individual cloud workloads in place, but no coherent plan encompassing all of them nor a strategy for building out for the future. The focus is on reducing the cost of discrete systems and on getting to the cloud with minimal disruption. The wins are quick, but there is no provision for scale.',
    LEVEL_2: 'Organizations in this phase have a broad vision that governs individual workloads, which are designed and developed with an eye to future needs and scale. The organization has started to embrace change, and the people and process portion of the equation are now involved. IT teams are both efficient and effective, increasing the value of harnessing the cloud for business operations.',
    LEVEL_4: 'Organizations in this phase have cloud operations functioning smoothly, and have turned their attention to integrating the data and insights garnered from working in the cloud. Existing data is transparently shared. New data is collected and analyzed. The predictive and prescriptive analytics of machine learning applied. People and processes are being transformed, which further supports the technological changes. IT is no longer a cost center, but has become a partner to the business.',
}

REPORT_LEVEL_DESCRIPTIONS = {
    LEVEL_0: 'This is the most basic of the three phases of maturity. You are probably reducing costs with a quick return on investment and little disruption to your IT organization.',
    LEVEL_1: 'This is the most basic of the three phases of maturity but you are on your way towards the next phase. You are probably reducing costs with a quick return on investment and little disruption to your IT organization.',
    LEVEL_2: 'This is the second of the three phases of maturity. You are increasing the value delivered by your IT organization by streamlining operations to be both more efficient and more effective.',
    LEVEL_3: 'This is the second of the three phases of maturity, but you are on your way towards the next phase. You are increasing the value delivered by your IT organization by streamlining operations to be both more efficient and more effective.',
    LEVEL_4: 'This is the most advanced of the three phases of maturity. Your IT organization is becoming an engine of innovation, making it a partner to the business.',
}


INDUSTRY_AVG_DESCRIPTION = 'How organizations perform on average; dynamically calculated based on the results of those who have completed this survey.'

INDUSTRY_BEST_DESCRIPTION = 'This is the highest recorded score from a participant who has taken the Google Cloud Maturity Assessment.'



DIMENSION_HEADER_DESCRIPTIONS = {
    DIMENSION_LEARN: '<p class="dmb-u-m-b-s">Your organization’s ability to continuously learn is determined by your efforts to upskill your IT staff while also taking advantage of the experiences shared by third-party contractors and partners. This two-pronged approach ensures that you apply cloud computing best practices idiomatically to Google Cloud Platform (or any other public cloud provider), tailored to your business needs and without having to climb the steep learning curve of doing things for the first time.</p><p class="dmb-u-m-b-s">Your staff will be more familiar with your organization’s unique idiosyncrasies and understand its technical and cultural nuances, while supporting third parties will have the experience of having completed multiple prior cloud migrations across a broad spectrum of customer solutions.</p>',
    DIMENSION_LEAD: '<p class="dmb-u-m-b-s">The effectiveness of your organization’s cloud adoption is determined by the visibility and value of the mandate issued top-down from your sponsors (which include C-level executives as well as middle management and team leaders) and the motivational momentum generated bottom-up from your teams’ cross-functional collaboration. These two counterparts together are responsible for clearly articulating objectives, making informed decisions, and executing them in concert with multiple functions.</p><p class="dmb-u-m-b-s">Sponsors control which resources are allocated to your organization’s cloud adoption efforts and bring stakeholders from different business functions and reporting lines together. However, they must ultimately rely on an agile and cross-functional group of cloud early adopters to practically implement their strategy.</p>',
    DIMENSION_SCALE: '<p class="dmb-u-m-b-s">Your organization’s ability to scale in the cloud is determined by the extent to which you abstract away your infrastructure with managed and serverless cloud services, as well as the quality of your CI/CD process chain and the programmable infrastructure code that runs through it.</p><p class="dmb-u-m-b-s">Because everything is managed via an API, automation can pay greater dividends in the cloud than in any other environment. Not only does it reduce human toil and serve as automatic documentation, it is also instrumental in making change low risk and frequent - the key ingredient for innovation.</p>',
    DIMENSION_SECURE: '<p class="dmb-u-m-b-s">In the narrow sense, the security of your cloud estate is determined by your ability to guarantee who may perform which action on which resource (identity and access management) and your understanding of the data that needs protecting, ensuring it is appropriately catalogued, encrypted, and guarded from exfiltration, to name just a few considerations.</p><p>In the more holistic sense, your security posture relies on the advanced maturity of the other three cloud adoption themes:</p><ol class="dmb-u-m-b-s"><li>continuous learning of the latest technical vulnerabilities and security best practices</li><li>leading by setting measurable security objectives and rewarding a culture of blameless postmortems</li><li>scaling through automation which, in turn, minimizes human error and maximizes auditability.</li></ol><p class="dmb-u-m-b-s">Because security is so essential and because it cuts across all dimensions and themes, it lives at the very center of the cloud adoption model.</p>',
}

DIMENSION_LEVEL_DESCRIPTION = {
    DIMENSION_LEARN: {
        LEVEL_0: '<p class="dmb-u-m-b-s">Upskilling is on a best-effort basis, reliant on individual self-motivation and free educational resources like online documentation and YouTube.</p><p class="dmb-u-m-b-s">Third-party contractors and partners are relied upon to deliver essential work required to achieve the objectives set out by the business. They typically enjoy wide-ranging and ongoing privileged access to your organization’s cloud estate and serve as a first point of escalation in the event of a technical question or an operational incident.</p><p class="dmb-u-m-b-s">You expect to be able to achieve tactical objectives with the IT staff you have and are not taking action to hire new staff with prior cloud experience.</p>',
        LEVEL_1: '<p class="dmb-u-m-b-s">Upskilling is on a best-effort basis, reliant on individual self-motivation and free educational resources like online documentation and YouTube.</p><p class="dmb-u-m-b-s">Third-party contractors and partners are relied upon to deliver essential work required to achieve the objectives set out by the business. They typically enjoy wide-ranging and ongoing privileged access to your organization’s cloud estate and serve as a first point of escalation in the event of a technical question or an operational incident.</p><p class="dmb-u-m-b-s">You expect to be able to achieve tactical objectives with the IT staff you have and are not taking action to hire new staff with prior cloud experience.</p>',
        LEVEL_2: '<p class="dmb-u-m-b-s">Upskilling is program managed and offered to any IT role who is directly or indirectly responsible for contributing to a successful cloud adoption. A learning plan has been published, training classes (online or offline) are offered on a regular basis, and achieving formal certification is encouraged and budgeted for.</p><p class="dmb-u-m-b-s">Third-party contractors and partners provide subject matter expertise to fill the IT staff’s remaining knowledge gaps or where the topic is so narrow and deep that it would be unreasonable to expect your IT staff to upskill to that level. These external parties serve as a second-tier point of escalation in the event of a technical question or operational incident that cannot be answered or resolved internally within your IT staff. As such, they will typically have moderated access to the organization’s cloud estate and be authorized (and audited) to escalate their privileges in break-glass scenarios that require quick and determined intervention.</p><p class="dmb-u-m-b-s">You are actively opening new roles and are hiring for people with prior cloud experience to complement the IT staff as it upskills itself on cloud computing best practices.</p><p class="dmb-u-m-b-s">Each IT staff member is given a GCP sandbox project and a limited budget for them to experiment with and test new ideas.</p>',
        LEVEL_3: '<p class="dmb-u-m-b-s">Upskilling is program managed and offered to any IT role who is directly or indirectly responsible for contributing to a successful cloud adoption. A learning plan has been published, training classes (online or offline) are offered on a regular basis, and achieving formal certification is encouraged and budgeted for.</p><p class="dmb-u-m-b-s">Third-party contractors and partners provide subject matter expertise to fill the IT staff’s remaining knowledge gaps or where the topic is so narrow and deep that it would be unreasonable to expect your IT staff to upskill to that level. These external parties serve as a second-tier point of escalation in the event of a technical question or operational incident that cannot be answered or resolved internally within your IT staff. As such, they will typically have moderated access to the organization’s cloud estate and be authorized (and audited) to escalate their privileges in break-glass scenarios that require quick and determined intervention.</p><p class="dmb-u-m-b-s">You are actively opening new roles and are hiring for people with prior cloud experience to complement the IT staff as it upskills itself on cloud computing best practices.</p><p class="dmb-u-m-b-s">Each IT staff member is given a GCP sandbox project and a limited budget for them to experiment with and test new ideas.</p>',
        LEVEL_4: '<p class="dmb-u-m-b-s">Upskilling is continuous and collaborative. In addition to a regular formal training program, IT teams and individual contributors host regular hackathons and tech talks to maximize knowledge sharing. Going one step further, IT staff are encouraged to demonstrate thought leadership to the industry through public blog articles and public speaking. This outreach serves a double function of challenging staff to stretch themselves and also to attract new talent to be hired.</p><p class="dmb-u-m-b-s">You have reviewed and, where needed, redefined all roles and responsibilities to reflect the new requirements of a cloud-first IT organization.</p><p class="dmb-u-m-b-s">Third-party contractors and partners serve primarily as staff augmentation with no privileged access and very few areas of exclusive knowledge. Most technical questions can be answered internally, and all incident response playbooks can be executed entirely in-house.</p>',
    },
    DIMENSION_LEAD: {
        LEVEL_0: '<p class="dmb-u-m-b-s">Sponsorship is limited to senior management from or for one line of business. Their primary contribution is delivering the mandate (“signing off”) and passing it down their reporting line to be executed upon. Sponsors only get actively involved as a final point of escalation when progress is otherwise hampered.</p><p class="dmb-u-m-b-s">Cloud adoption progress is driven by individual contributors with a personal interest in cloud computing for their solution(s). The ability for early adopters to collaborate with other IT roles is subject to the friction of the incumbent org structure and reporting lines.</p><p class="dmb-u-m-b-s">Because the scope is limited to the project or line of business that this team of early adopters is aligned with -- and must operate within that budget -- their output will not be embedded with central IT. Depending on the perspective, the outcome is either a “minimum viable cloud” or “cloud shadow IT”.</p>',
        LEVEL_1: '<p class="dmb-u-m-b-s">Sponsorship is limited to senior management from or for one line of business. Their primary contribution is delivering the mandate (“signing off”) and passing it down their reporting line to be executed upon. Sponsors only get actively involved as a final point of escalation when progress is otherwise hampered.</p><p class="dmb-u-m-b-s">Cloud adoption progress is driven by individual contributors with a personal interest in cloud computing for their solution(s). The ability for early adopters to collaborate with other IT roles is subject to the friction of the incumbent org structure and reporting lines.</p><p class="dmb-u-m-b-s">Because the scope is limited to the project or line of business that this team of early adopters is aligned with -- and must operate within that budget -- their output will not be embedded with central IT. Depending on the perspective, the outcome is either a “minimum viable cloud” or “cloud shadow IT”.</p>',
        LEVEL_2: '<p class="dmb-u-m-b-s">Sponsorship extends up to the C-level. Each manager in the reporting line has clearly defined objectives and KPIs that support the organization’s cloud adoption. Sponsors’ key contributions include actively reaching out horizontally to other IT or business functions to clear the critical path of roadblocks and visibly and continuously championing the journey.</p><p class="dmb-u-m-b-s">Performance indicators prioritize traditional IT service-level objectives over the speed of experimentation, innovation, and recovery from failure.</p><p class="dmb-u-m-b-s">Cloud adoption progress is driven by a dedicated cross-functional team (Center of Excellence) of advocates, working across project boundaries. All critical IT roles inside this COE are filled, for example, application architect, software or data engineer, networking engineer, and identity/directory admin, across operations, information security, and finance. Team members are committed full-time or part-time, and their job title and their personal performance indicators are updated to reflect their new responsibilities.</p><p class="dmb-u-m-b-s">Cloud adoption may also be complemented by a dedicated technical project manager who is familiar with the IT organization, the stakeholders, and the technology landscape.</p>',
        LEVEL_3: '<p class="dmb-u-m-b-s">Sponsorship extends up to the C-level. Each manager in the reporting line has clearly defined objectives and KPIs that support the organization’s cloud adoption. Sponsors’ key contributions include actively reaching out horizontally to other IT or business functions to clear the critical path of roadblocks and visibly and continuously championing the journey.</p><p class="dmb-u-m-b-s">Performance indicators prioritize traditional IT service-level objectives over the speed of experimentation, innovation, and recovery from failure.</p><p class="dmb-u-m-b-s">Cloud adoption progress is driven by a dedicated cross-functional team (Center of Excellence) of advocates, working across project boundaries. All critical IT roles inside this COE are filled, for example, application architect, software or data engineer, networking engineer, and identity/directory admin, across operations, information security, and finance. Team members are committed full-time or part-time, and their job title and their personal performance indicators are updated to reflect their new responsibilities.</p><p class="dmb-u-m-b-s">Cloud adoption may also be complemented by a dedicated technical project manager who is familiar with the IT organization, the stakeholders, and the technology landscape.</p>',
        LEVEL_4: '<p class="dmb-u-m-b-s">Sponsorship is comprehensive across the entire C-level to include marketing, finance, operations, HR, and more, and extends down to all levels of management. They comprehensively and consistently set the tone for a culture of experimentation and innovation within teams. Error budgets for software services are accepted and understood at the highest level (CEO), and a culture of blameless postmortems is fostered throughout the IT organization.</p><p class="dmb-u-m-b-s">Project teams operate in an environment of transparency and open information sharing and enjoy enough decision-making autonomy to be able to experiment ad hoc without having to ask for permission or having to wait for resources to be provisioned. (Data governance and cost control are now a function of automation, not manual managerial process.) Failures are celebrated for the valuable lessons that the team has learned and will be shared with the wider business for posterity. An individual’s mistake is interpreted as a collective or systematic failure that must be addressed as a whole, not by reprimanding the individual.</p>',
    },
    DIMENSION_SCALE: {
        LEVEL_0: '<p class="dmb-u-m-b-s">Use of managed or serverless cloud services is limited. Instead, a continued reliance on self-managed, long-lived virtual machines (VMs) provides a familiar computing platform at the risk of entropy (“config drift”), making consistent and secure operations increasingly hard over time. Because there is more to be managed, there is also more to be measured, increasing the burden of collecting quality, high-frequency events and metrics.</p><p class="dmb-u-m-b-s">Changes to application code and environment configuration are reviewed and controlled manually, for example, by a change advisory board. They are often considered high risk and deployed infrequently, measured in weeks or even months.</p><p class="dmb-u-m-b-s">The provisioning of cloud resources is performed manually via the GCP Web Console or command-line interface (CLI). Infrastructure automation tools like Deployment Manager or Hashicorp’s Terraform are not leveraged. While the use of the GCP Web Console or CLI is already a great improvement over the manual process of racking and stacking servers, it only marks the beginning of the cloud’s potential for automation.</p>',
        LEVEL_1: '<p class="dmb-u-m-b-s">Use of managed or serverless cloud services is limited. Instead, a continued reliance on self-managed, long-lived virtual machines (VMs) provides a familiar computing platform at the risk of entropy (“config drift”), making consistent and secure operations increasingly hard over time. Because there is more to be managed, there is also more to be measured, increasing the burden of collecting quality, high-frequency events and metrics.</p><p class="dmb-u-m-b-s">Changes to application code and environment configuration are reviewed and controlled manually, for example, by a change advisory board. They are often considered high risk and deployed infrequently, measured in weeks or even months.</p><p class="dmb-u-m-b-s">The provisioning of cloud resources is performed manually via the GCP Web Console or command-line interface (CLI). Infrastructure automation tools like Deployment Manager or Hashicorp’s Terraform are not leveraged. While the use of the GCP Web Console or CLI is already a great improvement over the manual process of racking and stacking servers, it only marks the beginning of the cloud’s potential for automation.</p>',
        LEVEL_2: '<p class="dmb-u-m-b-s">VMs are designed to be immutable, thereby greatly reducing the scope for change to a system. Environment configuration is baked into versioned VM images, and stateful and stateless workloads are cleanly separated to allow for elastic horizontal scaling. Inside the VM, configuration values and keys are stored only in-memory, and outside the VM only in discrete services like the GCP metadata service, Cloud Key Management Service, or Hashicorp Vault.</p><p class="dmb-u-m-b-s">The risk of change is considered to be mostly moderate. Deployments to production environments are executed programmatically, but triggered manually, and can be easily rolled back if necessary.</p><p class="dmb-u-m-b-s">Application teams go beyond basic monitoring and logging, making use of application performance monitoring (APM), either through Stackdriver or through a third-party solution to deliver near real-time insights into service health under real production loads, 24/7.</p><p class="dmb-u-m-b-s">The provisioning of GCP projects includes all associated configurations (like VPC networking, billing account, and Cloud Identity and Access Management policies) and is performed programmatically via Deployment Manager or Hashicorp Terraform, based on a limited set of inputs like cost center, data sensitivity, team ownership, and dependency with services hosted in other GCP projects.</p>',
        LEVEL_3: '<p class="dmb-u-m-b-s">VMs are designed to be immutable, thereby greatly reducing the scope for change to a system. Environment configuration is baked into versioned VM images, and stateful and stateless workloads are cleanly separated to allow for elastic horizontal scaling. Inside the VM, configuration values and keys are stored only in-memory, and outside the VM only in discrete services like the GCP metadata service, Cloud Key Management Service, or Hashicorp Vault.</p><p class="dmb-u-m-b-s">The risk of change is considered to be mostly moderate. Deployments to production environments are executed programmatically, but triggered manually, and can be easily rolled back if necessary.</p><p class="dmb-u-m-b-s">Application teams go beyond basic monitoring and logging, making use of application performance monitoring (APM), either through Stackdriver or through a third-party solution to deliver near real-time insights into service health under real production loads, 24/7.</p><p class="dmb-u-m-b-s">The provisioning of GCP projects includes all associated configurations (like VPC networking, billing account, and Cloud Identity and Access Management policies) and is performed programmatically via Deployment Manager or Hashicorp Terraform, based on a limited set of inputs like cost center, data sensitivity, team ownership, and dependency with services hosted in other GCP projects.</p>',
        LEVEL_4: '<p class="dmb-u-m-b-s">Production VMs allow shell access in break-glass scenarios for debugging purposes only. Self-managed services are replaced with managed equivalents (for example, Cloud SQL, Cloud Memorystore) or serverless/SaaS alternatives, where feasible, to minimize the operations overhead of IaaS-based services.</p><p class="dmb-u-m-b-s">The risk of change is considered to be low. Deployments to production environments are executed programmatically and automatically, using phased strategies (canary, blue/green, and so on).</p><p class="dmb-u-m-b-s">Logging and monitoring are comprehensive and cover every service-level indicator that underpins each service-level objective.</p><p class="dmb-u-m-b-s">All cloud resources are provisioned programmatically via Deployment Manager, Hashicorp Terraform, or directly via GCP’s RESTful APIs. Entire production environments can be (re)created within minutes in another zone or region.</p>',
    },
    DIMENSION_SECURE: {
        LEVEL_0: '<p class="dmb-u-m-b-s">User identities manifest themselves as Google Cloud Identity accounts under an organization domain name, and all consumer accounts for Google Analytics, Adwords, Play, YouTube, etc. are now under the control of the enterprise. These identities are not yet synchronized with the organization’s central identity solution, e.g., Microsoft Active Directory, and therefore not governed by a single source of truth.</p><p class="dmb-u-m-b-s">Cloud IAM policies predominantly rely on the convenience of project-level Primitive Roles (Owner, Editor, Viewer) rather than following the principle of least privilege. Default permissions allow for any user to create GCP projects and billing accounts. Cloud IAM permissions are not continuously monitored with tools like Forseti Security, and the GCP Admin Activity and Data Access logs are not systematically audited. Service accounts can be created freely, and private keys for service accounts are not automatically rotated.</p><p class="dmb-u-m-b-s">An overreliance is placed on the network to establish a secure logical perimeter around all hosted data and applications: firewalls are used as a critical component to restrict access based on contextual information like the IP address of the client or the port of the application. Communication between clouds and data centers is encrypted using virtual private network (VPN) tunnels by default, with little regard to the efficacy of inter-application encryption using Transport Layer Security (TLS). VPC Service Controls are enforced around fully managed GCP services like Cloud Storage and BigQuery as a matter of principled policy, rather than based on the sensitivity of the data.</p>',
        LEVEL_1: '<p class="dmb-u-m-b-s">User identities manifest themselves as Google Cloud Identity accounts under an organization domain name, and all consumer accounts for Google Analytics, Adwords, Play, YouTube, etc. are now under the control of the enterprise. These identities are not yet synchronized with the organization’s central identity solution, e.g., Microsoft Active Directory, and therefore not governed by a single source of truth.</p><p class="dmb-u-m-b-s">Cloud IAM policies predominantly rely on the convenience of project-level Primitive Roles (Owner, Editor, Viewer) rather than following the principle of least privilege. Default permissions allow for any user to create GCP projects and billing accounts. Cloud IAM permissions are not continuously monitored with tools like Forseti Security, and the GCP Admin Activity and Data Access logs are not systematically audited. Service accounts can be created freely, and private keys for service accounts are not automatically rotated.</p><p class="dmb-u-m-b-s">An overreliance is placed on the network to establish a secure logical perimeter around all hosted data and applications: firewalls are used as a critical component to restrict access based on contextual information like the IP address of the client or the port of the application. Communication between clouds and data centers is encrypted using virtual private network (VPN) tunnels by default, with little regard to the efficacy of inter-application encryption using Transport Layer Security (TLS). VPC Service Controls are enforced around fully managed GCP services like Cloud Storage and BigQuery as a matter of principled policy, rather than based on the sensitivity of the data.</p>',
        LEVEL_2: '<p class="dmb-u-m-b-s">User identities are synchronized to Google Cloud Identity from a directory service like Active Directory or OpenLDAP, thereby maintaining a single source of truth and a simpler governance model. Users are authenticated either with the same synchronized password or via a third-party single sign-on (SSO) service. 100% of all user accounts use two-step verification (e.g., SMS or code generator app) to defend against phishing attacks, albeit not with a hardware security key.</p><p class="dmb-u-m-b-s">Cloud IAM policies reference a much more granular set of predefined roles, rather than the coarse primitive roles. The Project Creator and Billing Account Creator roles have been removed from the organization level to ensure a basic degree of cloud resource governance.</p><p class="dmb-u-m-b-s">The network-based security perimeter (VPC) is augmented by additional security layers that protect individual services, for example, via Google’s global Cloud Load Balancing with TLS configured, Cloud Identity-Aware Proxy, and Cloud Armor. This, in turn, lowers the risk profile of exposing a private service to the public internet.</p>',
        LEVEL_3: '<p class="dmb-u-m-b-s">User identities are synchronized to Google Cloud Identity from a directory service like Active Directory or OpenLDAP, thereby maintaining a single source of truth and a simpler governance model. Users are authenticated either with the same synchronized password or via a third-party single sign-on (SSO) service. 100% of all user accounts use two-step verification (e.g., SMS or code generator app) to defend against phishing attacks, albeit not with a hardware security key.</p><p class="dmb-u-m-b-s">Cloud IAM policies reference a much more granular set of predefined roles, rather than the coarse primitive roles. The Project Creator and Billing Account Creator roles have been removed from the organization level to ensure a basic degree of cloud resource governance.</p><p class="dmb-u-m-b-s">The network-based security perimeter (VPC) is augmented by additional security layers that protect individual services, for example, via Google’s global Cloud Load Balancing with TLS configured, Cloud Identity-Aware Proxy, and Cloud Armor. This, in turn, lowers the risk profile of exposing a private service to the public internet.</p>',
        LEVEL_4: '<p class="dmb-u-m-b-s">All service-to-service communication is authenticated and authorized. Little trust is placed in the circumstance that they might share the same virtual private cloud (VPC) and/or VPN. For that same reason, internal firewall rules don’t allow for specific IP addresses or ranges but rather for specific service accounts.</p><p class="dmb-u-m-b-s">A comprehensive understanding of the contents of all your data stores provides the threat profiles for which you can design your security and data governance models, considering scenarios of both unauthorized and inappropriate access.</p><p class="dmb-u-m-b-s">100% of all user accounts use a hardware security key as their second factor to effectively defend against phishing attacks. SMS and code generator apps are understood to be insufficiently safe.</p><p class="dmb-u-m-b-s">GCP Admin Activity and Data Access logs are regularly audited through Stackdriver and automatic alerts have been configured to watch for patterns that match your threat profile. Cloud IAM permissions and firewall rules are continuously monitored and corrected with tools like Forseti Security.</p>',
    },
}


CLOUD_CENTER_EXCELLENCE_URL = 'https://services.google.com/fh/files/misc/cloud_center_of_excellence.pdf'

GCP_TRAINING_CTA = {
    'text': 'GCP training',
    'link': 'https://cloud.google.com/training/',
}

EXECUTIVE_SPONSORSHIP_CTA = {
    'text': 'Strong Executive Sponsorship',
    'link': CLOUD_CENTER_EXCELLENCE_URL,
}

TEAM_STRUCTURE_CTA = {
    'text': 'Staffing the Team',
    'link': CLOUD_CENTER_EXCELLENCE_URL,
}

GOALS_CTA = {
    'text': 'Site Reliability Engineering',
    'link': 'https://landing.google.com/sre/',
}

CLOUD_FUNDING_CTA = {
    'text': 'Cloud Center Of Excellence',
    'link': CLOUD_CENTER_EXCELLENCE_URL,
}

CROSS_FUNCTIONAL_COLLAB_CTA = {
    'text': 'Engaging with the Organization',
    'link': CLOUD_CENTER_EXCELLENCE_URL,
}

CONTINUOUS_DELIVERY_CTA = {
    'text': 'Continuous Delivery',
    'link': 'https://cloud.google.com/solutions/continuous-delivery/'
}

CICD_CTA = {
    'text': 'CI/CD Tools',
    'link': 'https://cloud.google.com/docs/ci-cd/'
}

CREATING_MANAGING_LABELS_CTA = {
    'text': 'Creating and Managing Labels',
    'link': 'https://cloud.google.com/resource-manager/docs/creating-managing-labels'
}

MONITORING_CTA = {
    'text': 'Monitoring',
    'link': 'https://landing.google.com/sre/workbook/chapters/monitoring/'
}

MICROSERVICES_CTA = {
    'text': 'Microservices',
    'link': 'https://medium.freecodecamp.org/decentralize-your-application-with-google-cloud-platform-7149ec6d0255'
}

AUTOSCALING_CTA = {
    'text': 'Autoscaling',
    'link': 'https://cloud.google.com/compute/docs/autoscaler/',
}

BILLING_REPORTS_CTA = {
    'text': 'View Your Cost Trends With Billing Reports',
    'link': 'https://cloud.google.com/billing/docs/how-to/reports',
}

COMMITTED_USE_DISCOUNTS_CTA = {
    'text': 'Committed Use Discounts',
    'link': 'https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts',
}

TWELVE_FACTOR_APP_CTA = {
    'text': 'The Twelve-Factor App',
    'link': 'https://12factor.net/',
}

CLOUD_IDENTITY_MANAGEMENT_CTA = {
    'text': 'Cloud Identity & Access Management',
    'link': 'https://cloud.google.com/iam/docs/concepts#best-practices',
}

TRUST_SECURITY_CTA = {
    'text': 'Trust & Security',
    'link': 'https://cloud.google.com/security/',
}

SECURITY_GOVERNANCE_CTA = {
    'text': 'Security & Governance',
    'link': 'https://cloud.google.com/big-data/security-governance/',
}

CUSTOMER_ENCRYPTION_KEYS_CTA = {
    'text': 'Customer Managed Encryption Keys',
    'link': 'https://cloud.google.com/storage/docs/encryption/customer-managed-keys',
}


DIMENSION_RECOMMENDATIONS = {
    DIMENSION_LEARN: {
        LEVEL_0: [
            {
                'header': 'Talent and Hiring',
                'text': 'Secure headcount and publish new job descriptions for cloud-related roles. Actively start hiring to bring on staff with prior cloud experience. Use third parties for some cloud work and to cover for cloud-specific knowledge gaps.',
            },
            {
                'header': 'Training Resources',
                'text': 'Provide staff with on-demand training courses and hands-on labs. Secure and align budget for training classes and certifications.',
                'cta': GCP_TRAINING_CTA,
            },
            {
                'header': 'Training Goals and Measurement',
                'text': 'Create a training plan that includes required training and certifications for any IT role that is directly or indirectly responsible for contributing to a successful cloud adoption. Include training goals for each team.',
            },
        ],
        LEVEL_1: [
            {
                'header': 'Talent and Hiring',
                'text': 'Secure headcount and publish new job descriptions for cloud-related roles. Actively hire to bring on staff with prior cloud experience. Use third parties to provide specialist knowledge and give them moderated "break glass" admin access.',
            },
            {
                'header': 'Training Resources',
                'text': 'Provide staff with on-demand training courses and labs. Schedule instructor-led training options. and make them available to staff. Align budget for cloud certifications. Create a mechanism for each IT staff member to be provisioned with a sandbox project to experiment with.',
                'cta': GCP_TRAINING_CTA,
            },
            {
                'header': 'Training Goals and Measurement',
                'text': 'Distribute a training plan that includes required training and certifications for any IT role who is directly or indirectly responsible for contributing to a successful cloud adoption. Include training goals for each team. and create a mechanism for consistent tracking and reporting.',
            },
        ],
        LEVEL_2: [
            {
                'header': 'Talent and Hiring',
                'text': 'In addition to new job postings, review existing roles and redefine them to reflect new requirements of a cloud-first IT organization. Begin transition of admin access from third-party partners to internal operations teams, using third parties as staff augmentation functions only.',
            },
            {
                'header': 'Training Resources',
                'text': 'In addition to on-demand and instructor-led options, create platforms for peer-to-peer knowledge sharing such as wikis or internal knowledge bases.If not already in place, create a mechanism for each IT staff member to be provisioned with a sandbox project to experiment with.',
                'cta': GCP_TRAINING_CTA,
            },
            {
                'header': 'Training Goals and Measurement',
                'text': 'In addition to team-level targets that are consistently reported in your organization, encourage individuals to self-assess their level of completion against published targets specific to their roles. Track and reward the cloud certifications individuals achieve.',
            },
        ],
        LEVEL_3: [
            {
                'header': 'Talent and Hiring',
                'text': 'In addition to new job postings, review existing roles and redefine them to reflect new requirements of a cloud-first IT organization. Transition admin access from third-party partners to internal operations teams, using third parties as staff augmentation functions only.',
            },
            {
                'header': 'Training Resources',
                'text': 'In addition to on-demand, instructor-led, and static peer-to-peer learning options, encourage and reward employee-hosted events such as tech talks and hackathons. If not already in place, create a mechanism for each IT staff member to be provisioned with a sandbox project to experiment with.',
                'cta': GCP_TRAINING_CTA,
            },
            {
                'header': 'Training Goals and Measurement',
                'text': 'In addition to team-level targets that are consistently reported in your organization, formalize role-specific assessments for individuals on a periodic basis.',
            },
        ],
        LEVEL_4: [
            {
                'header': 'Talent and Hiring',
                'text': 'Ensure all roles and responsibilities have been redefined (updated?) to reflect the new requirements of a cloud-first IT organization.',
            },
            {
                'header': 'Training Resources',
                'text': 'Continue to provide on-demand, instructor-led, and static peer-to-peer options as well as proactive learning resources via employee-hosted events such as tech talks and hackathons. Encourage staff to produce public blog articles and engage in public speaking engagements.',
                'cta': GCP_TRAINING_CTA,
            },
            {
                'header': 'Training Goals and Measurement',
                'text': 'Continue to track, reward, and report on team-level targets and role-specific assessments for individuals on a periodic basis.',
            },
        ],
    },
    DIMENSION_LEAD: {
        LEVEL_0: [
            {
                'header': 'Executive Sponsorship',
                'text': 'Identify executive sponsor for the project. Secure sponsorship from at least one line of business.',
                'cta': EXECUTIVE_SPONSORSHIP_CTA,
            },
            {
                'header': 'Team Structure and Governance',
                'text': 'Enable teams to learn cloud technologies and encourage cross-organizational collaboration. Gain agreement to Initiate an effort to build a Cloud Center of Excellence to drive cloud adoption. Begin to define and publish governance standards required to comply with industry norms such as PCI DSS, HIPAA and others.',
                'cta': TEAM_STRUCTURE_CTA,
            },
            {
                'header': 'Goals and Measurement',
                'text': 'Build, deploy and put into production one or more workloads to showcase cloud readiness.',
                'cta': GOALS_CTA,
            },
            {
                'header': 'Cloud Funding',
                'text': 'Secure dedicated cloud funding for relevant and critical projects.',
                'cta': CLOUD_FUNDING_CTA,
            },
            {
                'header': 'Cross-Functional Collaboration',
                'text': 'Share best practices, templates, and procedures with other teams on an as-needed basis.',
                'cta': CROSS_FUNCTIONAL_COLLAB_CTA,
            },
        ],
        LEVEL_1: [
            {
                'header': 'Executive Sponsorship',
                'text': 'Identify the right executive sponsor who can be the face of the project and can positively influence stakeholders. Provide behind-the-scenes assistance to sponsors to drive sponsorship from one or more C-level executives.',
                'cta': EXECUTIVE_SPONSORSHIP_CTA,
            },
            {
                'header': 'Team Structure and Governance',
                'text': 'Build and deploy Cloud Center of Excellence to drive and support multiple cloud projects. Enforce governance by implementing preventive and reactive controls to avoid compliance issues.',
                'cta': TEAM_STRUCTURE_CTA,
            },
            {
                'header': 'Goals and Measurement',
                'text': 'In addition to having production workloads, begin to implement SRE best practices such as service-level objectives across workloads.',
                'cta': GOALS_CTA,
            },
            {
                'header': 'Cloud Funding',
                'text': 'In addition to project-based funding, formulate a roadmap to secure funding for R&D.',
                'cta': CLOUD_FUNDING_CTA,
            },
            {
                'header': 'Cross-Functional Collaboration',
                'text': 'Ensure teams collaborate on a regular basis and have a formalized way of sharing best practices, templates, and documentation.',
                'cta': CROSS_FUNCTIONAL_COLLAB_CTA,
            },
        ],
        LEVEL_2: [
            {
                'header': 'Executive Sponsorship',
                'text': 'In addition to driving sponsorship, enable sponsor to build and drive a shared roadmap for cloud adoption/migration strategy. Build momentum to ensure sponsorship is championed by most of the C-level executives.',
                'cta': EXECUTIVE_SPONSORSHIP_CTA,
            },
            {
                'header': 'Team Structure and Governance',
                'text': 'Use the Cloud Center Of Excellence to align your organization and implement best practices. Introduce cloud-centric IT roles to support cloud projects across the organization. Empower governance teams to refine controls as your organization continues to mature in cloud.',
                'cta': TEAM_STRUCTURE_CTA,
            },
            {
                'header': 'Goals and Measurement',
                'text': 'Implement SRE best practices and begin to analyze and define key performance indicators to evalute your success in the cloud.',
                'cta': GOALS_CTA,
            },
            {
                'header': 'Cloud Funding',
                'text': 'Begin to decommission on-premise infrastructure to offset cloud spend.',
                'cta': CLOUD_FUNDING_CTA,
            },
            {
                'header': 'Cross-Functional Collaboration',
                'text': 'Encourage team members to collaborate and share best practices across the organization to drive cross-functional projects.',
                'cta': CROSS_FUNCTIONAL_COLLAB_CTA,
            },
        ],
        LEVEL_3: [
            {
                'header': 'Executive Sponsorship',
                'text': 'Strive for comprehensive C-level sponsorship across the board to set the tone for a culture of cloud-first adoption and experimentation/innovation within teams.',
                'cta': EXECUTIVE_SPONSORSHIP_CTA,
            },
            {
                'header': 'Team Structure and Governance',
                'text': '"Nurture the Cloud Center Of Excellence to drive innovation along with day-to-day cloud projects. Ensure cloud centric IT roles are in place and give projects full autonomy to drive, manage and govern themselves. In additon to implementing and refining governance controls, enable auditors to generate and view on-demand compliance reports.',
                'cta': TEAM_STRUCTURE_CTA,
            },
            {
                'header': 'Goals and Measurement',
                'text': 'In addition to implementing SRE best practices and KPI\'s, ensure teams have an effective and efficient way to report them on an as-needed basis.',
                'cta': GOALS_CTA,
            },
            {
                'header': 'Cloud Funding',
                'text': 'Reduce on-premise footprint to legacy applications so that on-premise spend is approved only where justified. On-premises spend only where justified.',
                'cta': CLOUD_FUNDING_CTA,
            },
            {
                'header': 'Cross-Functional Collaboration',
                'text': 'Strive to build an internal knowledge repository driven by strong collaboration with a sense of ownership for maintaining and developing best practices.',
                'cta': CROSS_FUNCTIONAL_COLLAB_CTA,
            },
        ],
        LEVEL_4: [
            {
                'header': 'Executive Sponsorship',
                'text': 'Continue to drive sponsorship from C-level executives across the board to become a cloud-first organization and to drive innovation by fostering a culture of R&D projects within teams.',
                'cta': EXECUTIVE_SPONSORSHIP_CTA,
            },
            {
                'header': 'Team Structure and Governance',
                'text': 'Continue to grow the Cloud Center Of Excellence to drive innovation and R&D practices across the organization. Continue to mature cloud centric IT roles and ensure all project teams are able to function on their own. Continue to refine and implement governance controls and reports to be fully compliant with ever increasing industry regulations.',
                'cta': TEAM_STRUCTURE_CTA,
            },
            {
                'header': 'Goals and Measurement',
                'text': 'Continue to exercise Disaster and Recovery Testing (DiRT) drills wherein SREs push production systems to the limit and inflict actual outages in order to ensure that systems react as expected and to figure out ways to make the systems more robust in order to prevent uncontrolled outages by exposing unexpected weaknesses.',
                'cta': GOALS_CTA,
            },
            {
                'header': 'Cloud Funding',
                'text': 'Secure cloud funding to continue building and deploying applications using cloud native products and services, moving IT to a zero infrastructure footprint.',
                'cta': CLOUD_FUNDING_CTA,
            },
            {
                'header': 'Cross-Functional Collaboration',
                'text': 'Continue to embrace a thriving and collaborative culture across the organization to drive innovation.',
                'cta': CROSS_FUNCTIONAL_COLLAB_CTA,
            },
        ],
    },
    DIMENSION_SCALE: {
        LEVEL_0: [
            {
                'header': 'Provisioning Services',
                'text': 'Start to provision some cloud services such as compute, storage, identity and access management with scripting. Develop formal standards and create a programmatic provisioning plan for all project foundation components.',
                'cta': CONTINUOUS_DELIVERY_CTA,
            },
            {
                'header': 'Integration and Deployment',
                'text': 'Create testing & change management plans with risk profiles defined. Ensure standardized automation tooling and scripts for testing and changes in environments.',
                'cta': CICD_CTA,
            },
            {
                'header': 'Capacity Planning',
                'text': 'Establish a formal cloud capacity planning plan within your organization and review this quarterly both internally and with your cloud team. Make use of labeling instances to better understand consumption by workload or other dimensions such as environment type.',
                'cta': CREATING_MANAGING_LABELS_CTA,
            },
            {
                'header': 'Monitoring and Logging',
                'text': 'Define SLOs for each application and service. Align cloud service metrics with SLO requirements and then create a monitoring & logging capabilities plan. Ensure near-real time data is available 24/7.',
                'cta': MONITORING_CTA,
            },
            {
                'header': 'Application Architecture',
                'text': 'Start to break down monolithic applications and systems into modules, providing a better structure for development. Start by separating stateful and stateless workloads to allow independent horizontal scaling. Set up configuration data to only be stored in memory in VMs and in discrete services outside VMs. Experiment with the use of containers and immutable VMs.',
                'cta': MICROSERVICES_CTA,
            },
        ],
        LEVEL_1: [
            {
                'header': 'Provisioning Services',
                'text': 'Start to provision some cloud services such as compute, storage, identity and access management with scripting. Develop formal standards and create a programmatic provisioning plan for all project foundation components.',
                'cta': CONTINUOUS_DELIVERY_CTA,
            },
            {
                'header': 'Integration and Deployment',
                'text': 'Build a plan to implement rolling updates using automation on production environments, during a maintenance window if necessary. Establish rigorous change management protocols creating risk-gradation strategies like canary or blue/green deployments for an automated deployment process.',
                'cta': CICD_CTA,
            },
            {
                'header': 'Capacity Planning',
                'text': 'Establish a formal cloud capacity planning plan within your organization and review this quarterly both internally and with your cloud team. Make use of labeling instances to better understand consumption by workload or other dimensions such as environment type. Use autoscale for production workloads based on simple utilization metrics such as CPU/RAM.',
                'cta': AUTOSCALING_CTA,
            },
            {
                'header': 'Monitoring and Logging',
                'text': 'Define SLOs for each application and service. Align cloud service metrics with SLO requirements and then create a monitoring & logging capabilities plan.',
                'cta': MONITORING_CTA,
            },
            {
                'header': 'Application Architecture',
                'text': 'Decide on workloads to deploy using containers and short lived VM\'s based on workload characteristics. Modularize at least one existing or new application such that each of the individual components is self contained and individually deployable. Build an application architecture plan for refactoring existing monolithic applications into modules.',
                'cta': MICROSERVICES_CTA,
            },
        ],
        LEVEL_2: [
            {
                'header': 'Provisioning Services',
                'text': 'Automation should be in place for the full deployment lifecycle of at least one project. Build a consistent approach across all project teams including standardized tooling. Implement formal standards and a programmatic provisioning of all project foundation components.',
                'cta': CONTINUOUS_DELIVERY_CTA,
            },
            {
                'header': 'Integration and Deployment',
                'text': 'Create continuous code deployment schedules based on risk profiles. Introduce canary or blue/green deployment strategies with manual transition between current and new versions; working towards the situation where a formal maintenance window is no longer required. Aim to have limited use of traditional build/test/deploy practices and more standard CI/CD tooling.',
                'cta': CICD_CTA,
            },
            {
                'header': 'Capacity Planning',
                'text': 'Review your formal capacity plan based on your business cycles, seasonality, and other expected impacts on cloud capacity needs. Build custom reports against billing and utilization data for ongoing analysis of spend and opportunities to optimize costs. Use autoscale for production workloads based on a combination of simple utilization metrics such as CPU/RAM and application specific metrics. Proactively leverage Committed Use Discounts for steady state workloads.',
                'cta': BILLING_REPORTS_CTA,
            },
            {
                'header': 'Monitoring and Logging',
                'text': 'Embed logging and application performance monitoring in all cloud services across silos and lines of business. Ensure near-real time data is available 24/7.',
                'cta': MONITORING_CTA,
            },
            {
                'header': 'Application Architecture',
                'text': 'Establish application workload standards that incorporate usage of serverless service. Ensure all containers are immutable and have config details embedded in VMs with O/S credentials are locked down. All new applications should be architected using 12-factor principles.',
                'cta': TWELVE_FACTOR_APP_CTA,
            },
        ],
        LEVEL_3: [
            {
                'header': 'Provisioning Services',
                'text': 'Automation should be in place for the full deployment lifecycle of more than one project. Implement formal standards and a programmatic provisioning of all project foundation components. Build a consistent approach to provisioning across all projects including standardized tooling.',
                'cta': CONTINUOUS_DELIVERY_CTA,
            },
            {
                'header': 'Integration and Deployment',
                'text': 'Canary or blue/green deployment strategies or similar should be in use and you should be dynamically transitioning users to the new versions of applications. Make sure that all components can be tested and deployed independently.',
                'cta': CICD_CTA,
            },
            {
                'header': 'Capacity Planning',
                'text': 'Review your formal capacity plan based on your business cycles, seasonality, and other expected impacts on cloud capacity needs. Build custom reports against billing and utilization data for ongoing analysis of spend and opportunities to optimize costs. Use autoscale for production workloads based on a combination of simple utilization metrics such as CPU/RAM and application specific metrics. Proactively leverage Committed Use Discounts for steady state workloads.',
                'cta': COMMITTED_USE_DISCOUNTS_CTA,
            },
            {
                'header': 'Monitoring and Logging',
                'text': 'Ensure that logging and application performance monitoring is comprehensive across all services, aligning with defined SLOs.',
                'cta': MONITORING_CTA,
            },
            {
                'header': 'Application Architecture',
                'text': 'Review all components and ensure that they can be tested and deployed independently. Eliminate application complexity via broad adoption of containers and serverless services, focusing on fit-for-purpose technologies. Data management should be handled primarily by fully managed cloud services and all new applications should be architected using 12-factor principles.',
                'cta': TWELVE_FACTOR_APP_CTA
            },
        ],
        LEVEL_4: [
            {
                'header': 'Provisioning Services',
                'text': 'Review the automation for cloud services provisioning and ensure tooling is standardized across all projects. Applications should be able to be deployed in additional regions and/or zones in a matter of minutes leveraging fully automated deployment tooling.',
                'cta': CONTINUOUS_DELIVERY_CTA,
            },
            {
                'header': 'Integration and Deployment',
                'text': 'Ensure that application changes are considered “low risk” and deployments are fully automated. If not, review the scenarios where there is an exception and build a plan to resolve. ',
                'cta': CICD_CTA,
            },
            {
                'header': 'Capacity Planning',
                'text': 'Review your formal capacity plan based on your business cycles, seasonality, and other expected impacts on cloud capacity needs. Proactively leverage Committed Use Discounts for steady state workloads.',
                'cta': COMMITTED_USE_DISCOUNTS_CTA,
            },
            {
                'header': 'Monitoring and Logging',
                'text': 'Continue to log and monitor comprehensively across all services and applications, aligning with defined SLOs.',
                'cta': MONITORING_CTA,
            },
            {
                'header': 'Application Architecture',
                'text': 'Review all applications against the 12-factor principles and build a plan to retire or refactor legacy applications and systems. Continue broad adoption of containers and serverless services, focusing on fit-for-purpose technologies. Conduct architectural reviews to eliminate complexity in compute needs via adoption of containers, serverless services and fully managed cloud database services',
                'cta': TWELVE_FACTOR_APP_CTA,
            },
        ],
    },
    DIMENSION_SECURE: {
        LEVEL_0: [
            {
                'header': 'User Identity',
                'text': 'Leverage Active Directory and/or LDAP servers as the source of truth for users.',
                'cta': CLOUD_IDENTITY_MANAGEMENT_CTA,
            },
            {
                'header': 'Controls & Policies',
                'text': '"Begin to define and document security controls and processes required to adhere to these controls. Adopt basic governance and risk management process and policies. Use the security principle of least privilege to grant IAM roles, that is, only give the least amount of access necessary to your resources. Enhance network-based security perimeter by verifying user identity in the context of a request.',
                'cta': TRUST_SECURITY_CTA,
            },
            {
                'header': 'Governance',
                'text': 'Leverage common set of identity policies, audit and enforcement procedures to analyze logs and reports to validate user and service account compliance. Develop controls to support centralized user and service account provisioning with critical features such as initial password and key vaulting, integrated logging, etc. Classify data access strategy.',
                'cta': SECURITY_GOVERNANCE_CTA,
            },
            {
                'header': 'Encryption',
                'text': 'Ensure keys are stored and secured locally on-premises using a safe vault. Rotate keys at regular intervals (manually or using an automated process).',
                'cta': CUSTOMER_ENCRYPTION_KEYS_CTA,
            },
        ],
        LEVEL_1: [
            {
                'header': 'User Identity',
                'text': 'In addition to leveraging active directory, define standards and protocols to manage and map user identities between identity providers across organizations. All user and system account access within cloud environments should be based around self describing groups.',
                'cta': CLOUD_IDENTITY_MANAGEMENT_CTA,
            },
            {
                'header': 'Controls & Policies',
                'text': 'Build and document security controls. Validate organization-wide security processes and policies. Expand network-based security parameter by verifying the service identity in the context of request along with the user identity.',
                'cta': TRUST_SECURITY_CTA,
            },
            {
                'header': 'Governance',
                'text': 'Enforce 2FA/MFA requirement for privileged accounts. Develop auditing and enforcement policies and processes. Enforce standard set of policies and controls to prevent unauthorized access.',
                'cta': SECURITY_GOVERNANCE_CTA,
            },
            {
                'header': 'Encryption',
                'text': 'Leverage Customer-Managed Encryption Keys (CMEK) wherever possible. Ensure manual process and tooling is in place to rotate the encryption keys along with a regular rotation schedule.',
                'cta': CUSTOMER_ENCRYPTION_KEYS_CTA,
            },
        ],
        LEVEL_2: [
            {
                'header': 'User Identity',
                'text': 'Leverage cloud-based user directory or identity provider as unified source of truth with centralized provisioning/deprovisioning of users based on on-boarding/termination of users and/or system accounts.',
                'cta': CLOUD_IDENTITY_MANAGEMENT_CTA,
            },
            {
                'header': 'Controls & Policies',
                'text': 'Actively monitor and measure compliance by implementing a standardized set of security controls across the organization. Formulate information security committees along with validation and measurement processes. Begin to replace existing network-based security perimeter to reduce reliance on VPN(s) for granting secured access to workforce.',
                'cta': TRUST_SECURITY_CTA,
            },
            {
                'header': 'Governance',
                'text': 'Leverage single sign-on as a standardized process to access cloud environments along with automated controls to detect anomalies. Automate risk-based workflows and controls to grant access into cloud environments. Certify and audit access at regular intervals. Provide capability to generate on-demand report to identity violators. Develop preventative and reactive controls to enforce compliance.',
                'cta': SECURITY_GOVERNANCE_CTA,
            },
            {
                'header': 'Encryption',
                'text': 'Leverage Customer-Managed Encryption Keys (CMEK) wherever possible. Ensure manual/automated process and tooling in place to rotate the encryption keys along with a regular and well-documented rotation schedule. Review, audit and certify keys on a regular basis.',
                'cta': CUSTOMER_ENCRYPTION_KEYS_CTA,
            },
        ],
        LEVEL_3: [
            {
                'header': 'User Identity',
                'text': 'Integrate the provisioning and management of users with your enterprise\'s single source of truth for users (e.g. AD) to ensure that when employees join and leave the company the state in Google is consistent.',
                'cta': CLOUD_IDENTITY_MANAGEMENT_CTA,
            },
            {
                'header': 'Controls & Policies',
                'text': 'Implement standardized security controls across the board. Implement a well-defined and comprehensive Security Program to ensure strong defense. Avoid relying on a network-based security perimeter and/or VPN by setting up access controls around individual devices and users (e.g. BeyondCorp).',
                'cta': TRUST_SECURITY_CTA,
            },
            {
                'header': 'Governance',
                'text': 'Develop a fully automated solution to certify cloud access granted to human users and/or service accounts accessing sensitive data. Provide reporting capabilities to ensure strict compliance. Use the principle of "Just-in-time" access to grant highly-privileged access for user and service accounts. Develop real time auditing and alerting controls to detect anomalies. Strive for fully automated preventative controls and anomaly detection along with proactive monitoring, audit and access review certification systems/processes.',
                'cta': SECURITY_GOVERNANCE_CTA,
            },
            {
                'header': 'Encryption',
                'text': 'Leverage Customer-Managed Encryption Keys (CMEK). Ensure fully automated key rotation service is in place to rotate keys at regular intervals. Review, audit and certify keys and provide an on-demand reporting capability to ensure strict compliance.',
                'cta': CUSTOMER_ENCRYPTION_KEYS_CTA,
            },
        ],
        LEVEL_4: [
            {
                'header': 'User Identity',
                'text': 'Continue to improve the user management process to provide great user experience along with an on-demand dashboard view to validate user access details.',
                'cta': CLOUD_IDENTITY_MANAGEMENT_CTA,
            },
            {
                'header': 'Controls & Policies',
                'text': 'Continue to improve the standardized set of security controls. Mature security programs to tackle complex access and data breach scenarios. Strive to implement zero trust security across the organization.',
                'cta': TRUST_SECURITY_CTA,
            },
            {
                'header': 'Governance',
                'text': 'Continue to mature existing controls and process to provide heightened security across the organization.',
                'cta': SECURITY_GOVERNANCE_CTA,
            },
            {
                'header': 'Encryption',
                'text': 'Continue to leverage Customer-Managed Encryption Keys (CMEK) along with a fully-automated rotation schedule ensuring strict compliance across the board. Additionally, continue to mature dashboard capabilities to provide an interactive view for auditors to review and detect anomalies.',
                'cta': CUSTOMER_ENCRYPTION_KEYS_CTA,
            },
        ],
    },
}

DIMENSION_SIDEPANEL_HEADING = 'We measure cloud maturity across four themes that define the foundation of cloud readiness. An organization\'s readiness for success in the cloud is determined by current business practices in each of these four themes. More information on the themes of cloud maturity can be found in the <a class="h-c-inline-link" href="https://cloud.google.com/adoption-framework/">Google Cloud Adoption Framework</a> whitepaper.'

DIMENSION_SIDEPANEL_DESCRIPTIONS = {
    DIMENSION_LEARN: 'The quality and scale of the learning programs in place to upskill technical teams, and the ability to augment IT staff with experienced partners.',
    DIMENSION_LEAD: 'The extent to which IT teams are supported by a mandate from leadership to migrate to the cloud, and the degree in which the teams themselves are cross-functional, collaborative, and self-motivated.',
    DIMENSION_SCALE: 'The extent to which cloud-native services are used that reduce operational overhead and automate manual processes and policies.',
    DIMENSION_SECURE: 'The capability to protect services from unauthorized and inappropriate access with a multilayered, identity-centric security model.',
}


CONTENT_DATA = {
    'levels': LEVELS,
    'levels_max': LEVELS_MAX,
    'level_descriptions': LEVELS_DESCRIPTIONS,
    'report_level_descriptions': REPORT_LEVEL_DESCRIPTIONS,
    'dimensions': DIMENSION_ORDER,
    'dimension_labels': DIMENSION_TITLES,
    'dimension_header_descriptions': DIMENSION_HEADER_DESCRIPTIONS,
    'dimension_level_description': DIMENSION_LEVEL_DESCRIPTION,
    'dimension_recommendations': DIMENSION_RECOMMENDATIONS,
    'industry_avg_description': INDUSTRY_AVG_DESCRIPTION,
    'industry_best_description': INDUSTRY_BEST_DESCRIPTION,
    'dimension_sidepanel_heading': DIMENSION_SIDEPANEL_HEADING,
    'dimension_sidepanel_descriptions': DIMENSION_SIDEPANEL_DESCRIPTIONS,
    'subdimensions': SUBDIMENSION_ORDER,
    'subdimension_labels': SUBDIMENSION_TITLES,
}

#####  GOOGLE SHEETS EXPORT TENANT CUSTOMIZATION #####
GOOGLE_SHEET_EXPORT_SURVEY_FIELDS = GOOGLE_SHEET_BASE_SURVEY_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS = GOOGLE_SHEET_BASE_RESULT_FIELDS.copy()
GOOGLE_SHEET_EXPORT_RESULT_FIELDS.update(DIMENSION_TITLES)
#####  END OF GOOGLE SHEETS EXPORT TENANT CUSTOMIZATION #####
