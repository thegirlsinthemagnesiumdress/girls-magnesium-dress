goog.module('dmb.components.dimensionTab.directive');

const dimensionTabCtrl = goog.require('dmb.components.dimensionTab.controller');
const dimensionTabLegacyTemplate = goog.require('dmb.components.dimensionTab.legacyTemplate');
const dimensionTabTemplate = goog.require('dmb.components.dimensionTab.template');

/**
 * Dimension tab directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function DimensionTabDirective() {
  return {
    restrict: 'A',
    scope: {
      'dmbDimensionTab': '@',
      'companyName': '@',
    },
    template: function(tElem, tAttrs) {
      return tAttrs.tenant === 'retail' ? dimensionTabTemplate : dimensionTabLegacyTemplate;
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
