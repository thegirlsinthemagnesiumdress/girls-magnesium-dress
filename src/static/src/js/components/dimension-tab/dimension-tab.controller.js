goog.module('dmb.components.dimensionTab.controller');

// const tenantDataElementName = 'bootstrap-data';

/**
 * DimensionTab class controller.
 */
class DimensionTabController {
  /**
   * DimensionTab controller
   *
   * @param {!angular.$sce} $sce
   * @param {!Function} dmbLevelsFactory
   * @param {!Function} resultInTopLevel
   * @param {!Object} tenantConf
   * @param {!string} dmbStaticUrl
   *
   * @ngInject
   */
  constructor(
    $sce,
    dmbLevelsFactory,
    resultInTopLevel,
    tenantConf,
    dmbStaticUrl) {
    /**
     * @type {string}
     * @export
     */
    this.companyName;

    /**
     * @type {string}
     * @export
     */
    this.dmbDimensionTab;

    /**
     * @type {?number}
     * @export
     */
    this.dimensionResult;

    /**
     * @type {?number}
     * @export
     */
    this.dimensionIndAvg;

    /**
     * @type {?number}
     * @export
     */
    this.dimensionIndBest;

    /**
     * @type {Object}
     * @export
     */
    this.dimensionIndReady;

    /**
     * @type {string}
     * @export
     */
    this.tenant;


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
    this.recommendations = {};

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
     * @type {boolean}
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
     * @type {Object}
     * @export
     */
    this.tenantConf = tenantConf;

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
    this.updateDimensionTabData();
  }

  /**
   * updates the levels data for from dmbLevelsFactory
   */
  updateDimensionTabData() {
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
      ).current['mapValue']
    );

    this.recommendations = this.dmbLevelsFactory(
      this.dimensionResult,
      this.tenantConf.dimensionRecommendations[this.dmbDimensionTab]
    ).current['mapValue'];
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
