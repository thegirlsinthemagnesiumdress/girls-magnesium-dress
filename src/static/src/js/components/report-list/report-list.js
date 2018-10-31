goog.module('dmb.components.reportList');

const directive = goog.require('dmb.components.reportList.directive');

/** @const {string} */
const MODULE_NAME = 'reportList';


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


