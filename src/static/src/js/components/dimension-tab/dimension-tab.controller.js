goog.module('dmb.components.dimensionTab.controller');


/**
 * DOM selectors used by component.
 *
 * @const
 * @type {Object}
 */
const DOM_SELECTORS = {};


/**
 * DimensionTab class controller.
 */
class DimensionTabController {

  /**
   * DimensionTab controller
   *
   * @param {!angular.Scope} $scope
   * @param {!Object} reportService
   * @param {!Function} floorDmbFactory
   * @param {!Object} dimensionHeaders
   * @param {!Object} dimensionHeadersDescription
   * @param {!Object} dimensionLevelDescription
   * @param {!Object} dimensionLevelRecommendations
   *
   * @ngInject
   */
  constructor(
      $scope,
      reportService,
      floorDmbFactory,
      dimensionHeaders,
      dimensionHeadersDescription,
      dimensionLevelDescription,
      dimensionLevelRecommendations) {
        /**
         * @export
         * type {Object}
         */
        this.dimensionHeaders = dimensionHeaders;

        /**
         * @export
         * type {Object}
         */
        this.dimensionHeadersDescription = dimensionHeadersDescription;

        /**
         * @export
         * type {Object}
         */
        this.dimensionLevelDescription = dimensionLevelDescription;

        /**
         * @export
         * type {Object}
         */
        this.dimensionLevelRecommendations = dimensionLevelRecommendations;

        /**
         * @export
         * type {Object}
         */
        this.dmb = null;

        /**
         * @export
         * type {Object}
         */
        this.floorDMB = null;

        $scope.$watch(() => (reportService.dmb_d), (nVal)=> {
          this.dmb = nVal ? nVal[$scope['dmbDimensionTab']] : null;
          this.floorDMB = floorDmbFactory(this.dmb);
        });

        this.reportService = reportService;
  }
}


/** @const {string} */
DimensionTabController.CONTROLLER_NAME = 'DimensionTabCtrl';


/** @const {string} */
DimensionTabController.CONTROLLER_AS_NAME = 'dimensionTabCtrl';


exports = {
  main: DimensionTabController,
  CONTROLLER_NAME: DimensionTabController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: DimensionTabController.CONTROLLER_AS_NAME,
};
