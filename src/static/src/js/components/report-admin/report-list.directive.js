goog.module('dmb.components.reportAdmin.directive');

const reportAdminCtrl = goog.require('dmb.components.reportAdmin.controller');

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


exports = {
  main: ReportListDirective,
  DIRECTIVE_NAME: ReportListDirective.DIRECTIVE_NAME,
};
