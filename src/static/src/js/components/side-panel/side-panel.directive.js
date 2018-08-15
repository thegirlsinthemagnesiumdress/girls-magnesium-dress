goog.module('dmb.components.sidePanel.directive');

const SidePanel = goog.require('dmb.components.sidePanel.class').main;

/**
 * Side panel directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function SidePanelDirective() {
  return {
    restrict: 'A',
    link(scope, element, attrs) {
      scope.class = new SidePanel(element[0]);

      scope.$on('$destroy', scope.class.destroy);
    },
  };
}


/** @const {string} */
SidePanelDirective.DIRECTIVE_NAME = 'dmbSidePanel';


exports = {
  main: SidePanelDirective,
  DIRECTIVE_NAME: SidePanelDirective.DIRECTIVE_NAME,
};
