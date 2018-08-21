goog.module('dmb.components.scroll');

const service = goog.require('dmb.components.scroll.service');


/** @const {string} */
const MODULE_NAME = 'scroll';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.factory(service.SERVICE_NAME, service.main);


/**
 * scroll angular module.
 * @type {!angular.Module}
 */
exports.module = module;
