goog.module('dmb.components.sidePanel.triggerDirective');

// const SidePanel = goog.require('dmb.components.sidePanel.class');


/**
 * Side panel trigger directive.
 * @param {Object} sidePanelService
 *
 * @return {Object} Config for the directive
 * @ngInject
 */
function SidePanelTriggerDirective(sidePanelService) {
  return {
    restrict: 'A',
    link(scope, element, attrs) {
      element.on('click', () => {
        const targetMatches = attrs['dmbSidePanelTrigger'].match(/#(.+)/);
        if (targetMatches[1]) {
          sidePanelService.openPanel(targetMatches[1]);
        } else {
          console.warn('Side panel target not found');
        }
      });
    },
  };
}


/** @const {string} */
SidePanelTriggerDirective.DIRECTIVE_NAME = 'dmbSidePanelTrigger';


exports = {
  main: SidePanelTriggerDirective,
  DIRECTIVE_NAME: SidePanelTriggerDirective.DIRECTIVE_NAME,
};
