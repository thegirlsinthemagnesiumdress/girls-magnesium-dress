goog.module('dmb.components.report.directive');

const Report = goog.require('dmb.components.report.class');

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportDirective() {
  return {
    restrict: 'A',
    controller: '',
    controllerAs:'',
  };
}


/** @const {string} */
ReportDirective.DIRECTIVE_NAME = 'dmbReport';


exports = {
  main: ReportDirective,
  DIRECTIVE_NAME: ReportDirective.DIRECTIVE_NAME,
};
