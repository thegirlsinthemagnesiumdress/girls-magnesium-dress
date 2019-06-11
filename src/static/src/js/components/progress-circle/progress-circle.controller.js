goog.module('dmb.components.progressCircle.controller');

/**
 * DOM selectors used by component.
 *
 * @const
 * @type {Object}
 */
const progressBarClass = '.dmb-progress-circle__prog-bar';

/**
 * ProgressCircle class controller
 */
class ProgressCircleController {
  /**
   * ProgressCircle controller
   *
   * @param {!angular.JQLite} $element
   * @param {!angular.Attributes} $attrs
   * @param {!angular.Scope} $scope
   * @param {!Object} tenantConf
   *
   * @ngInject
   */
  constructor($element, $attrs, $scope, tenantConf) {
    /**
     * @type {HTMLElement}
     * @private
     */
    this.progressBar_ = $element[0].querySelector(progressBarClass);

    $scope.$watch($attrs['dmbProgressCircle'], (nVal) => {
      const percentComplete = nVal / tenantConf.levelsMax * 100;
      this.setProgressCircle(percentComplete);
    });
  }

  /**
   * Sets the circle progress by setting the strole-dashoffset.
   * @param {!number} percentComplete
   */
  setProgressCircle(percentComplete) {
    const dashOffset = 339.292 * (100 - percentComplete) / 100;
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
