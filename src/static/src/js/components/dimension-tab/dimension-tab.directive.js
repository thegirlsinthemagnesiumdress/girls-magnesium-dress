goog.module('dmb.components.dimensionTab.directive');

const dimensionTabCtrl = goog.require('dmb.components.dimensionTab.controller');
const dimensionTabtemplate = goog.require('dmb.components.dimensionTab.template');

/**
 * Dimension tab directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportDirective() {
  return {
    restrict: 'A',
    scope: {
      dmbDimensionTab: '@',
      companyName: '@',
    },
    template: dimensionTabtemplate,
    controller: dimensionTabCtrl.main,
    controllerAs: dimensionTabCtrl.CONTROLLER_AS_NAME,
  };
}


/** @const {string} */
ReportDirective.DIRECTIVE_NAME = 'dmbDimensionTab';


exports = {
  main: ReportDirective,
  DIRECTIVE_NAME: ReportDirective.DIRECTIVE_NAME,
};

/*
  EXAMPLE HTML:
*/
