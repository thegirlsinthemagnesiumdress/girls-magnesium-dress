goog.module.declareNamespace('dmb.components.reportAdmin.directive');

import * as reportAdminCtrl from './report-admin.controller';

/**
 * Report List directive.
 * @param {!angular.$location} $location
 * @param {!angular.$timeout} $timeout
 * @param {Object} sidePanelService
 *
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportListDirective($location, $timeout, sidePanelService) {
  return {
    restrict: 'A',
    controller: reportAdminCtrl.main,
    controllerAs: reportAdminCtrl.CONTROLLER_AS_NAME,
    link() {
      $timeout(() => {
        if ($location.hash().includes('create-survey')) {
          sidePanelService.openPanel('dmb-create-survey');
        }
      }, 0);
    },
  };
}


/** @const {string} */
ReportListDirective.DIRECTIVE_NAME = 'dmbReportsAdmin';


export const main = ReportListDirective;
export const DIRECTIVE_NAME = ReportListDirective.DIRECTIVE_NAME;
