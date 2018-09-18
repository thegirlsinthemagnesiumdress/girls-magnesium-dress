goog.module('dmb.components.progressTable');

const directive = goog.require('dmb.components.progressTable.directive');


/** @const {string} */
const MODULE_NAME = 'progressTable';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);


/**
 * Progress table angular module.
 * @type {!angular.Module}
 */
exports.module = module;

