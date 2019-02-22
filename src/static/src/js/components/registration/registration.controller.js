goog.module('dmb.components.registration.controller');

const SURVEY_ENDPOINT = '/api/survey';
const CREATE_SURVEY = 'createsurvey';

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
     * @type{string}
     */
    this.companyName= '';

    /**
     * @export
     * @type{string}
     */
    this.industry= '';

    /**
     * @export
     * @type{string}
     */
    this.distributionChannel= '';

    /**
     * @export
     * @type{string}
     */
    this.country= '';

    /**
     * @export
     * @type{string}
     */
    this.engagementLead= '';

    /**
     * @export
     * @type{string}
     *
     * Get tenant from URL structure: url/<tenant>/createsurvey/
     *
     */
    this.tenant = $location.absUrl().split(`/${CREATE_SURVEY}`)[0].split(`/`).pop();

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
      'tenant': this.tenant,
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
      this.link = res['data']['link'];
      this.companyName = res['data']['company_name'];
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
    this.serverError = false;
  }
}


/** @const {string} */
RegistrationController.CONTROLLER_NAME = 'RegistrationCtrl';


exports = {
  main: RegistrationController,
  CONTROLLER_NAME: RegistrationController.CONTROLLER_NAME,
};
