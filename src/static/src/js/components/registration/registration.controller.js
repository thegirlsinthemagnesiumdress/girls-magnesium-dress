goog.module('dmb.components.registration.controller');
const domSafe = goog.require('goog.dom.safe');

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
     * @type{string}
     */
    this.accountId;

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
    this.tenant = '';

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

    /**
     * @export
     * @type {boolean}
     */
    this.hideConfirmationPage = false;
  }

  /**
   * Submit data to API endopoint
   * @export
   */
  submit() {
    this.serverError = false;

    let data = {
      'account_id': this.accountId,
      'company_name': this.companyName,
      'industry': this.industry,
      'country': this.country,
      'engagement_lead': this.engagementLead,
      'tenant': this.tenant,
    };

    if (this.elId && !data['engagement_lead']) {
      data['engagement_lead'] = this.elId;
    }

    this._ngHttp.post(
      SURVEY_ENDPOINT,
      data, {
      headers: {
        'X-CSRFToken': this._csrfToken,
      },
    }).then((res) => {
      if (this.hideConfirmationPage) {
        // go redirect to qualtrics survey page
        domSafe.setLocationHref(document.location, res['data']['link']);
      } else {
        // legacy for reports list page where no redirect is required
        this.link = res['data']['link'];
        this.companyName = res['data']['company_name'];
      }
    }, () => {
      this.serverError = true;
    });
  }

  /**
   * Resets the form.
   * @export
   */
  reset() {
    this.accountId = '';
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
