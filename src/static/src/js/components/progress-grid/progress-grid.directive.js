goog.module('dmb.components.progressGrid.directive');

const progressGridCtrl = goog.require('dmb.components.progressGrid.controller');
const progressGridTemplate = goog.require('dmb.components.progressGrid.template');

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function ProgressGridDirective() {
  return {
    restrict: 'E',
    scope: {
      'companyName': '@',
      'companyLevel': '<',
      'industryAvg': '<',
      'industryBest': '<',
      'industryReady': '<',
    },
    controller: progressGridCtrl.main,
    controllerAs: progressGridCtrl.CONTROLLER_AS_NAME,
    template: progressGridTemplate,
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

*/
