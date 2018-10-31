goog.module('dmb.components.reportList.directive');

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
    link() {
      $timeout(() => {
        if ($location.hash().includes('create-survey')) {
          sidePanelService.openPanel('dmb-create-survey');
        }
      }, 0);
    },
    controller() {},
  };
}


/** @const {string} */
ReportListDirective.DIRECTIVE_NAME = 'dmbReportsAdmin';


exports = {
  main: ReportListDirective,
  DIRECTIVE_NAME: ReportListDirective.DIRECTIVE_NAME,
};
