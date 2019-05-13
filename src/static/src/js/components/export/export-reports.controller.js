goog.module('dmb.components.exportReports.controller');

/**
 * Export reports controller
 */
class ExportReportsController {
  /**
   *
   * @param {!angular.$http} $http
   * @param {!Object} csrfToken
   * @param {!Object} tenantConf
   * @ngInject
   */
  constructor($http, csrfToken, tenantConf) {
    this._ngHttp = $http;
    this._csrfToken = csrfToken;

    /**
     * Tenant
     * @export
     * @type {String}
     */
    this.tenant = tenantConf.tenant;

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
   * @param {String} engagementLead
   */
  export(event, engagementLead) {
    event.preventDefault();

    let data = {
      'engagement_lead': engagementLead,
      'tenant': this.tenant,
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
      console.error(`${err.data}`);
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
