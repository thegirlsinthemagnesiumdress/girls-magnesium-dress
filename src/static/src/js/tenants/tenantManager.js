goog.module('dmb.components.tenantManager');

const service = goog.require('dmb.components.sidePanel.service');


/** @const {string} */
const MODULE_NAME = 'sidePanel';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


class TenantManager(tenant) {
  constructor() {

  }
}


module.service(service.SERVICE_NAME, service.main);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
