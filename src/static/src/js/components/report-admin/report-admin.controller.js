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
     * @type {Array.<Object>}
     * @export
     */
    this.surveys = bootstrapData['surveys'];
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
