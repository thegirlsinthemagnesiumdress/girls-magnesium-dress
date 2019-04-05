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
    this.contentData = {};


    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];

    this.contentData = JSON.parse(tenantDataElement.dataset['recommendations']);

    this.dimensionHeaders = this.contentData['dimension_labels'];
    this.dimensions = this.contentData['dimensions'];
    this.levels = this.contentData['levels'];
    this.levelDescriptions = this.contentData['level_descriptions'];
    this.reportLevelDescriptions = this.contentData['report_level_descriptions'];
    this.dimensionHeadersDescription = this.contentData['dimension_headers_descriptions'];
    this.dimensionLevelDescription = this.contentData['dimension_level_description'];
    this.dimensionLevelRecommendations = this.contentData['dimension_level_recommendations'];
  }
}


module.service(SERVICE_NAME, TenantConfiguration);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
