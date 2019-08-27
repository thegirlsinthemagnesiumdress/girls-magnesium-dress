goog.module.declareNamespace('dmb.components.tenant');

const tenantDataElementName = 'bootstrap-data';

/** @const {string} */
const MODULE_NAME = 'tenant';

/** @const {string} */
const SERVICE_NAME = 'tenantConf';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);

/**
 * Tenant conf class
 */
class TenantConfiguration {
  /**
   *
   */
  constructor() {
    /**
     * @type string
     * @export
     */
    this.tenant = '';

    /**
     * @type {Object}
     * @export
     */
    this.levels = {};

    /**
     * @type {string}
     * @export
     */
    this.levelsMax = '';

    /**
     * @type {Object}
     * @export
     */
    this.levelDescriptions = {};

    /**
     * @type {Object}
     * @export
     */
    this.reportLevelDescriptions = {};

    /**
     * @type {Array}
     * @export
     */
    this.dimensionList = [];

    /**
     * @type {Object}
     * @export
     */
    this.dimensionTitles = {};

    /**
     * @type {Object}
     * @export
     */
    this.dimensionHeaderDescriptions = {};

    /**
     * @type {Object}
     * @export
     */
    this.dimensionLevelDescription = {};

    /**
     * @type {Object}
     * @export
     */
    this.dimensionRecommendations = {};

    /**
     * @type {Object}
     * @export
     */
    this.industryAvgDescription = null;

    /**
     * @type {Object}
     * @export
     */
    this.industryBestDescription = null;

    /**
     * @type {Object}
     * @export
     */
    this.contentData = {};

    /**
     * @type {string}
     * @export
     */
    this.dimensionSidepanelHeading = '';

    /**
     * @type {Object}
     * @export
     */
    this.subdimensions = {};

    /**
     * @type {Object}
     * @export
     */
    this.subdimensionLists = {};

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportHeading = '';

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportDescription = '';

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportCta = '';

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportSubheading = '';

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsSidepanelHeading = '';

    /**
     * @type {Object}
     * @export
     */
    this.subdimensionNames = {};

    /**
     * @type {Object}
     * @export
     */
    this.subdimensionDescriptions = {};


    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];

    this.contentData = JSON.parse(tenantDataElement.dataset['contentData']);

    this.levels = this.contentData['levels'];
    this.levelsMax = this.contentData['levels_max'];
    const levelKeys = Object.keys(this.levels);
    this.levelsTotal = levelKeys.length;
    this.levelsArray = levelKeys.sort();
    this.levelDescriptions = this.contentData['level_descriptions'];
    this.reportLevelDescriptions = this.contentData['report_level_descriptions'];

    this.dimensionList = this.contentData['dimensions'];
    this.dimensionTitles = this.contentData['dimension_titles'];
    this.dimensionHeaderDescriptions = this.contentData['dimension_header_descriptions'];
    this.dimensionLevelDescription = this.contentData['dimension_level_description'];
    this.dimensionRecommendations = this.contentData['dimension_recommendations'];
    this.industryAvgDescription = this.contentData['industry_avg_description'];
    this.industryBestDescription = this.contentData['industry_best_description'];
    this.dimensionSidepanelHeading = this.contentData['dimension_sidepanel_heading'];
    this.dimensionSidepanelDescriptions = this.contentData['dimension_sidepanel_descriptions'];

    this.subdimensionLists = this.contentData['subdimension_lists'];
    if (this.subdimensionLists) {
      this.subdimensionsReportHeading = this.contentData['subdimensions_report_heading'];
      this.subdimensionsReportSubheading = this.contentData['subdimensions_report_subheading'];
      this.subdimensionsReportDescription = this.contentData['subdimensions_report_description'];
      this.subdimensionsReportCta = this.contentData['subdimensions_report_cta'];
      this.subdimensionsSidepanelHeading = this.contentData['subdimensions_sidepanel_heading'];

      this.subdimensionNames = this.contentData['subdimension_names'];
      this.subdimensionDescriptions = this.contentData['subdimension_descriptions'];
    }
  }
}


module.service(SERVICE_NAME, TenantConfiguration);
