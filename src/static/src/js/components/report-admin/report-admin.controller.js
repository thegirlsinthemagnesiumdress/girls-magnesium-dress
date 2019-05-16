goog.module('dmb.components.reportAdmin.controller');

/**
 * ReportAdmin class controller.
 */
class ReportAdminController {
  /**
   * ReportAdmin controller
   *
   * @param {Object} bootstrapData
   *
   * @ngInject
   */
  constructor(bootstrapData) {
    /**
     * Whether a row with nested report row is expanded or not.
     * @type {Object}
     * @export
     */
    this.expandedRows = {};

    /**
     * @type {Object}
     * @export
     */
    this.bootstrapData = bootstrapData;

    /**
     * @type {Array.<Object>}
     * @export
     */
    this.surveys = this.bootstrapData['results'];
  }


  /**
   * Function to toggle the view of nested rows using the 'View history' button
   * in the reports list
   * @param {number} rowIndex
   * @export
   */
  viewHistory(rowIndex) {
    this.expandedRows[rowIndex] = !this.expandedRows[rowIndex];
  }
}


/** @const {string} */
ReportAdminController.CONTROLLER_NAME = 'ReportAdminCtrl';


/** @const {string} */
ReportAdminController.CONTROLLER_AS_NAME = 'reportAdminCtrl';


exports = {
  main: ReportAdminController,
  CONTROLLER_NAME: ReportAdminController.CONTROLLER_NAME,
  CONTROLLER_AS_NAME: ReportAdminController.CONTROLLER_AS_NAME,
};
