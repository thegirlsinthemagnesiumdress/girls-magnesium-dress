import * as reportCtrl from '../progress-circle/progress-circle.controller';

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ReportDirective() {
  return {
    restrict: 'A',
    scope: false,
    controller: reportCtrl.main,
    controllerAs: reportCtrl.CONTROLLER_AS_NAME,
  };
}


/** @const {string} */
ReportDirective.DIRECTIVE_NAME = 'dmbProgressCircle';


export const main = ReportDirective;
export const DIRECTIVE_NAME = ReportDirective.DIRECTIVE_NAME;

/*
  EXAMPLE HTML:

  <svg
      dmb-progress-circle="reportCtrl.result.dmb"
      class="dmb-progress-circle__prog-svg"
      width="214" height="214" viewBox="0 0 120 120">
    <circle class="dmb-progress-circle__bg-bar" cx="60" cy="60" r="54" fill="none" stroke-width="12" />
    <circle class="dmb-progress-circle__prog-bar" cx="60" cy="60" r="54" fill="none" stroke-width="12" />
  </svg>
*/
