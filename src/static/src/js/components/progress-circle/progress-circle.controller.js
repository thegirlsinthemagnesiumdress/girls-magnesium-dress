/**
 * DOM selectors used by component.
 *
 * @const
 * @type {string}
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

        /**
     * @type {Object}
     * @export
     */
    this.firstLevel = tenantConf.levelsArray[0];

    /**
     * The circumference in pixels of the SVG circle we're animating.
     * Used to calculate the size of the progress
     * @type {number}
     * @export
     */
    this.svgCircumference = 339.292;

    $scope.$watch($attrs['dmbProgressCircle'], (dmbScore) => {
      if (dmbScore !== null) {
        const percentComplete = ((dmbScore - this.firstLevel) / (tenantConf.levelsMax - this.firstLevel)) * 100;
        this.setProgressCircle(percentComplete);
      }
    });
  }

  /**
   * Sets the circle progress by setting the strole-dashoffset.
   * @param {!number} percentComplete
   */
  setProgressCircle(percentComplete) {
    const dashOffset = this.svgCircumference * (100 - percentComplete) / 100;
    this.progressBar_.setAttribute('style', `stroke-dashoffset: ${dashOffset};`);
  }
}


/** @const {string} */
ProgressCircleController.CONTROLLER_NAME = 'ProgressCircleCtrl';


/** @const {string} */
ProgressCircleController.CONTROLLER_AS_NAME = 'progressCircleCtrl';


export const main = ProgressCircleController;
export const CONTROLLER_NAME = ProgressCircleController;
export const CONTROLLER_AS_NAME = ProgressCircleController.CONTROLLER_AS_NAME;
