goog.module('dmb.components.progressCircle.controller');


/**
 * DOM selectors used by component.
 *
 * @const
 * @type {Object}
 */
const DOM_SELECTORS = {
  progressBar: '.dmb-progress-circle__prog-bar',
};


/**
 * ProgressCircle class controller.
 */
class ProgressCircleController {
  /**
   * ProgressCircle controller
   *
   * @param {!angular.JQLite} $element
   * @param {!angular.Attributes} $attrs
   * @param {!angular.Scope} $scope
   * @param {!angular.$filter} $filter
   *
   * @ngInject
   */
  constructor($element, $attrs, $scope, $filter) {
    /**
     * @type {angular.JQLite}
     * @private
     */
    this.$element_ = $element;

    /**
     * @type {HTMLElement}
     * @private
     */
    this.progressBar_ = $element[0].querySelector(DOM_SELECTORS.progressBar);

    $scope.$watch($attrs['dmbProgressCircle'], (nVal) => {
      const prog = $filter('dmbPercentageNumber')(nVal);
      this.setProgressCircle(prog);
    });
  }

  /**
   * Sets the circle progress by setting the strole-dashoffset.
   * @param {!number} progress
   */
  setProgressCircle(progress) {
    const dashOffset = 339.292 * (100 - progress) / 100;
    this.progressBar_.setAttribute('style', `stroke-dashoffset: ${dashOffset};`);
  }
}


/** @const {string} */
ProgressCircleController.CONTROLLER_NAME = 'ProgressCircleCtrl';


/** @const {string} */
ProgressCircleController.CONTROLLER_AS_NAME = 'progressCircleCtrl';


exports = {
  main: ProgressCircleController,
  CONTROLLER_NAME: ProgressCircleController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ProgressCircleController.CONTROLLER_AS_NAME,
};
