
goog.module('dmb.components.scroll.pinTopDirective');


/**
 * Sets a class when the element's parent gets to the top of the viewport.
 * It remove the class when scrolling back up.
 *
 * @param {!Object} scrollService
 * @return {Object}
 * @ngInject
 */
function pinTopDirective(scrollService) {
  return {
    restrict: 'A',
    /**
     * @param  {!angular.Scope} scope The scope of the directive
     * @param  {!angular.JQLite} element The element to be scroll aware
     * @param  {{dmbScrollAwarepinnedClass: string, dmbScrollAwareExitClass: string}} attrs The attributes on the html
     * @param  {!angular.ComponentController} ctrl The controller to bind to
     */
    link(scope, element, attrs, ctrl) {
      const nativeElement = element[0];
      const parentElement = element[0].parentElement;
      const pinnedClass = attrs.dmbPinnedClass || 'dmb-pinned';
      let cachedDimensions = null;


      ctrl.cacheValid = false;
      ctrl.checkElementPosition = checkElementPosition;
      ctrl.getElementDimensions = getElementDimensions;
      ctrl.pinned = false;
      ctrl.isPinned = isPinned;
      ctrl.isNotPinned = isNotPinned;
      ctrl.onDestroy = onDestroy;
      ctrl.onReady = onReady;
      ctrl.onResize = onResize;

      scrollService.addListener(ctrl.checkElementPosition);
      window.addEventListener('resize', ctrl.onResize);
      scope.$on('$destroy', onDestroy);

      ctrl.onReady();

      /**
       * Checks if the element is on screen or not
       * @param  {number} screenTop How far down the page the top of the screen has scrolled
       */
      function checkElementPosition(screenTop) {
        const {parentTop} = ctrl.getElementDimensions();

        if (parentTop < screenTop) {
          ctrl.isPinned();
        } else {
          ctrl.isNotPinned();
        }
      }

      /**
       * [getElementDimensions description]
       * @return {Object.<string, number>} Returns a set of dimension properties
       */
      function getElementDimensions() {
        if (ctrl.cacheValid && cachedDimensions) {
          return cachedDimensions;
        }

        cachedDimensions = {
          parentTop: scrollService.getElementOffsetTop(parentElement),
          parentHeight: parentElement.offsetHeight,
          screenHeight: window.innerHeight,
        };
        ctrl.cacheValid = true;

        return cachedDimensions;
      }

      /**
       * Function called when the element enters the viewport
       */
      function isPinned() {
        nativeElement.classList.add(pinnedClass);
      }

      /**
       * Function called when the element leaves the viewport
       */
      function isNotPinned() {
        nativeElement.classList.remove(pinnedClass);
      }

      /**
       * Simply flags the dimentions to be recalculated after a resize
       */
      function onResize() {
        ctrl.cacheValid = false;
      }

      /**
       *
       */
      function onReady() {
        ctrl.checkElementPosition(window.scrollY);
      }

      /**
       * Unbinds the events when the scope is destroyed
       */
      function onDestroy() {
        scrollService.removeListener(ctrl.checkElementPosition);
        window.removeEventListener('resize', ctrl.onResize);
      }
    },
    controller() {},
  };
}

exports = {
  DIRECTIVE_NAME: 'dmbPinTop',
  main: pinTopDirective,
};