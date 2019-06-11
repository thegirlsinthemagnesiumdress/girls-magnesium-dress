goog.module('dmb.components.tenant');

const tenantDataElementName = 'bootstrap-data';

/** @const {string} */
const MODULE_NAME = 'tenant';

/** @const {string} */
const SERVICE_NAME = 'tenantConf';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);

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
     * @type {String}
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
     * @type {Array}
     * @export
     */
    this.dimensions = [];

    /**
     * @type {Object}
     * @export
     */
    this.dimensionHeaders = {};

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
    this.contentData = {};

    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];

    this.contentData = JSON.parse(tenantDataElement.dataset['contentData']);

    this.dimensionHeaders = this.contentData['dimension_labels'];
    this.dimensions = this.contentData['dimensions'];
    this.levels = this.contentData['levels'];
    this.levelsMax = this.contentData['levels_max'];
    this.levelsTotal = Object.keys(this.levels).length;
    this.levelDescriptions = this.contentData['level_descriptions'];
    this.reportLevelDescriptions = this.contentData['report_level_descriptions'];
    this.dimensionHeaderDescriptions = this.contentData['dimension_header_descriptions'];
    this.dimensionLevelDescription = this.contentData['dimension_level_description'];
    this.dimensionRecommendations = this.contentData['dimension_recommendations'];
    this.industryAvgDescription = this.contentData['industry_avg_description'];
    this.industryBestDescription = this.contentData['industry_best_description'];
    this.dimensionSidepanelHeading = this.contentData['dimension_sidepanel_heading'];
    this.dimensionSidepanelDescriptions = this.contentData['dimension_sidepanel_descriptions'];
  }
}


module.service(SERVICE_NAME, TenantConfiguration);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
