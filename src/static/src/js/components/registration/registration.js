goog.module('dmb.components.registration');

const controller = goog.require('dmb.components.registration.controller');


/** @const {string} */
const MODULE_NAME = 'registration';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
