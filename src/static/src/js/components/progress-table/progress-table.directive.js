goog.module.declareNamespace('dmb.components.progressTable.directive');

import * as progTableCtrl from './progress-table.controller';

const progressTableTemplateUrl = '/angular/progress-table';

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportDirective() {
  return {
    restrict: 'E',
    scope: {
      'companyName': '@',
      'industryAvg': '<',
      'industryBest': '<',
      'ratingMain': '<',
      'industryReady': '<',
    },
    controller: progTableCtrl.main,
    controllerAs: progTableCtrl.CONTROLLER_AS_NAME,
    templateUrl: progressTableTemplateUrl,
  };
}


/** @const {string} */
ReportDirective.DIRECTIVE_NAME = 'dmbProgressTable';


export const main = ReportDirective;
export const DIRECTIVE_NAME = ReportDirective.DIRECTIVE_NAME;

/*
EXAMPLE HTML

<dmb-progress-table
  data-rating-main="reportCtrl.result.dmb"
  data-industry-avg="reportCtrl.industryResult.dmb"
  data-industry-best="reportCtrl.industryResult.dmb_bp"
  data-company-name="{[reportCtrl.survey.company_name]}"
  data-industry-ready="!!dimensionTabCtrl.industryResult">
</dmb-progress-table>

*/
