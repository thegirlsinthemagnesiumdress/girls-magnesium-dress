goog.module('dmb.components.report.controller');

const surveyEndpoint = '/api/report/company/';
const industryEndpoint = '/api/report/industry/';
const locationSidRegex = /\/(\w+)[\/\!\?#]?[^\/]*$/;


/**
 * Report class controller
 */
class ReportController {
  /**
   * Report controller
   *
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @param {!object} reportService
   * @param {!object} floorDmbFactory
   * @constructor
   * @ngInject
   */
  constructor($http, $location, reportService, floorDmbFactory) {
    const sidMatches = $location.absUrl().match(locationSidRegex);
    const surveyId = sidMatches ? sidMatches[1] : null;

    /**
     * Survey object.
     * @type {object}
     * @export
     */
    this.survey = null;

    /**
     * Survey result object.
     * @type {object}
     * @export
     */
    this.result = null;

    /**
     * Floored dmb
     * @type {number}
     * @export
     */
    this.floorDmb = null;

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
     * @type {object}
     * @export
     */
    this.industryResult = null;

    // We're saving the results in a service since it's not possible to
    // directly pass them to the directive throught the bindings since
    // the tab component messes up the scopes. We use a service instead.
    $http.get(`${surveyEndpoint}${surveyId}`).then((res)=> {
      this.survey = res.data;
      this.result = this.survey.last_survey_result;
      this.floorDmb = floorDmbFactory(this.result.dmb);

      reportService.dmb_d = this.result.dmb_d;

      $http.get(`${industryEndpoint}${this.survey.industry}`).then((res) => {
        this.industryResult = res.data;
        reportService.industryDmb_d = this.industryResult.dmb_d;
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
