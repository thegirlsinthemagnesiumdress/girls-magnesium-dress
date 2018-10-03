goog.module('dmb.components.registration.controller');

const SURVEY_ENDPOINT = '/api/survey';


/**
 * Registration controller.
 */
class RegistrationController {
  /**
   *
   * @param {!angular.$http} $http
   * @param {!angular.Scope} $scope
   * @param {!angular.$location} $location
   * @param {!Object} csrfToken
   * @ngInject
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
    this.industry= '';

    /**
     * @export
     */
    this.country= '';

    /**
     * @export
     * @type {boolean}
     */
    this.serverError = false;

    const elMatches = $location.hash().match(/el=([^&]*)/);

    /**
     * @export
     */
    this.elId= elMatches ? elMatches[1] : null;

    /**
     * @export
     */
    this.link = '';
  }

  /**
   * Submit data to API endopoint
   * @export
   */
  submit() {
    let data = {
      'company_name': this.companyName,
      'industry': this.industry,
      'country': this.country,
      'engagement_lead': this.engagementLead,
    };

    if (this.elId && !data['engagement_lead']) {
      data['engagement_lead'] = this.elId;
    }

    this.serverError = false;

    this._ngHttp.post(
      SURVEY_ENDPOINT,
      data, {
      headers: {
        'X-CSRFToken': this._csrfToken,
      },
    }).then((res) => {
      this.link = res.data.link;
    }, (res) => {
      this.serverError = true;
    });
  }

  /**
   * Resets the form.
   * @export
   */
  reset() {
    this.companyName = '';
    this.industry = '';
    this.country = '';
    this.link = '';
    this.serverError = '';
  }
}


/** @const {string} */
RegistrationController.CONTROLLER_NAME = 'RegistrationCtrl';


exports = {
  main: RegistrationController,
  CONTROLLER_NAME: RegistrationController.CONTROLLER_NAME,
};
