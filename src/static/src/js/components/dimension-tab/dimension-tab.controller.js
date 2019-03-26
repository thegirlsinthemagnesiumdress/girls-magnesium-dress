goog.module('dmb.components.dimensionTab.controller');

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
   * @param {!Object} tenantConf
   *
   * @ngInject
   */
  constructor(
    $scope,
    reportService,
    floorDmbFactory,
    tenantConf,
    dmbStaticUrl) {
    /**
     * @export
     * @type {string}
     */
    this.dmbStaticUrl = dmbStaticUrl;

    /**
     * @type {!Object}
     * @export
     */
    this.levels = tenantConf.levels;

    /**
     * @export
     * @type {string}
     */
    this.levelsTotal = tenantConf.levelsTotal;

    /**
     * @export
     * @type {string}
     */
    this.logoUrls = {};

    /**
     * @export
     * type {Object}
     */
    this.dimensionClassNames = {};

    tenantConf.dimensions.map((dimension) => {
      const dimensionHyphenatedName = dimension.replace(/_/g, '-');
      this.dimensionClassNames[dimension] = dimensionHyphenatedName;
      this.logoUrls[dimension] = `devstatic/img/${$scope.tenant}/dimensions/${dimensionHyphenatedName}.svg`;
    });

    /**
     * @export
     * type {Object}
     */
    this.dimensionHeaders = tenantConf.dimensionHeaders;

    /**
     * @export
     * type {Object}
     */
    this.dimensionHeadersDescription = tenantConf.dimensionHeadersDescription;

    /**
     * @export
     * type {Object}
     */
    this.dimensionLevelDescription = tenantConf.dimensionLevelDescription;

    /**
     * @export
     * type {Object}
     */
    this.dimensionLevelRecommendations = tenantConf.dimensionLevelRecommendations;

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

    /**
     * @export
     * type {Object}
     */
    this.industryDmb = null;

    /**
     * @export
     * type {Object}
     */
    this.industryDmb_bp = null;

    /**
     * @export
     * type {Object}
     */
    this.industryResult = null;

    /**
    * type {!Object}
      */
    this.reportService = reportService;

    $scope.$watch(() => (reportService.dmb_d), (nVal)=> {
      this.dmb = nVal ? nVal[$scope['dmbDimensionTab']] : null;
      this.floorDMB = floorDmbFactory(this.dmb);
    });

    $scope.$watch(() => (reportService.industryDmb_d), (nVal)=> {
      this.industryDmb = nVal ? nVal[$scope['dmbDimensionTab']] : null;
    });

    $scope.$watch(() => (reportService.industryDmb_d_bp), (nVal)=> {
      this.industryDmb_bp = nVal ? nVal[$scope['dmbDimensionTab']] : null;
    });

    $scope.$watch(() => (reportService.industryResult), (nVal)=> {
      this.industryResult = nVal;
    });
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
