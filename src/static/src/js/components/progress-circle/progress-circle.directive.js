goog.module('dmb.components.progressCircle.directive');

const reportCtrl = goog.require('dmb.components.progressCircle.controller');

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportDirective() {
  return {
    restrict: 'A',
    controller: reportCtrl.main,
    controllerAs: reportCtrl.CONTROLLER_AS_NAME,

  };
}


/** @const {string} */
ReportDirective.DIRECTIVE_NAME = 'dmbReport';


exports = {
  main: ReportDirective,
  DIRECTIVE_NAME: ReportDirective.DIRECTIVE_NAME,
};
