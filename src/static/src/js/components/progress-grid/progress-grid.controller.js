goog.module('dmb.components.progressGrid.controller');

/**
 * ProgressGrid class controller.
 */
class ProgressGridController {
  /**
   * ProgressGrid controller
   *
   * @param {!Object} tenantConf
   *
   * @ngInject
   */
  constructor(tenantConf) {
    /**
     * @export
     * type {Object}
     */
    this.levels = tenantConf.levels;

    /**
     * @export
     * type {Object}
     */
    this.levelsTotal = tenantConf.levelsTotal;
  }

  /**
   * Function to get a rounded level value from a value
   * @param {number} value
   * @return {number}
   * @export
   */
  getLevel(value) {
    return Math.min(Math.floor(value), (this.levelsTotal - 1));
  }

  /**
   * Function to get the level name from the value
   * @param {number} value
   * @return {string}
   * @export
   */
  getLevelName(value) {
    const level = this.getLevel(value);
    return this.levels[level];
  }

  /**
   * Function to get the progress width/height for the horizontal and vertical bars
   * @param {number} value
   * @return {string}
   * @export
   */
  getProgress(value) {
    const prog = value * 100;
    return `${prog}%`;
  }
}


/** @const {string} */
ProgressGridController.CONTROLLER_NAME = 'ProgressGridCtrl';


/** @const {string} */
ProgressGridController.CONTROLLER_AS_NAME = 'progressGridCtrl';


exports = {
  main: ProgressGridController,
  CONTROLLER_NAME: ProgressGridController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ProgressGridController.CONTROLLER_AS_NAME,
};
