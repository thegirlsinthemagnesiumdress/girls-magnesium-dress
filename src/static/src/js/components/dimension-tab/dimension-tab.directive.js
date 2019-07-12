goog.module('dmb.components.dimensionTab.directive');

const dimensionTabCtrl = goog.require('dmb.components.dimensionTab.controller');
const dimensionTabTemplateUrl = '/angular/dimension-tab/';

/**
 * Dimension tab directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function DimensionTabDirective() {
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
    templateUrl: dimensionTabTemplateUrl,
    controller: dimensionTabCtrl.main,
    controllerAs: dimensionTabCtrl.CONTROLLER_AS_NAME,
    bindToController: true,
  };
}


/** @const {string} */
DimensionTabDirective.DIRECTIVE_NAME = 'dmbDimensionTab';


exports = {
  main: DimensionTabDirective,
  DIRECTIVE_NAME: DimensionTabDirective.DIRECTIVE_NAME,
};

/*
  EXAMPLE HTML:
*/
