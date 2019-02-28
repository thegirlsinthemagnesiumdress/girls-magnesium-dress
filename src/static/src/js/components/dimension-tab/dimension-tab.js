goog.module('dmb.components.dimensionTab');

const directive = goog.require('dmb.components.dimensionTab.directive');

/** @const {string} */
const MODULE_NAME = 'dimensionTab';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);


/**
 * Dimension tab angular module.
 * @type {!angular.Module}
 */
exports.module = module;
