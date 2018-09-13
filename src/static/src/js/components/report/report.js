goog.module('dmb.components.report');

const directive = goog.require('dmb.components.report.directive');


/** @const {string} */
const MODULE_NAME = 'report';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);


/**
 * Report angular module.
 * @type {!angular.Module}
 */
exports.module = module;
