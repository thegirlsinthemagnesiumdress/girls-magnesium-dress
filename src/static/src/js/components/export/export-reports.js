goog.module('dmb.components.exportReports');

const controller = goog.require('dmb.components.exportReports.controller');


/** @const {string} */
const MODULE_NAME = 'exportReports';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);


/**
 * Export reports angular module.
 * @type {!angular.Module}
 */
exports.module = module;
