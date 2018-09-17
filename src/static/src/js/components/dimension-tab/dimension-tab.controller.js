goog.module('dmb.components.dimensionTab.controller');


/**
 * DOM selectors used by component.
 *
 * @const
 * @type {object}
 */
const DOM_SELECTORS = {};


/**
 * DimensionTab class controller.
 */
class DimensionTabController {
  /**
   * DimensionTab controller
   *
   * @param {!angular.$element} $element
   * @param {!angular.$scope} $scope
   * @param {!object} reportService
   * @param {!object} dimensionHeaders
   * @param {!object} dimensionHeadersDescription
   * @param {!object} dimensionLevelDescription
   * @param {!object} dimensionLevelRecomendations
   * @constructor
   * @ngInject
   */
  constructor(
      $element,
      $scope,
      reportService,
      dimensionHeaders,
      dimensionHeadersDescription,
      dimensionLevelDescription,
      dimensionLevelRecomendations) {
        /**
         * @export
         * type {object}
         */
        this.dimensionHeaders = dimensionHeaders;

        /**
         * @export
         * type {object}
         */
        this.dimensionHeadersDescription = dimensionHeadersDescription;

        /**
         * @export
         * type {object}
         */
        this.dimensionLevelDescription = dimensionLevelDescription;

        /**
         * @export
         * type {object}
         */
        this.dimensionLevelRecomendations = dimensionLevelRecomendations;

        /**
         * @export
         * type {object}
         */
        this.dmb = null;

        /**
         * @export
         * type {object}
         */
        this.floorDMB = null;

        $scope.$watch(() => (reportService.dmb_d), (nVal)=> {
          this.dmb = nVal ? nVal[$scope.dmbDimensionTab] : null;
          this.floorDMB = Math.min(Math.floor(this.dmb), 3);
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
