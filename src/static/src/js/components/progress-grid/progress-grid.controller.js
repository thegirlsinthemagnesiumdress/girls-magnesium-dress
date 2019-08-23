goog.module.declareNamespace('dmb.components.progressGrid.controller');

import {CONTENT_UPDATED_EVENT} from '../scroll/scroll-pin-top.directive';

/**
 * ProgressGrid class controller.
 */
class ProgressGridController {
  /**
   * ProgressGrid controller
   *
   * @param {!angular.$rootScope} $rootScope
   * @param {!Object} tenantConf
   * @param {!Function} dmbLevelsFactory
   *
   * @ngInject
   */
  constructor($rootScope, tenantConf, dmbLevelsFactory) {
    /**
     * @type {string}
     * @export
     */
    this.companyName;

    /**
     * @type {?number}
     * @export
     */
    this.ratingMain;

    /**
     * @type {?number}
     * @export
     */
    this.industryAvg;

    /**
     * @type {?number}
     * @export
     */
    this.industryBest;

    /**
     * @type {Object}
     * @export
     */
    this.industryReady;

    /**
     * @type {angular.$rootScope}
     * @export
     */
    this.$rootScope = $rootScope;

    /**
     * @type {Object}
     * @export
     */
    this.levels = tenantConf.levels;

    /**
     * @type {Object}
     * @export
     */
    this.levelsMax = tenantConf.levelsMax;

    /**
     * @type {Array<string>}
     * @export
     */
    this.levelsArray = tenantConf.levelsArray;

    /**
     * @type {Object}
     * @export
     */
    this.ratingMainData = {};


    /**
    * @type {Object}
    * @export
    */
    this.industryBestData = {};

    /**
     * @type {Object}
     * @export
     */
    this.industryAvgData = {};

    /**
     *
     * @type {Function}
     * @export
     */
    this.dmbLevelsFactory = dmbLevelsFactory;

    // Bind for external use
    this.updateLevelsData = this.updateLevelsData.bind(this);
  }

  /**
   * On scope initialisation update the values
   */
  $onInit() {
    this.updateLevelsData();
  }

  /**
   * Respond to property changes and update the values
   */
  $onChanges() {
    this.updateLevelsData();
    this.$rootScope.$broadcast(CONTENT_UPDATED_EVENT);
  }

  /**
   * updates the levels data for from dmbLevelsFactory
   */
  updateLevelsData() {
    this.ratingMainData = this.dmbLevelsFactory(this.ratingMain);
    this.industryBestData = this.dmbLevelsFactory(this.industryBest);
    this.industryAvgData = this.dmbLevelsFactory(this.industryAvg);
  }

  /**
   * Function to get the progress width/height for the horizontal and vertical bars.
   * The value returned is a percentage of the first level because the element we are
   * resizing sits within the first level.
   * @param {number} value
   * @return {string}
   * @export
   */
  getProgress(value) {
    if (!angular.isDefined(value)) {
      return '';
    }

    const firstLevel = this.levelsArray[0];
    const firstLevelRange = this.levelsArray[1] - firstLevel;

    // normalise value to 0 by subtracting the firstLevel
    value -= firstLevel;

    // calculate the percentage of bar based on the first level's range
    const prog = (value / firstLevelRange) * 100;
    return `${prog}%`;
  }
}


/** @const {string} */
ProgressGridController.CONTROLLER_NAME = 'ProgressGridCtrl';


/** @const {string} */
ProgressGridController.CONTROLLER_AS_NAME = 'progressGridCtrl';


export const main = ProgressGridController;
export const CONTROLLER_NAME = ProgressGridController;
export const CONTROLLER_AS_NAME = ProgressGridController.CONTROLLER_AS_NAME;
