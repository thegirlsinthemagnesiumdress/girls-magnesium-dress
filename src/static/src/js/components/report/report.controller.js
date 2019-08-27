goog.module.declareNamespace('dmb.components.report.controller');

const surveyEndpoint = '/api/report/company/';
const resultEndpoint = '/api/report/result/';
const industryEndpoint = '/api/report/industry/';
const locationSidRegex = /reports\/(\w+)[#\/].*$/;
const resultResponseIdRegex = /reports\/result\/(\w+)[#\/].*$/;


/**
 * Report class controller
 */
class ReportController {
  /**
   * Report controller
   *
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @param {!angular.$timeout} $timeout
   * @param {!angular.$sce} $sce
   * @param {!Function} dmbLevelsFactory
   * @param {!Function} resultInTopLevel
   * @param {!Object} tenantConf
   * @param {!string} dmbStaticUrl
   *
   * @ngInject
   */
  constructor(
    $http,
    $location,
    $timeout,
    $sce,
    dmbLevelsFactory,
    resultInTopLevel,
    tenantConf,
    dmbStaticUrl) {
    const sidMatches = $location.absUrl().match(locationSidRegex);
    const responseIdMatches = $location.absUrl().match(resultResponseIdRegex);
    const surveyId = sidMatches ? sidMatches[1] : null;
    const responseId = responseIdMatches ? responseIdMatches[1] : null;

    // /** @private {!angular.$timeout} */
    // this.ngTimeout_ = $timeout;

    /**
     * @type {Object}
     * @export
     */
    this.tenantConf = tenantConf;

    /**
     * @type {Object}
     * @export
     */
    this.levels = tenantConf.levels;

    /**
     * @type {Array.<string>}
     * @export
     */
    this.levelsMin = tenantConf.levelsArray[0];

    /**
     * @type {String}
     * @export
     */
    this.levelsMax = tenantConf.levelsMax;

    /**
     * @type {!Object}
     * @export
     */
    this.levelDescriptions = tenantConf.levelDescriptions;

    /**
     * @type {!Object}
     * @export
     */
    this.reportLevelDescriptions = tenantConf.reportLevelDescriptions;

    /**
     * @type {!Object}
     * @export
     */
    this.industryAvgDescription = tenantConf.industryAvgDescription;

    /**
     * @type {!Object}
     * @export
     */
    this.industryBestDescription = tenantConf.industryBestDescription;

    /**
     * Industry result object
     * @type {Object}
     * @export
     */
    this.industryResult = null;

    /**
     * Industry best rating source industry
     * @type {Object}
     * @export
     */
    this.industryAvgSource = null;

    /**
     * Industry average source industry
     * @type {Object}
     * @export
     */
    this.industryBestSource = null;

    /**
     * @type {Array.<string>}
     * @export
     */
    this.dimensionList = tenantConf.dimensionList;

    /**
     * Dimensions object for dimension tabss
     * @type {Object}
     * @export
     */
    this.dimensions = {};

    /**
     * @type {string}
     * @export
     */
    this.dimensionSidepanelHeading = tenantConf.dimensionSidepanelHeading;

    /**
     * @type {!Object}
     * @export
     */
    this.dimensionSidepanelDescriptions = tenantConf.dimensionSidepanelDescriptions;

    /**
     *
     * @type {?number}
     * @export
     */
    this.overallResult = null;

    /**
     *
     * @type {Object}
     * @export
     */
    this.currentLevelData = {};

    /**
     *
     * @type {Object}
     * @export
     */
    this.nextLevelData = {};

    /**
     *
     * @type {Object}
     * @export
     */
    this.currentLevelDescription = {};

    /**
     * Survey object.
     * @type {Object}
     * @export
     */
    this.survey = null;

    /**
     * Survey result object.
     * @type {Object}
     * @export
     */
    this.result = null;

    /**
     * @type {!Object}
     * @export
     */
    this.subdimensionLists = tenantConf.subdimensionLists;

    /**
     * @type {!Object}
     * @export
     */
    this.subdimensions = {};

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportHeading = tenantConf.subdimensionsReportHeading;

    /**
     * @type {!Object}
     * @export
     */
    this.subdimensionsReportDescription = $sce.trustAsHtml(tenantConf.subdimensionsReportDescription);

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportCta = tenantConf.subdimensionsReportCta;

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsReportSubheading = tenantConf.subdimensionsReportSubheading;

    /**
     * @type {string}
     * @export
     */
    this.subdimensionsSidepanelHeading = tenantConf.subdimensionsSidepanelHeading;

    /**
     * @type {Object}
     * @export
     */
    this.subdimensionDescriptions = tenantConf.subdimensionDescriptions;

    /**
     *
     * @type {Function}
     * @export
     */
    this.dmbLevelsFactory = dmbLevelsFactory;

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
     *
     * @type {Function}
     * @export
     */
    this.trustAsHtml = $sce.trustAsHtml;


    // Allows use from other contexts
    this.setOverallResult = this.setOverallResult.bind(this);

    const reportEndpoint = responseId ? `${resultEndpoint}${responseId}` : `${surveyEndpoint}${surveyId}`;

    // Get report results
    $http.get(reportEndpoint).then((res)=> {
      this.survey = res.data;
      this.result = this.survey['survey_result'];
      this.result['dmb']

      // DRF returns decimal fields as strings. We should probably look into this
      // on the BE but until we do let's fix this on the FE
      this.setOverallResult(parseFloat(this.result['dmb']));

      // this.dimensionResults = this.result['dmb_d'];

      this.dimensionList.forEach((dimension) => {
        this.setDimensionResult(dimension, this.result['dmb_d'][dimension]);

        if (!this.subdimensionLists) {
          return
        }

        this.subdimensionLists[dimension].forEach((subdimension) => {
          this.setSubdimensionResult(subdimension, this.result['dmb_d'][subdimension]);
        })
      });


      // Get industry results
      $http.get(`${industryEndpoint}${this.survey['industry']}?tenant=${this.survey['tenant']}`).then((res) => {
        this.industryResult = res.data;
        this.industryAvgSource = this.industryResult['dmb_industry'];
        this.industryBestSource = this.industryResult['dmb_bp_industry'];

        this.dimensionList.forEach((dimension) => {
          if (this.industryResult['dmb_d']) {
            this.dimensions[dimension].indResults.average = this.industryResult['dmb_d'][dimension];
          }
          if (this.industryResult['dmb_d_bp']) {
            this.dimensions[dimension].indResults.best = this.industryResult['dmb_d_bp'][dimension];
          }
        });
      });
    });
  }

  /**
   * Sets values for overall result
   * @param {number} overallResult
   * @export
   */
  setOverallResult(overallResult) {
    if (!angular.isDefined(overallResult)) {
      return;
    }

    this.overallResult = overallResult;
    const levelData = this.dmbLevelsFactory(this.overallResult);
    this.currentLevelData = levelData['current'];
    this.nextLevelData = levelData['next'];
    const levelDescriptions = this.dmbLevelsFactory(
      this.overallResult,
      this.reportLevelDescriptions
    );
    this.currentLevelDescription = levelDescriptions['current']['mapValue'];
  }


  /**
   * Sets this.dimensions object with the correct data for a given dimension and a given result
   * @param {string} dimension
   * @param {number} value
   * @export
   */
  setDimensionResult(dimension, value) {
    if (!angular.isDefined(value)) {
      return;
    }

    const dimensionObj = {};

    dimensionObj.name = this.tenantConf.dimensionTitles[dimension];
    dimensionObj.description = this.trustAsHtml(
      this.tenantConf.dimensionHeaderDescriptions[dimension]
    );

    dimensionObj.result = value;

    const levelsData = this.dmbLevelsFactory(value);
    const dimensionCurrentLevelObject = levelsData.current;
    const dimensionNextLevelObject = levelsData.next;
    const dimensionLevel = levelsData.current.value;

    dimensionObj.levels = {
      current: {
        description: this.trustAsHtml(
          this.tenantConf.dimensionLevelDescription[dimension][dimensionLevel]
        ),
        name: dimensionCurrentLevelObject.mapValue,
        value: dimensionCurrentLevelObject.value,
      },
      next: {
        name: dimensionNextLevelObject.mapValue,
        value: dimensionNextLevelObject.value,
      },
    };

    dimensionObj.inTopLevel = this.resultInTopLevel(value);
    dimensionObj.recommendations = this.tenantConf.dimensionRecommendations[dimension][dimensionLevel];
    dimensionObj.indResults = {
      average: null,
      best: null,
    };

    this.dimensions[dimension] = dimensionObj;
  }

  /**
   * Sets this.subdimensions object with the correct data for a given subdimension and result
   * @param {string} subdimension
   * @param {number} value
   * @export
   */
  setSubdimensionResult(subdimension, value) {
    if (!angular.isDefined(value)) {
      return;
    }

    const dimensionObj = {};

    dimensionObj.name = this.tenantConf.subdimensionNames[subdimension];
    dimensionObj.description = this.trustAsHtml(
      this.tenantConf.subdimensionDescriptions[subdimension]
    );

    dimensionObj.result = value;

    const levelsData = this.dmbLevelsFactory(value);
    const dimensionCurrentLevelObject = levelsData.current;
    const dimensionNextLevelObject = levelsData.next;

    dimensionObj.levels = {
      current: {
        name: dimensionCurrentLevelObject.mapValue,
        value: dimensionCurrentLevelObject.value,
      },
      next: {
        name: dimensionNextLevelObject.mapValue,
        value: dimensionNextLevelObject.value,
      },
    };

    this.subdimensions[subdimension] = dimensionObj;
  }

  /**
   * @export
   */
  print() {
    window['print']();
  }
}


/** @const {string} */
ReportController.CONTROLLER_NAME = 'ReportCtrl';


/** @const {string} */
ReportController.CONTROLLER_AS_NAME = 'reportCtrl';


export const main = ReportController;
export const CONTROLLER_NAME = ReportController.CONTROLLER_NAME;
export const CONTROLLER_AS_NAME = ReportController.CONTROLLER_AS_NAME;
