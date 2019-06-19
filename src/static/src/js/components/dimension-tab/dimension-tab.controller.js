goog.module('dmb.components.dimensionTab.controller');

// const tenantDataElementName = 'bootstrap-data';

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
     * @type {Function}
     * @export
     */
    this.trustAsHtml = $sce.trustAsHtml;

    /**
     * @type {Function}
     * @export
     */
    this.dmbLevelsFactory = dmbLevelsFactory;

    /**
     *
     * @type {Boolean}
     * @export
     */
    this.topLevel = false;

    /**
     *
     * @type {Function}
     * @export
     */
    this.resultInTopLevel = resultInTopLevel;

    /**
     * @export
     * @type {string}
     */
    this.dmbStaticUrl = dmbStaticUrl;

    /**
     * @type {Object}
     * @export
     */
    this.tenantConf = tenantConf;

    /**
     * @type {string}
     * @export
     */
    this.dimensionHeader = '';

    /**
     * @type {string}
     * @export
     */
    this.dimensionDescription = '';

    /**
     * @type {string}
     * @export
     */
    this.dimensionLevelDescription = '';

    /**
     * @type {Object}
     * @export
     */
    this.currentLevelData = {};

    /**
     * @type {Object}
     * @export
     */
    this.nextLevelData = {};


    // /**
    //  * @type {Boolean}
    //  * @export
    //  */
    // this.industryReady = false;


    // /**
    //  * @type string
    //  * @export
    //  */
    // this.tenant = '';

    // /**
    //  * @type {!Object}
    //  * @export
    //  */
    // this.levels = tenantConf.levels;


    // /**
    //  * @export
    //  * @type {String}
    //  */
    // this.levelsMax = tenantConf.levelsMax;

    // /**
    //  * @export
    //  * @type {Object}
    //  */
    // this.currentLevel = {};

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.nextLevel = {};

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.dimensions = tenantConf.dimensions;

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.dimensionClassNames = {};

    // tenantConf.dimensions.forEach((dimension) => {
    //   this.dimensionClassNames[dimension] = dimension.replace(/_/g, '-');
    // });

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.recommendations = {};

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.dmb = null;

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.industryDmb = null;

    // /**
    //  * @type {Object}
    //  * @export
    //  */
    // this.industryDmb_bp = null;

    /**
     * @type {Boolean}
     * @export
     */
    this.dimensionIndReady = false;

    // /**
    //  * @type {!Object}
    //  */
    // this.reportService = reportService;

    // /**
    //  *
    //  * @type {Boolean}
    //  * @export
    //  */
    // this.resultInTopLevel = false;

    // const tenantDataElement = document.getElementById(tenantDataElementName);
    // this.tenant = tenantDataElement.dataset['tenant'];

    // $scope.$watch(() => (reportService.dmb_d), (nVal)=> {
    //   const dimension = $scope['dmbDimensionTab'];
    //   this.dmb = nVal ? nVal[dimension] : null;

    //   this.dimensionHeader = tenantConf.dimensionHeaders[dimension];
    //   this.dimensionDescription = $sce.trustAsHtml(tenantConf.dimensionHeaderDescriptions[dimension]);

    //   if (this.dmb) {
    //     const dmbLevels = dmbLevelsFactory(this.dmb);
    //     this.currentLevel = dmbLevels.current;
    //     this.nextLevel = dmbLevels.next;
    //     this.resultInTopLevel = resultInTopLevel(this.dmb);
    //     this.dimensionLevelDescription = $sce.trustAsHtml(
    //       dmbLevelsFactory(
    //         this.dmb,
    //         tenantConf.dimensionLevelDescription[dimension]
    //       ).current.mapValue
    //     );

    //     this.recommendations = dmbLevelsFactory(
    //       this.dmb,
    //       tenantConf.dimensionRecommendations[dimension]
    //     ).current.mapValue;
    //   }
    // });

    // $scope.$watch(() => (reportService.industryDmb_d), (nVal)=> {
    //   this.industryDmb = nVal ? nVal[$scope['dmbDimensionTab']] : null;
    // });

    // $scope.$watch(() => (reportService.industryDmb_d_bp), (nVal)=> {
    //   this.industryDmb_bp = nVal ? nVal[$scope['dmbDimensionTab']] : null;
    // });

    // $scope.$watch(() => (reportService.industryResult), (nVal)=> {
    //   this.industryResult = nVal;
    // });


    // Bind for external use
    this.updateDimensionTabData = this.updateDimensionTabData.bind(this);
  }

  /**
   * On scope initialisation update the values
   */
  $onInit() {
    this.updateDimensionTabData();
  }

  /**
   * Respond to property changes and update the values
   */
  $onChanges() {
    console.log('$onChanges');
    this.updateDimensionTabData();
  }

  /**
   * updates the levels data for from dmbLevelsFactory
   */
  updateDimensionTabData() {
    console.log('updateDimensionTabData');
    const levelData = this.dmbLevelsFactory(this.dimensionResult);
    this.currentLevelData = levelData.current;
    this.nextLevelData = levelData.next;

    this.topLevel = this.resultInTopLevel(this.dimensionResult);

    this.dimensionHeader = this.tenantConf.dimensionHeaders[this.dmbDimensionTab];
    this.dimensionDescription = this.trustAsHtml(
      this.tenantConf.dimensionHeaderDescriptions[this.dmbDimensionTab]
    );

    this.dimensionLevelDescription = this.trustAsHtml(
      this.dmbLevelsFactory(
        this.dimensionResult,
        this.tenantConf.dimensionLevelDescription[this.dmbDimensionTab]
      ).current.mapValue
    );

    this.recommendations = this.dmbLevelsFactory(
      this.dimensionResult,
      this.tenantConf.dimensionRecommendations[this.dmbDimensionTab]
    ).current.mapValue;
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
