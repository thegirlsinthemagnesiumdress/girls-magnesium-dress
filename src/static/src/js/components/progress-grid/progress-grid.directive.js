goog.module('dmb.components.progressGrid.directive');

const progressGridCtrl = goog.require('dmb.components.progressGrid.controller');
const progressGridTemplateUrl = '/angular/progress-grid';
const progressGridFallbackTemplateUrl = '/angular/progress-grid-fallback';

/**
 * Side panel directive.
 * @ngInject
 * @param {boolean} cssGridSupport
 * @return {Object} Config for the directive
 */
function ProgressGridDirective(cssGridSupport) {
  return {
    restrict: 'E',
    scope: {
      'companyName': '@',
      'ratingMain': '<',
      'industryAvg': '<',
      'industryBest': '<',
      'industryReady': '<',
    },
    controller: progressGridCtrl.main,
    controllerAs: progressGridCtrl.CONTROLLER_AS_NAME,
    bindToController: true,
    templateUrl: () => {
      return cssGridSupport ? progressGridTemplateUrl : progressGridFallbackTemplateUrl;
    },
  };
}


/** @const {string} */
ProgressGridDirective.DIRECTIVE_NAME = 'dmbProgressGrid';


exports = {
  main: ProgressGridDirective,
  DIRECTIVE_NAME: ProgressGridDirective.DIRECTIVE_NAME,
};

/*
EXAMPLE HTML
<dmb-progress-grid
    data-company-name="{[reportCtrl.survey.company_name]}"
    data-rating-main="reportCtrl.result.dmb"
    data-industry-avg="reportCtrl.industryResult.dmb"
    data-industry-best="reportCtrl.industryResult.dmb_bp"
    data-industry-ready="!!reportCtrl.industryResult">
</dmb-progress-grid>
*/
