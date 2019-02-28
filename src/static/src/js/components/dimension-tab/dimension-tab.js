goog.module('dmb.components.dimensionTab');

const directive = goog.require('dmb.components.dimensionTab.directive');
const {
  dimensionHeaders,
  dimensionHeadersDescription,
  dimensionLevelDescription,
  dimensionLevelRecommendations,
} = goog.require('dmb.components.dimensionTab.adsStrings');

const {
  dimensionHeaders,
  newsDimensionHeadersDescription,
  newsDimensionLevelDescription,
  newsDimensionLevelRecommendations,
} = goog.require('dmb.components.dimensionTab.newsStrings');


/** @const {string} */
const MODULE_NAME = 'dimensionTab';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);

module.factory('dimensionHeaders', ['tenant', (tenant) => {
  return tenant === 'news' ? newsDimensionHeaders : dimensionHeaders;
}]);
module.factory('dimensionHeadersDescription', ['tenant', (tenant) => {
  return tenant === 'news' ? newsDimensionHeadersDescription : dimensionHeadersDescription;
}]);
module.factory('dimensionLevelDescription', ['tenant', (tenant) => {
  return tenant === 'news' ? newsDimensionLevelDescription : dimensionLevelDescription;
}]);
module.factory('dimensionLevelRecommendations', ['tenant', (tenant) => {
  return tenant === 'news' ? newsDimensionLevelRecommendations : dimensionLevelRecommendations;
}]);


/**
 * Dimension tab angular module.
 * @type {!angular.Module}
 */
exports.module = module;
