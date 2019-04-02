goog.module('dmb.components.tenant');

const confMap = goog.require('dmb.components.tenant.confMap');
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
    this.dimensionHeadersDescription = {};

    /**
     * @type {Object}
     * @export
     */
    this.dimensionLevelDescription = {};

    /**
     * @type {Object}
     * @export
     */
    this.dimensionLevelRecommendations = {};


    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];
    const conf = confMap[this.tenant];
    this.levels = conf.levels;
    this.levelsTotal = Object.keys(this.levels).length;
    this.levelDescriptions = conf.levelDescriptions;
    this.reportLevelDescriptions = conf.reportLevelDescriptions;
    this.dimensions = conf.dimensions;
    this.dimensionHeaders = /** @type {Object} */ (JSON.parse(tenantDataElement.dataset['dimensions']));
    this.dimensionHeadersDescription = conf.dimensionHeadersDescription;
    this.dimensionLevelDescription = conf.dimensionLevelDescription;
    this.dimensionLevelRecommendations = conf.dimensionLevelRecommendations;
  }
}


module.service(SERVICE_NAME, TenantConfiguration);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
