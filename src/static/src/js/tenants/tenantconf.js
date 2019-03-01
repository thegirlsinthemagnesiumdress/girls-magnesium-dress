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


    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];
    const conf = confMap[this.tenant];
    this.levels = conf.levels;
    this.levelDescriptions = conf.levelDescriptions;
    this.dimensions = conf.dimensions;
    this.dimensionHeaders = JSON.parse(tenantDataElement.dataset['dimensions']);
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
