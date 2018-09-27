goog.module('dmb.components.report.controller');

const surveyEndpoint = '/api/report/company/';
const industryEndpoint = '/api/report/industry/';
const locationSidRegex = /\/(\w+)[^\/\!\?#]?[^\/]*$/;

const PaginationModel = goog.require('glue.ng.pagination.Model');


/**
 * Report class controller
 */
class ReportController {
  /**
   * Report controller
   *
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @param {!Object} reportService
   * @param {!Function} floorDmbFactory
   * @param {!Object} dimensionHeaders
   *
   * @ngInject
   */
  constructor(
      $http,
      $location,
      reportService,
      floorDmbFactory,
      dimensionHeaders,
      glueState,
      $timeout) {
    const sidMatches = $location.absUrl().match(locationSidRegex);
    const surveyId = sidMatches ? sidMatches[1] : null;

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
     * Floored dmb
     * @type {?number}
     * @export
     */
    this.floorDmb = null;

    /**
     * Floored dmb
     * @type {!object}
     * @export
     */
    this.dimensionHeaders = dimensionHeaders;

    this.model = new PaginationModel();

    /** @private {!angular.$timeout} */
    this.ngTimeout_ = $timeout;

    /**
     * @export
     * @type {Array.<string>}
     */
    this.dimensions = [
      'attribution',
      'ads',
      'audience',
      'access',
      'automation',
      'organization',
    ];


    /**
     * Industry result object.
     * @type {Object}
     * @export
     */
    this.industryResult = null;

    // We're saving the results in a service since it's not possible to
    // directly pass them to the directive throught the bindings since
    // the tab component messes up the scopes. We use a service instead.
    $http.get(`${surveyEndpoint}${surveyId}`).then((res)=> {
      this.survey = res.data;
      this.result = this.survey['last_survey_result'];

      // DRF returns decimal fields as strings. We should probably look into this
      // on the BE but until we do let's fix this on the FE.
      this.result.dmb = parseFloat(this.result['dmb']);

      this.floorDmb = floorDmbFactory(this.result.dmb);

      reportService.dmb_d = this.result['dmb_d'];

      $http.get(`${industryEndpoint}${this.survey['industry']}`).then((res) => {
        this.industryResult = res.data;
        reportService.industryDmb_d = this.industryResult['dmb_d'];
        reportService.industryDmb_d_bp = this.industryResult['dmb_d_bp'];
      });
    });
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
