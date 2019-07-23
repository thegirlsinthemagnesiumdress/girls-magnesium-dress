 goog.module.declareNamespace('dmb.components.sidePanel.directive');

import {SidePanel} from './side-panel.class';

/**
 * Side panel directive.
 * @param {Object} sidePanelService
 *
 * @ngInject
 * @return {Object} Config for the directive
 */
function SidePanelDirective(sidePanelService) {
  return {
    restrict: 'A',
    link(scope, element, attrs) {
      scope.class = new SidePanel(element[0], false);
      sidePanelService.registerPanel(element[0].id, scope.class);

      scope.$on('$destroy', scope.class.destroy);
    },
  };
}


/** @const {string} */
SidePanelDirective.DIRECTIVE_NAME = 'dmbSidePanel';


export const main = SidePanelDirective;
export const DIRECTIVE_NAME = SidePanelDirective.DIRECTIVE_NAME;

/*

  EXAMPLE HTML:

  // Trigger element

  <button class="dmb-survey-checklist-button" dmb-side-panel-trigger="#some-id">Trigger Element</button>

  // Side panel

  // default position is right side, for left side use `dmb-side-panel--left`
  // default width is 90%, for narrow side panel use `dmb-side-panel--narrow`

  <div id="some-id" class="dmb-side-panel" dmb-side-panel>

    <button class="dmb-side-panel__fab dmb-fab" dmb-side-panel-close>
      <span class="dmb-fab__icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <use xlink:href="#mi-close"></use>
        </svg>
      </span>
      <span class="dmb-fab__text">Close</span>
    </button>

    <div class="dmb-side-panel__inner">
      <h1 class="h-c-headline h-c-headline--two dmb-h-mb--medium">Side panel title</h1>
      [Side panel content goes here…]
    </div>

  </div>

*/
