goog.module('dmb.components.scroll.directive');

/**
 * @param {!Object} scrollService
 * @return {Object}
 * @ngInject
 */
function scrollAwareDirective(scrollService) {
  return {
    restrict: 'A',
    /**
     * @param  {!angular.Scope} scope The scope of the directive
     * @param  {!angular.JQLite} element The element to be scroll aware
     * @param  {{dmbScrollAwareEnterClass: string, dmbScrollAwareExitClass: string}} attrs The attributes on the html
     * @param  {!angular.ComponentController} ctrl The controller to bind to
     */
    link(scope, element, attrs, ctrl) {
      const nativeElement = element[0];
      let cachedDimensions = null;

      const enterClass = attrs['dmbScrollAwareEnterClass'];
      const exitClass = attrs['dmbScrollAwareExitClass'];

      ctrl.cacheValid = false;
      ctrl.checkElementPosition = checkElementPosition;
      ctrl.getElementDimensions = getElementDimensions;
      ctrl.isInView = isInView;
      ctrl.isOutOfView = isOutOfView;
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
        const {elTop, elHeight, screenHeight} = ctrl.getElementDimensions();
        const elBottom = elTop + elHeight;
        const screenBottom = screenTop + screenHeight;

        if (screenBottom > elTop && screenTop < elBottom) {
          ctrl.isInView();
        } else {
          ctrl.isOutOfView();
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
          elTop: scrollService.getElementOffsetTop(nativeElement),
          elHeight: nativeElement.offsetHeight,
          screenHeight: window.innerHeight,
        };
        ctrl.cacheValid = true;

        return cachedDimensions;
      }

      /**
       * Function called when the element enters the viewport
       */
      function isInView() {
        if (enterClass) {
          nativeElement.classList.add(enterClass);

          // If the classes have been added and there are no classes to remove, we're done
          if (!exitClass) {
            ctrl.onDestroy();
          }
        }
      }

      /**
       * Function called when the element leaves the viewport
       */
      function isOutOfView() {
        if (exitClass) {
          nativeElement.classList.remove(exitClass);

          // If the classes have been removed and there are no classes to add, we're done
          if (!enterClass) {
            ctrl.onDestroy();
          }
        }
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
  DIRECTIVE_NAME: 'dmbScrollAware',
  main: scrollAwareDirective,
};
