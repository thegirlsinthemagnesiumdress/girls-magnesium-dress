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
   * @param {!Object} reportService
   * @param {!Function} floorDmbFactory
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
      reportService,
      floorDmbFactory,
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
     * Floored dmb.
     * @type {?number}
     * @export
     */
    this.floorDmb = null;

    /**
     *  Show dimensions tab (instead of the zippy).
     * @type {!boolean}
     * @export
     */
    this.showTabs = this.showTabs_(glueBreakpoint.getBreakpointSize());

    /**
     * @type {!Object}
     * @export
     */
    this.levels = tenantConf.levels;

    /**
     * @type {!Object}
     * @export
     */
    this.levelDescriptions = tenantConf.levelDescriptions;

    /**
     * @export
     * @type {Array.<string>}
     */
    this.dimensions = tenantConf.dimensions;

    /**
     * @export
     * @type {string}
     */
    this.levelsTotal = Object.keys(this.levels).length;

    /**
     * @type {!Object}
     * @export
     */
    this.dimensionHeaders = tenantConf.dimensionHeaders;

       /**
     * @type {glue.ng.pagination.Model}
     * @export
     */
    this.model = new PaginationModel({
      'activeEl': this.dimensions[0],
    });

    /**
     * Industry result object.
     * @type {Object}
     * @export
     */
    this.industryResult = null;

    /**
     * Industry best rating source industry.
     * @const {string}
     * @export
     */
    this.industryAvgSource = null;

    /**
     * Industry average source industry.
     * @const {string}
     * @export
     */
    this.industryBestSource = null;

    /**
     * Whether to render tabset of not
     * @type {boolean}
     * @export
     */
    this.renderTabset = false;

    const reportEndpoint = responseId ? `${resultEndpoint}${responseId}` : `${surveyEndpoint}${surveyId}`;

    // We're saving the results in a service since it's not possible to
    // directly pass them to the directive throught the bindings since
    // the tab component messes up the scopes. We use a service instead.
    $http.get(reportEndpoint).then((res)=> {
      this.survey = res.data;
      this.result = this.survey['survey_result'];

      // DRF returns decimal fields as strings. We should probably look into this
      // on the BE but until we do let's fix this on the FE.
      this.result.dmb = parseFloat(this.result['dmb']);

      this.floorDmb = floorDmbFactory(this.result.dmb);

      reportService.dmb_d = this.result['dmb_d'];

      // ENABLE FOR DEMO
      // reportService.dmb_d['reader_revenue'] = null;

      // TODO(aabuelgasim): remove this chunk once new tabby is used
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
