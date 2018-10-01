goog.module('dmb.components.scroll');

const service = goog.require('dmb.components.scroll.service');
const directive = goog.require('dmb.components.scroll.directive');
const pinTopDirective = goog.require('dmb.components.scroll.pinTopDirective');


/** @const {string} */
const MODULE_NAME = 'scroll';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.factory(service.SERVICE_NAME, service.main);
module.directive(directive.DIRECTIVE_NAME, directive.main);
module.directive(pinTopDirective.DIRECTIVE_NAME, pinTopDirective.main);


/**
 * scroll angular module.
 * @type {!angular.Module}
 */
exports.module = module;
