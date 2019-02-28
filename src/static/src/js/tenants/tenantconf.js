goog.module('dmb.components.tenant');

const confMap = goog.require('dmb.components.tenant.confMap');

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
    this.tenant = document.documentElement.dataset['tenant'];

    /**
     * @type string[]
     * @export
     */
    this.dimensions = JSON.parse(document.documentElement.dataset['dimensions']);

    /**
     * @type string[]
     * @export
     */
    this.levels = [];

    /**
     * @type string[]
     * @export
     */
    this.dimensionHeaders = [];

    /**
     * @type string[]
     * @export
     */
    this.dimensionHeadersDescription = [];

    /**
     * @type string[]
     * @export
     */
    this.dimensionLevelDescription = [];

    /**
     * @type string[]
     * @export
     */
    this.dimensionLevelRecommendations = [];

    const conf = confMap[this.tenant];

    this.levels = conf.levels;
    this.dimensionHeaders = conf.dimensionHeaders;
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
