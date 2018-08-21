goog.module('dmb.components.sidePanel.directive');

const SidePanel = goog.require('dmb.components.sidePanel.class');

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

/*

  EXAMPLE HTML:

  <div id="some-id" class="dmb-side-panel dmb-side-panel--narrow" dmb-side-panel>

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
