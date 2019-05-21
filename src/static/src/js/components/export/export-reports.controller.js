goog.module('dmb.components.exportReports.controller');

/**
 * Export reports controller
 */
class ExportReportsController {
  /**
   *
   * @param {!angular.$http} $http
   * @param {!Object} csrfToken
   * @ngInject
   */
  constructor($http, csrfToken) {
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
  }

  /**
   * Export report data
   * @export
   * @param {!Object} event
   * @param {String} engagementLead
   */
  export(event, engagementLead) {
    event.preventDefault();

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
    });
  }

  /**
   * Reset export to try again
   * @export
   */
  resetExport() {
    this.exportError = false;
    this.exportSuccess = false;
  }
}


/** @const {string} */
ExportReportsController.CONTROLLER_NAME = 'ExportReportsCtrl';


exports = {
  main: ExportReportsController,
  CONTROLLER_NAME: ExportReportsController.CONTROLLER_NAME,
};
