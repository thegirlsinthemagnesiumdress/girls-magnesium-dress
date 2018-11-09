goog.module('dmb.components.scroll.SmoothScrollCtrl');

const EventType = goog.require('goog.events.EventType');
const KeyCodes = goog.require('goog.events.KeyCodes');

/**
 * Directive controller for smooth scroll directive. Listens for clicks and
 * key press events on <a> elements and triggers animated scroll on the page.
 *
 * This is copied from glue.
 * @final
 */
class SmoothScrollCtrl {
  /**
   * @param {!angular.Scope} $scope
   * @param {!angular.Attributes} $attrs
   * @param {!angular.JQLite} $element
   * @param {!Object} glueSmoothScrollService
   * @ngInject
   */
  constructor($scope, $attrs, $element, glueSmoothScrollService) {
    /** @private {!angular.Scope} */
    this.ngScope_ = $scope;

    /** @private {!angular.Attributes} */
    this.ngAttrs_ = $attrs;

    /** @private {!angular.JQLite} */
    this.ngElement_ = $element;

    /** @private {!Object} */
    this.glueSmoothScrollService_ = glueSmoothScrollService;

    /** @private {string} */
    this.id_ = '';

    this.init_();
  }

  /**
   * Calls scrollTo method in glue smooth scroll service
   * @param {Object=} e
   * @private
   */
  scroll_(e) {
    const config = {
      hash: false,
    };
    const duration = parseInt(this.ngAttrs_['glueSmoothScrollDuration'], 10);
    if (duration) {
      config.duration = duration;
    }
    const easing = this.ngAttrs_['glueSmoothScrollEasing'];
    if (easing) {
      config.easing = easing;
    }
    const direction = this.ngAttrs_['glueSmoothScrollDirection'];
    if (direction) {
      config.direction = direction;
    }
    const hash = this.ngAttrs_['glueSmoothScrollhash'];
    if (angular.isDefined(hash)) {
      config.hash = hash;
    }
    this.glueSmoothScrollService_.scrollTo(this.id_, config);
    e.preventDefault();
  }

  /**
   * Calls scroll method when the Enter key gets pressed.
   * @param {!Event} e
   * @private
   */
  keyDownHandler_(e) {
    const key = e.which || e.keyCode;
    if (key === KeyCodes.ENTER) {
      this.scroll_();
    }
    e.preventDefault();
  }

  /**
   * Initializes the component.
   * @private
   */
  init_() {
    this.id_ = this.ngAttrs_['href'].split('#').pop();
    if (this.id_ !== '' && document.getElementById(this.id_)) {
      const scrollFunc = this.scroll_.bind(this);
      const keyDownHandlerFunc = this.keyDownHandler_.bind(this);

      // Listens for click and keypress and triggers scrolls.
      this.ngElement_.on(EventType.CLICK, scrollFunc);
      this.ngElement_.on(EventType.KEYDOWN, keyDownHandlerFunc);

      // Removes the listeners when scope gets destroyed.
      this.ngScope_.$on('$destroy', () => {
        this.ngElement_.off(EventType.CLICK, scrollFunc);
        this.ngElement_.off(EventType.KEYDOWN, keyDownHandlerFunc);
      });
    }
  }
}


/** @const {string} */
SmoothScrollCtrl.CONTROLLER_NAME = 'DmbSmoothScrollCtrl';


/** @const {string} */
SmoothScrollCtrl.CONTROLLER_AS_NAME = 'dmbSmoothScrollCtrl';


exports = {
  main: SmoothScrollCtrl,
  CONTROLLER_NAME: SmoothScrollCtrl.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: SmoothScrollCtrl.CONTROLLER_AS_NAME,
};
