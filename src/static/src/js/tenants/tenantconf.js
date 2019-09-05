import {TenantConfiguration} from './tenantconf.class';

/** @const {string} */
const MODULE_NAME = 'tenant';

/** @const {string} */
const SERVICE_NAME = 'tenantConf';

/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);

// Angular Wrapping the standard class
module.service(SERVICE_NAME, TenantConfiguration);
