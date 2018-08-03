goog.module('dmb.components.registration.controller');

const SURVEY_ENDPOINT = '/api/survey';

/**
 * Registration controller.
 */
class RegistrationController {

  /**
   *
   * @param {!angular.$http} $http
   * @param {!angular.$scope} $scope
   * @param {!angular.$location} $location
   * @param {!object} csrfToken
   */
  constructor($http, $scope, $location, csrfToken) {
    this._ngHttp = $http;
    this._ngScope = $scope;
    this._csrfToken = csrfToken;

    /**
     * @export
     */
    this.companyName= '';

    /**
     * @export
     */
    const elMatches = $location.hash().match(/el=([^&]*)/);
    this.elId= elMatches ? elMatches[1] : null;

    /**
     * @export
     */
    this.link = '';
  }

  /**
   * Submit data to API endopoint
   */
  submit() {
    let data = {
      company_name: this.companyName,
    };

    if (this.elId) {
      data.engagement_lead = this.elId;
    }

    this._ngHttp.post(
      SURVEY_ENDPOINT,
      data, {
      headers: {
        'X-CSRFToken': this._csrfToken,
      },
    }).then((res) => {
      this.link = res.data.link;
    });
  }
}


/** @const {string} */
RegistrationController.CONTROLLER_NAME = 'RegistrationCtrl';


/** @const {string} */
RegistrationController.CONTROLLER_AS_NAME = 'RegistrationCtrl';


exports = {
  main: RegistrationController,
  CONTROLLER_NAME: RegistrationController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: RegistrationController.CONTROLLER_AS_NAME,
};
