goog.module('dmb.components.reportAdmin');

const directive = goog.require('dmb.components.reportAdmin.directive');

/** @const {string} */
const MODULE_NAME = 'reportAdmin';


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


