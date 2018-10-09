goog.module('dmb.components.sidePanel');

const directive = goog.require('dmb.components.sidePanel.directive');
const triggerDirective = goog.require('dmb.components.sidePanel.triggerDirective');
const service = goog.require('dmb.components.sidePanel.service');


/** @const {string} */
const MODULE_NAME = 'sidePanel';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
module.directive(triggerDirective.DIRECTIVE_NAME, triggerDirective.main);
module.service(service.SERVICE_NAME, service.main);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
