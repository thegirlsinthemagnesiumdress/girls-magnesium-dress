/**
 * Report class service
 * We had to create this service because Glue Tabs mess the scopes
 * and it's not possible to pass an asynchronous value to the tab inner directive.
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

    /**
     * @type {Object}
     * @export
     *
     */
    this.industryDmb_bp = {};

    /**
     * @type {Object}
     * @export
     *
     */
    this.industryResult = null;
  }
}

ReportService.SERVICE_NAME = 'reportService';


export const main = ReportService;
export const SERVICE_NAME = ReportService.SERVICE_NAME;
