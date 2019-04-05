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
     * @param {Object}
     * @export
     */
    this.levels = {};

    /**
     * @param {Object}
     * @export
     */
    this.levelDescriptions = {};

    /**
     * @param {Object}
     * @export
     */
    this.reportLevelDescriptions = {};

    /**
     * @param {Array}
     * @export
     */
    this.dimensions = [];

    /**
     * @param {Object}
     * @export
     */
    this.dimensionHeaders = {};


    /**
     * @param {Object}
     * @export
     */
    this.dimensionHeadersDescription = {};

    /**
     * @param {Object}
     * @export
     */
    this.dimensionLevelDescription = {};

    /**
     * @param {Object}
     * @export
     */
    this.dimensionLevelRecommendations = {};

    /**
     * @param {Object}
     * @export
     */
    this.recommendationsData = {};


    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];

    this.recommendationsData = JSON.parse(tenantDataElement.dataset['recommendations']);

    this.dimensionHeaders = this.recommendationsData['dimension_labels'];
    this.dimensions = this.recommendationsData['dimensions'];
    this.levels = this.recommendationsData['levels'];
    this.levelDescriptions = this.recommendationsData['level_descriptions'];
    this.reportLevelDescriptions = this.recommendationsData['report_level_descriptions'];
    this.dimensionHeadersDescription = this.recommendationsData['dimension_headers_descriptions'];
    this.dimensionLevelDescription = this.recommendationsData['dimension_level_description'];
    this.dimensionLevelRecommendations = this.recommendationsData['dimension_level_recommendations'];
  }
}


module.service(SERVICE_NAME, TenantConfiguration);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
