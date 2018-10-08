goog.module('dmb.components.progressTable.controller');

/**
 * ProgressTable class controller.
 */
class ProgressTableController {
  /**
   * ProgressTable controller
   *
   * @param {Object} floorDmbFactory
   *
   * @constructor
   * @ngInject
   */
  constructor(floorDmbFactory) {
    /**
     * @type {Object}
     * @private
     */
    this.floorDmbFactory_ = floorDmbFactory;
  }

  /**
   *
   * @param {?number} dmb
   * @return {string}
   * @export
   */
  getClass(dmb) {
    const activeClassMap = {
      0: 'nascent',
      1: 'emerging',
      2: 'connected',
      3: 'multimoment',
    };
    return activeClassMap[this.floorDmbFactory_(dmb)];
  }

  /**
   *
   * @param {number} dmb
   * @return {string}
   * @export
   */
  getProgressWidth(dmb) {
    const progWidth = dmb * 100;
    // We add an offset to make sure it's clear the bar overlaps the right column.
    const offset = dmb ? 5 : 0;
    return `calc(${progWidth}% + ${offset}px)`;
  }
}


/** @const {string} */
ProgressTableController.CONTROLLER_NAME = 'ProgressTableCtrl';


/** @const {string} */
ProgressTableController.CONTROLLER_AS_NAME = 'progressTableCtrl';


exports = {
  main: ProgressTableController,
  CONTROLLER_NAME: ProgressTableController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ProgressTableController.CONTROLLER_AS_NAME,
};
