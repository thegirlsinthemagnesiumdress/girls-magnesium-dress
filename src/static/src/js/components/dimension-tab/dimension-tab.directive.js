goog.module.declareNamespace('dmb.components.dimensionTab.directive');

import * as dimensionTabCtrl from '../dimension-tab/dimension-tab.controller';
const dimensionTabTemplateUrl = '/angular/dimension-tab/';

/**
 * Dimension tab directive.
 * @ngInject
 * @param {string} LANGUAGE_CODE
 * @return {Object} Config for the directive
 */
function DimensionTabDirective(LANGUAGE_CODE) {
  return {
    restrict: 'A',
    scope: {
      'companyName': '<',
      'dmbDimensionTab': '<',
      'dimensionResult': '<',
      'dimensionResults': '<',
      'dimensionIndAvg': '<',
      'dimensionIndBest': '<',
      'dimensionIndReady': '<',
      'tenant': '@',
    },
    templateUrl: `/${LANGUAGE_CODE}${dimensionTabTemplateUrl}`,
    controller: dimensionTabCtrl.main,
    controllerAs: dimensionTabCtrl.CONTROLLER_AS_NAME,
    bindToController: true,
  };
}


/** @const {string} */
DimensionTabDirective.DIRECTIVE_NAME = 'dmbDimensionTab';


export const main = DimensionTabDirective;
export const DIRECTIVE_NAME = DimensionTabDirective.DIRECTIVE_NAME;
