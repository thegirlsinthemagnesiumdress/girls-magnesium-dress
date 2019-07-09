// goog.module('dmb.components.report.controller');
goog.module.declareNamespace('dmb.components.report.controller');

import * as BreakpointService from '@google/glue/lib/ng/common/breakpoint-service';
import * as PaginationModel from '@google/glue/lib/ng/pagination/model';

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
   * @param {!angular.Scope} $scope
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @param {!glue.ng.state.StateService} glueState
   * @param {!angular.$timeout} $timeout
   * @param {!angular.$sce} $sce
   * @param {!Function} dmbLevelsFactory
   * @param {!Function} resultInTopLevel
   * @param {!Object} tenantConf
   * @param {!Object} glueBreakpoint
   * @param {!string} dmbStaticUrl
   *
   * @ngInject
   */
  constructor(
    $scope,
      $http,
      $location,
      glueState,
      $timeout,
      $sce,
      dmbLevelsFactory,
      resultInTopLevel,
      tenantConf,
      glueBreakpoint,
      dmbStaticUrl) {
    const sidMatches = $location.absUrl().match(locationSidRegex);
    const responseIdMatches = $location.absUrl().match(resultResponseIdRegex);
    const surveyId = sidMatches ? sidMatches[1] : null;
    const responseId = responseIdMatches ? responseIdMatches[1] : null;

    /** @private {!glue.ng.state.StateService} */
    this.glueState_ = glueState;

    /** @private {!angular.$timeout} */
    this.ngTimeout_ = $timeout;

    /**
     * @export
     * @type {boolean}
     */
    this.renderTabset = false;

    /**
     *  Show dimensions tab (instead of the zippy).
     * @type {!boolean}
     * @export
     */
    this.showTabs = this.showTabs_(glueBreakpoint.getBreakpointSize());


    /**
     * @export
     * @type {Object}
     */
    this.levels = tenantConf.levels;

    /**
     * @export
     * @type {String}
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
     * Industry result object.
     * @type {Object}
     * @export
     */
    this.industryResult = null;

    /**
     * Industry best rating source industry.
     * @type {Object}
     * @export
     */
    this.industryAvgSource = null;

    /**
     * Industry average source industry.
     * @type {Object}
     * @export
     */
    this.industryBestSource = null;


    /**
     * @export
     * @type {Array.<string>}
     */
    this.dimensions = tenantConf.dimensions;

    /**
     * @export
     * @type {Object}
     */
    this.dimensionsResults = {};

    /**
     * @export
     * @type {Object}
     */
    this.dimensionsIndAvgs = {};

    /**
     * @export
     * @type {Object}
     */
    this.dimensionsIndBests = {};

    /**
     * @type {!Object}
     * @export
     */
    this.dimensionHeaders = tenantConf.dimensionHeaders;

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
     * @type {glue.ng.pagination.Model}
     * @export
     */
    this.model = new PaginationModel({
      'activeEl': this.dimensions[0],
    });

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
     *
     * @type {Function}
     * @export
     */
    this.trustAsHtml = $sce.trustAsHtml;


    /**
     * @type {!Object}
     * @export
     */
    this.subdimensions = tenantConf.subdimensions;

    /**
     * @type {!Object}
     * @export
     */
    this.subdimensionDescription = $sce.trustAsHtml(tenantConf.subdimensionDescription);

    /**
     * @type {Object}
     * @export
     */
    this.subdimensionHeaders = tenantConf.subdimensionHeaders;

    /**
     * @export
     * @type {string}
     */
    this.dmbStaticUrl = dmbStaticUrl;

    /**
     * @type {Object}
     * @export
     */
    this.subdimensionDescriptions = tenantConf.subdimensionDescriptions;

    // Allows use from other contexts
    this.setOverallResult = this.setOverallResult.bind(this);

    const reportEndpoint = responseId ? `${resultEndpoint}${responseId}` : `${surveyEndpoint}${surveyId}`;

    // We're saving the results in a service since it's not possible to
    // directly pass them to the directive throught the bindings since
    // the tab component messes up the scopes. We use a service instead.
    $http.get(reportEndpoint).then((res)=> {
      this.survey = res.data;
      this.result = this.survey['survey_result'];

      // DRF returns decimal fields as strings. We should probably look into this
      // on the BE but until we do let's fix this on the FE
      this.setOverallResult(parseFloat(this.result['dmb']));
      this.dimensionsResults = this.result['dmb_d'];

      // // ENABLE TO TEST OPTIONAL DIMENSION IN NEWS
      // // reportService.dmb_d['reader_revenue'] = null;

      this.ngTimeout_(() => {
        this.renderTabset = true;
      }, 0, true);


      $http.get(`${industryEndpoint}${this.survey['industry']}?tenant=${this.survey['tenant']}`).then((res) => {
        this.industryResult = res.data;
        this.industryAvgSource = this.industryResult['dmb_industry'];
        this.industryBestSource = this.industryResult['dmb_bp_industry'];

        this.dimensionsIndAvgs = this.industryResult['dmb_d'];
        this.dimensionsIndBests = this.industryResult['dmb_d_bp'];
      });
    });

    $scope.$on(BreakpointService.Service.BREAK_POINT_UPDATE_EVENT, (e, size) => {
      this.showTabs= this.showTabs_(size);
      $scope.$apply();
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
   * Sets values for overall result
   * @param {string} dimension
   * @param {number} newValue
   */
  setDimensionsResult(dimension, newValue) {
    if (!angular.isDefined(newValue)) {
      return;
    }

    this.dimensionsResults[dimension] = newValue;
  }

  /**
   *  @param {string} size
   *  @return {boolean}
   *  @private
   */
  showTabs_(size) {
    const bpTabsEnabled = [
      'large',
      'x-large',
      'xx-large',
      'medium-large',
      'medium',
    ];

    return bpTabsEnabled.indexOf(size) > -1;
  }

  /**
   * Opens a specific tab if state is enabled. This is expected to be used with
   * something like ngClick.
   *
   * @param {string} tabsetId The unique state id for the tabset.
   * @param {string} elementId The unique id of the tab to open.
   * @export
   */
  selectTab(tabsetId, elementId) {
    this.ngTimeout_(() => {
      this.glueState_.setState(tabsetId, {
        'activeEl': elementId,
      });
    }, 0, true);
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
