goog.module('dmb.components.dimensionTab.controller');

const tenantDataElementName = 'bootstrap-data';

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
   * @param {!string} dmbStaticUrl
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
     * @type string
     * @export
     */
    this.tenant = '';

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
     * type {Object}
     */
    this.dimensionClassNames = {};

    tenantConf.dimensions.forEach((dimension) => {
      this.dimensionClassNames[dimension] = dimension.replace(/_/g, '-');
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
     * Subdimensions
     * @type {Object}
     * @export
     */
    this.subdimensions = tenantConf.subdimensions;

    /**
     * Subdimension labels
     * @type {Object}
     * @export
     */
    this.subdimensionHeaders = tenantConf.subdimensionHeaders;

    /**
     * Subdimension labels
     * @type {string}
     * @export
     */
    this.subdimensionDescription = tenantConf.subdimensionDescription;

    /**
     * Subdimension descriptions
     * @type {Object}
     * @export
     */
    this.subdimensionDescriptions = tenantConf.subdimensionDescriptions;

    /**
    * type {!Object}
      */
    this.reportService = reportService;

    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];

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
