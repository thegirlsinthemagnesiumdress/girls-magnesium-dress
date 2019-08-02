goog.module.declareNamespace('dmb.components.progressTable.controller');

/**
 * ProgressTable class controller.
 */
class ProgressTableController {
  /**
   * ProgressTable controller
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


export const main = ProgressTableController;
export const CONTROLLER_NAME = ProgressTableController;
export const CONTROLLER_AS_NAME = ProgressTableController.CONTROLLER_AS_NAME;
