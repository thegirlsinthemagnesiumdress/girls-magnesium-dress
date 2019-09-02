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
    }, (err) => {
      this.exportError = true;
      console.error(err);
    }).finally(()=> {
      this.showToast = true;
      this.submitting = false;
      this.timeout(() => {
        this.showToast = false;
      }, 7000);
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
