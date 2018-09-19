goog.module('dmb.components.dimensionTab');

const directive = goog.require('dmb.components.dimensionTab.directive');
const {
  dimensionHeaders,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelrecommendations,
} = goog.require('dmb.components.dimensionTab.strings');


/** @const {string} */
const MODULE_NAME = 'dimensionTab';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
module.factory('dimensionHeaders', () => dimensionHeaders);
module.factory('dimensionHeadersDescription', () => dimensionHeadersDescription);
module.factory('dimensionLevelDescription', () => dimensionLevelDescription);
module.factory('dimensionLevelrecommendations', () => dimensionLevelrecommendations);


/**
 * Dimension tab angular module.
 * @type {!angular.Module}
 */
exports.module = module;
