goog.module('dmb.components.report.service');


/**
 * Report class service
 * We had to create this service because Glue Tabs mess the scopes
 * and it's not possible to pass an asyncronous value to the tab inner directive.
 * We use a service to share this data between report controller and
 * tab dimension directive.
 */
class ReportService {
  /**
   * Report service constructor.
   *
   * @ngInject
   */
  constructor() {
    /**
     * @export
     * @type {Object}
     *
     */
    this.dmb_d = {};

    /**
     * @type {Object}
     * @export
     *
     */
    this.industryDmb_d = {};
  }
}

ReportService.SERVICE_NAME = 'reportService';


exports = {
  main: ReportService,
  SERVICE_NAME: ReportService.SERVICE_NAME,
};
