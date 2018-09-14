goog.module('dmb.components.report.controller');

const surveyEndpoint = '/api/report/company/';
const industryEndpoint = '/api/report/industry/';
const locationSidRegex = /\/(\w+)[\/!?#$]/;


/**
 * Report class controller
 */
class ReportController {
  /**
   * Report controller
   *
   * @param {!angular.$http} $http
   * @param {!angular.$location} $location
   * @constructor
   * @ngInject
   */
  constructor($http, $location) {
    const sidMatches = $location.absUrl().match(locationSidRegex);

    const surveyId = sidMatches ? sidMatches[1] : null;

    $http.get(`${surveyEndpoint}${surveyId}`).then((res)=> {
      this.survey = res.data;
      this.result = this.survey.last_survey_result;
      this.companyDmb = this.result.dmb / 4 * 100;
      $http.get(`${industryEndpoint}${this.survey.industry}`).then((res) => {
        this.industry = res.data;
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
