goog.module('dmb.components.progressGrid.controller');

/**
 * ProgressGrid class controller.
 */
class ProgressGridController {
  /**
   * ProgressGrid controller
   *
   * @param {function (*): number|null} floorDmbFactory
   * @param {!Object} tenantConf
   *
   * @ngInject
   */
  constructor(
    floorDmbFactory,
    tenantConf) {
    /**
     * @type {function (*): number|null}
     * @private
     */
    this.floorDmbFactory_ = floorDmbFactory;

    /**
     * @export
     * type {Object}
     */
    this.levels = tenantConf.levels;

    /**
     * @export
     * type {Object}
     */
    this.levelsTotal = Object.keys(this.levels).length;
  }

  /**
   *
   * @param {number} value
   * @return {string}
   * @export
   */
  getLevel(value) {
    return Math.min(Math.floor(value), (this.levelsTotal - 1));
  }

  /**
   *
   * @param {number} value
   * @return {string}
   * @export
   */
  getLevelName(value) {
    const level = this.getLevel(value);
    const levelName = this.levels[level];
    return levelName;
  }

  /**
   *
   * @param {number} value
   * @return {string}
   * @export
   */
  getProgress(value) {
    const prog = value * 100;
    const offset = this.getLevel(value);
    return `calc(${prog}% + ${offset}px)`;
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
