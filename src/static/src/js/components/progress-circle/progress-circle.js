goog.module('dmb.components.progressCircle');

const directive = goog.require('dmb.components.progressCircle.directive');


/** @const {string} */
const MODULE_NAME = 'progressCircle';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);


/**
 * Progress circle angular module.
 * @type {!angular.Module}
 */
exports.module = module;
