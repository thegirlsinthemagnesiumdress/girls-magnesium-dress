goog.module.declareNamespace('dmb.components.exportReports');

import * as controller from './export-reports.controller';


/** @const {string} */
const MODULE_NAME = 'exportReports';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);
