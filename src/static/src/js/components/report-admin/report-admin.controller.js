goog.module('dmb.components.reportAdmin.controller');

const accountIdInputClass = '.dmb-reports-admin__table-account-input';

/**
 * ReportAdmin class controller.
 */
class ReportAdminController {
  /**
   * ReportAdmin controller
   *
   * @param {!angular.$http} $http
   * @param {String} csrfToken
   * @param {Object} bootstrapData
   * @ngInject
   */
  constructor($http, csrfToken, bootstrapData) {
    this._ngHttp = $http;
    this._csrfToken = csrfToken;

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

    /**
     * @type {Array.<Object>}
     * @export
     */
    this.newAccountIds = [];

    this.surveys.forEach((survey) => {
      this.newAccountIds.push(survey['account_id']);
    });

    /**
     * @type {String}
     * @export
     */
    this.rowToEdit = null;

    /**
     * @type {boolean}
     * @export
     */
    this.submitting = false;

    /**
     * @type {boolean}
     * @export
     */
    this.serverError = false;
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

  /**
   * Show the form for editing the account ID and focus on the input
   *
   * @param {!Object} event
   * @param {String} rowIndex
   * @export
   */
  editAccountID(event, rowIndex) {
    const index = parseInt(rowIndex, 10);
    this.rowToEdit = rowIndex;

    // this.newAccountIds used to link value of each input box used for editing account ID with the account ID.
    // This means they can be edited in the input box without chaging the view in the table.
    // The table view is only changed upon successful PUT request
    this.newAccountIds[index] = this.surveys[index]['account_id'];

    // Give focus to input box. Need to wait until the edit account ID form is visible before focussing on the input.
    const accountIdInput = event.currentTarget.parentElement.querySelectorAll(accountIdInputClass)[0];

    window.setTimeout(() => {
      accountIdInput.focus();
    });
  }

  /**
   * Cancel edit of account ID
   *
   * @export
   */
  cancelAccountIDEdit() {
    this.rowToEdit = null;
  }

  /**
   * Submit account ID
   *
   * @param {!Object} event
   * @param {String} rowIndex
   * @export
   */
  submitAccountIDEdit(event, rowIndex) {
    event.preventDefault();
    this.serverError = false;

    const index = parseInt(rowIndex, 10);

    // take newAccountId for given row from user input
    const newAccountId = this.newAccountIds[index];

    let data = {
      'account_id': newAccountId,
    };

    // prevent 'Enter' key from submitting form when no change has been made
    if (this.newAccountIds[index] === this.surveys[index]['account_id']) {
      this.cancelAccountIDEdit();
      return;
    }

    this.submitting = true;

    this._ngHttp.put(
      event.currentTarget.dataset.url,
      data, {
      headers: {
        'X-CSRFToken': this._csrfToken,
      },
    }).then(() => {
      this.surveys[index]['account_id'] = newAccountId;
    }, (err) => {
      this.serverError = true;
      window['alert']('Account ID not changed due to server error!');
      console.error(err.data);
    }).then(() => {
      this.rowToEdit = null;
      this.submitting = false;
    });
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
