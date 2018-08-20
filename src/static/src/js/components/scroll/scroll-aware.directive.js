goog.module('dmb.components.scroll.directive');

/**
 * @param {!Object} scrollService
 * @return {Object}
 * @ngInject
 */
function scrollAwareDirective(scrollService) {
  return {
    restrict: 'A',
    link(scope, element, attrs, ctrl) {
      const nativeElement = element[0];
      let cachedDimensions = null;

      ctrl.getElementDimensions = getElementDimensions;
      ctrl.isInView = isInView;
      ctrl.isOutOfView = isOutOfView;

      // Once everything is bound, call the onReady function
      ctrl.onReady();

      /**
       * [getElementDimensions description]
       * @return {Object.<string, number>} Returns a set of dimension properties
       */
      function getElementDimensions() {
        if (ctrl.cacheValid && cachedDimensions) {
          return cachedDimensions;
        }

        cachedDimensions = {
          elTop: nativeElement.offsetTop,
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
        if (attrs.dmbScrollAwareEnterClass) {
          nativeElement.classList.add(attrs.dmbScrollAwareEnterClass);
        }
      }

      /**
       * Function called when the element leaves the viewport
       */
      function isOutOfView() {
        if (attrs.dmbScrollAwareExitClass) {
          nativeElement.classList.remove(attrs.dmbScrollAwareExitClass);
        }
      }
    },
    controller() {
      const ctrl = this;

      ctrl.$onInit = onInit;
      ctrl.checkElementPosition = checkElementPosition;
      ctrl.onResize = onResize;
      ctrl.onReady = onReady;
      ctrl.cacheValid = false;

      /**
       * Init event callback
       */
      function onInit() {
        scrollService.addListener(ctrl.checkElementPosition);
        window.addEventListener('resize', ctrl.onResize);
      }

      /**
       * Checks if the element is on screen or not
       * @param  {number} screenTop How far down the page the top of the screen has scrolled
       */
      function checkElementPosition(screenTop) {
        const {elTop, elHeight, screenHeight} = ctrl.getElementDimensions();
        const elBottom = elTop + elHeight;
        const screenBottom = scrollY + screenHeight;

        if (screenBottom > elTop && screenTop < elBottom) {
          ctrl.isInView();
        } else {
          ctrl.isOutOfView();
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
    },
  };
}

exports = {
  DIRECTIVE_NAME: 'dmbScrollAware',
  main: scrollAwareDirective,
};
