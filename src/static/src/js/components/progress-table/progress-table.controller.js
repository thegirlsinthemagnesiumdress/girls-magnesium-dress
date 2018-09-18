goog.module('dmb.components.progressTable.controller');

/**
 * ProgressTable class controller.
 */
class ProgressTableController {

  /**
   * ProgressTable controller
   *
   * @constructor
   * @ngInject
   */
  constructor($element, floorDmbFactory) {
    /**
     * @type {angular.$element}
     * @private
     */
    this.floorDmbFactory_ = floorDmbFactory;
  }

  getClass(dmb) {
    const activeClassMap = {
      0: 'nascent',
      1: 'emerging',
      2: 'connected',
      3: 'multimoment',
    };
    return activeClassMap[this.floorDmbFactory_(dmb)];
  }

  getProgressWidth(dmb) {
    const progWidth = dmb * 100;
    return `calc(${progWidth}% + ${this.floorDmbFactory_(dmb)}px)`;
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
