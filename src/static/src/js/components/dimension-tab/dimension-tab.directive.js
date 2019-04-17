goog.module('dmb.components.dimensionTab.directive');

const dimensionTabCtrl = goog.require('dmb.components.dimensionTab.controller');
const dimensionTabLegacyTemplateUrl = '/angular/dimension-tab-legacy/';
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
      'companyName': '@',
      'dmbDimensionTab': '@',
      'tenant': '@',
    },
    templateUrl: function(tElem, tAttrs) {
      return tAttrs.tenant === 'ads' ? dimensionTabLegacyTemplateUrl : dimensionTabTemplateUrl;
    },
    controller: dimensionTabCtrl.main,
    controllerAs: dimensionTabCtrl.CONTROLLER_AS_NAME,
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
