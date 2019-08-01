goog.module.declareNamespace('dmb.components.report.directive');

import * as reportCtrl from './report.controller';

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


export const main = ReportDirective;
export const DIRECTIVE_NAME = ReportDirective.DIRECTIVE_NAME;
