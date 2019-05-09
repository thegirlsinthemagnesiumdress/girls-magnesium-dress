goog.module('dmb.components.copyComponent');

const controller = goog.require('dmb.components.copyComponent.controller');


/** @const {string} */
const MODULE_NAME = 'copyComponent';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);


/**
 * Copy component angular module.
 * @type {!angular.Module}
 */
exports.module = module;
