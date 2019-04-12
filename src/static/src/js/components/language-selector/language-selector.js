goog.module('dmb.components.languageSelector');

const controller = goog.require('dmb.components.languageSelector.controller');


/** @const {string} */
const MODULE_NAME = 'languageSelector';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);


/**
 * Language selector angular module.
 * @type {!angular.Module}
 */
exports.module = module;
