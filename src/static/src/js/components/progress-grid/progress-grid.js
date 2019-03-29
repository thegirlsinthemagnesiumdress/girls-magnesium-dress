goog.module('dmb.components.progressGrid');

const directive = goog.require('dmb.components.progressGrid.directive');


/** @const {string} */
const MODULE_NAME = 'progressGrid';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);


/**
 * Progress grid angular module.
 * @type {!angular.Module}
 */
exports.module = module;

