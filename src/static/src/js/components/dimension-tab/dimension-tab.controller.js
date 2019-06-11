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
   * @param {!angular.$sce} $sce
   * @param {!Object} reportService
   * @param {!Function} dmbLevelsFactory
   * @param {!Function} resultInTopLevel
   * @param {!Object} tenantConf
   * @param {!string} dmbStaticUrl
   *
   * @ngInject
   */
  constructor(
    $scope,
    $sce,
    reportService,
    dmbLevelsFactory,
    resultInTopLevel,
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
     * @type {String}
     */
    this.levelsMax = tenantConf.levelsMax;

    /**
     * @export
     * @type {Object}
     */
    this.currentLevel = {};

    /**
     * @export
     * @type {Object}
     */
    this.nextLevel = {};

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
    this.dimensionHeader = '';

    /**
     * @export
     * type {Object}
     */
    this.dimensionHeaderDescription = '';

    /**
     * @export
     * type {Object}
     */
    this.dimensionLevelDescription = '';

    /**
     * @export
     * type {Object}
     */
    this.recommendations = {};

    /**
     * @export
     * type {Object}
     */
    this.dmb = null;

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

    /**
     *
     * @type {Boolean}
     * @export
     */
    this.resultInTopLevel = false;


    const tenantDataElement = document.getElementById(tenantDataElementName);
    this.tenant = tenantDataElement.dataset['tenant'];

    $scope.$watch(() => (reportService.dmb_d), (nVal)=> {
      const dimension = $scope['dmbDimensionTab'];
      this.dmb = nVal ? nVal[dimension] : null;
      const dmbLevels = dmbLevelsFactory(this.dmb);
      this.currentLevel = dmbLevels.current;
      this.nextLevel = dmbLevels.next;
      this.resultInTopLevel = resultInTopLevel(this.dmb);

      this.dimensionHeader = tenantConf.dimensionHeaders[dimension];
      this.dimensionDescription = $sce.trustAsHtml(tenantConf.dimensionHeaderDescriptions[dimension]);

      this.dimensionLevelDescription = $sce.trustAsHtml(
        dmbLevelsFactory(
          this.dmb,
          tenantConf.dimensionLevelDescription[dimension]
        ).current.mapValue
      );

      this.recommendations = dmbLevelsFactory(
        this.dmb,
        tenantConf.dimensionRecommendations[dimension]
      ).current.mapValue;
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
