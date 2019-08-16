goog.module.declareNamespace('dmb.components.exportReports.controller');

const TOAST_SUCCESS_MESSAGE = `Data export requested. This may take up to 5 minutes. Please check your email inbox.`;
const TOAST_ERROR_MESSAGE = `Sorry there was an error, please try again`;

/**
 * Export reports controller
 */
class ExportReportsController {
  /**
   *
   * @param {!angular.$http} $http
   * @param {!angular.$timeout} $timeout
   * @param {!Object} csrfToken
   * @ngInject
   */
  constructor($http, $timeout, csrfToken) {
    this._ngHttp = $http;
    this._csrfToken = csrfToken;

    /**
     * @export
     * @type {boolean}
     */
    this.exportSuccess = false;

    /**
     * @export
     * @type {boolean}
     */
    this.exportError = false;

    /**
     * @export
     * @type {boolean}
     */
    this.submiting = false;

    /**
     * @export
     * @type {boolean}
     */
    this.showToast = false;

    /**
     * @export
     * @type {string}
     */
    this.toastText = '';

    /**
     * @export
     * @type {Function}
     */
    this.timeout = $timeout;
  }

  /**
   * Export report data
   * @export
   * @param {!Object} event
   * @param {String} engagementLead
   */
  export(event, engagementLead) {
    event.preventDefault();
    this.submitting = true;

    let data = {
      'engagement_lead': engagementLead,
    };

    this._ngHttp.post(
      event.currentTarget.action,
      data,
      {
        headers: {
          'X-CSRFToken': this._csrfToken,
        },
      }
    ).then(() => {
      this.exportSuccess = true;
      this.toastText = TOAST_SUCCESS_MESSAGE;
    }, (err) => {
      this.exportError = true;
      this.toastText = TOAST_ERROR_MESSAGE;
      console.error(err);
    }).finally(()=> {
      this.showToast = true;
      this.submitting = false;
      this.timeout(() => {
        this.showToast = false;
      }, 10000);
    });
  }

  /**
   * Reset export to try again
   * @export
   */
  resetExport() {
    this.exportError = false;
    this.exportSuccess = false;
    this.submitting = false;
    this.showToast = false;
  }
}


/** @const {string} */
ExportReportsController.CONTROLLER_NAME = 'ExportReportsCtrl';


export const main = ExportReportsController;
export const CONTROLLER_NAME = ExportReportsController.CONTROLLER_NAME;
