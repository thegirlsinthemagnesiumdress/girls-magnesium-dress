goog.module('dmb.components.sidePanel');

const directive = goog.require('dmb.components.sidePanel.directive');


/** @const {string} */
const MODULE_NAME = 'sidePanel';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
