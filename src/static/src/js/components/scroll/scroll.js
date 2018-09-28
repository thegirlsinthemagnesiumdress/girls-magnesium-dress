goog.module('dmb.components.scroll');

const scrollService = goog.require('dmb.components.scroll.service');
const directive = goog.require('dmb.components.scroll.directive');
const pinTopDirective = goog.require('dmb.components.scroll.pinTopDirective');
const smoothScrollDirective = goog.require('dmb.components.scroll.smoothScrollDirective');
const config = goog.require('glue.ng.common.config');
const service = goog.require('glue.ng.smoothScroll.service');



/** @const {string} */
const MODULE_NAME = 'scroll';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, [
  config.module.name,
  service.module.name,
]);


module.factory(scrollService.SERVICE_NAME, scrollService.main);
module.directive(directive.DIRECTIVE_NAME, directive.main);
module.directive(pinTopDirective.DIRECTIVE_NAME, pinTopDirective.main);
module.directive(smoothScrollDirective.DIRECTIVE_NAME, smoothScrollDirective.main);


/**
 * scroll angular module.
 * @type {!angular.Module}
 */
exports.module = module;
