goog.module('dmb.components.report.controller');

const BreakpointService = goog.require('glue.ng.common.Breakpoint');
const PaginationModel = goog.require('glue.ng.pagination.Model');

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
   * @param {!angular.Scope} $rootScope
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @param {!glue.ng.state.StateService} glueState
   * @param {!angular.$timeout} $timeout
   * @param {!angular.$sce} $sce
   * @param {!Object} reportService
   * @param {!Function} dmbLevelsFactory
   * @param {!Function} resultInTopLevel
   * @param {!Object} tenantConf
   * @param {!Object} glueBreakpoint
   *
   * @ngInject
   */
  constructor(
    $scope,
      $rootScope,
      $http,
      $location,
      glueState,
      $timeout,
      $sce,
      reportService,
      dmbLevelsFactory,
      resultInTopLevel,
      tenantConf,
      glueBreakpoint) {
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
     * @type {String}
     * @export
     */
    this.overallResult = null;

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
     *
     * @type {Function}
     * @export
     */
    this.dmbLevelsFactory = dmbLevelsFactory;

    /**
     *
     * @type {Boolean}
     * @export
     */
    this.resultInTopLevel = false;

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

    const reportEndpoint = responseId ? `${resultEndpoint}${responseId}` : `${surveyEndpoint}${surveyId}`;

    // We're saving the results in a service since it's not possible to
    // directly pass them to the directive throught the bindings since
    // the tab component messes up the scopes. We use a service instead.
    $http.get(reportEndpoint).then((res)=> {
      this.survey = res.data;
      this.result = this.survey['survey_result'];

      // DRF returns decimal fields as strings. We should probably look into this
      // on the BE but until we do let's fix this on the FE.
      // this.result.dmb = parseFloat(this.result['dmb']);
      this.overallResult = this.result['dmb'];

      const dmbLevels = dmbLevelsFactory(this.overallResult);
      this.currentLevel = dmbLevels.current;
      this.nextLevel = dmbLevels.next;
      this.resultInTopLevel = resultInTopLevel(this.overallResult);

      // //////////////////////////////////
      // this.result['dmb_d'] = {
      //   'learn': 2.3,
      //   'lead': 3.5,
      //   'scale': 4.5,
      //   'secure': 5,
      // };
      // //////////////////////////////////

      reportService.dmb_d = this.result['dmb_d'];

      // ENABLE TO TEST OPTIONAL DIMENSION IN NEWS
      // reportService.dmb_d['reader_revenue'] = null;

      for (let key in reportService.dmb_d) {
        if (reportService.dmb_d[key] === null) {
          this.dimensions.splice(this.dimensions.indexOf(key), 1);
        }
      }
      this.ngTimeout_(() => {
        this.renderTabset = true;
      }, 0, true);
      // //////////////


      $http.get(`${industryEndpoint}${this.survey['industry']}?tenant=${this.survey['tenant']}`).then((res) => {
        this.industryResult = res.data;
        this.industryAvgSource = this.industryResult['dmb_industry'];
        this.industryBestSource = this.industryResult['dmb_bp_industry'];
        reportService.industryResult = this.industryResult;
        reportService.industryDmb_d = this.industryResult['dmb_d'];
        reportService.industryDmb_d_bp = this.industryResult['dmb_d_bp'];
        $rootScope.$broadcast('content-updated');
      });
    });

    $scope.$on(BreakpointService.service.BREAK_POINT_UPDATE_EVENT, (e, size) => {
      this.showTabs= this.showTabs_(size);
      $scope.$apply();
    });
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


exports = {
  main: ReportController,
  CONTROLLER_NAME: ReportController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ReportController.CONTROLLER_AS_NAME,
};
