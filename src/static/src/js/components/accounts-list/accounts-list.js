import {bootstrapData} from '../bootstrap/bootstrap-data';
const domSafe = goog.require('goog.dom.safe');

/**
 * Component for building out the AccountsList
 */
export default class AccountsList {
  /**
   * @param {Element} element
   * @return {AccountsList}
   */
  static attachTo(element) {
    return new AccountsList(element);
  }

  /**
   * @param {Element} element
   */
  constructor(element) {
    this.element = element;
    this.tbody = this.element.querySelector('tbody');
    this.accounts = bootstrapData['results'];

    if (this.tbody) {
      this.render();
    }
  }


  /**
   * Creating the data needed to build up the able view for each account
   * @param {Object} account
   * @return {Array.<Object>}
   */
  createColumnData(account) {
    /**
     * Format a number to a fixed number of decimal places, corrects the rounding issue of just using .toFixed()
     * @param {!number} number The number to format
     * @param {number=} dp (Optional) the number of decimal places to format to (defaults to 1)
     * @return {string}
     */
    function formatNumber(number, dp=1) {
      return (Math.round(number * 10) / 10).toFixed(dp);
    }

    const zeroWidthSpace = '​';
    return [
      {
        id: account['sid'],
        header: 'Organization',
        content: account['company_name'] || zeroWidthSpace,
      }, {
        id: account['sid'],
        header: 'Country',
        content: account['country_name'] || zeroWidthSpace,
      }, {
        id: account['sid'],
        header: 'Industry',
        content: account['industry_name'] || zeroWidthSpace,
      }, {
        id: account['sid'],
        header: 'Int. Maturity Score" class="h-c-table__cell--numerical',
        content: account['last_internal_result'] ?
            formatNumber(account['last_internal_result']['dmb']) : zeroWidthSpace,
      }, {
        id: account['sid'],
        header: 'Int. Maturity Level',
        content: account['internalCurrentLevelData'] ?
            account['internalCurrentLevelData']['mapValue'] : zeroWidthSpace,
      }, {
        id: account['sid'],
        header: 'Ext. Maturity Score" class="h-c-table__cell--numerical',
        content: account['last_survey_result'] ?
            formatNumber(account['last_survey_result']['dmb']) : zeroWidthSpace,
      }, {
        id: account['sid'],
        header: 'Ext. Maturity Level',
        content: account['externalCurrentLevelData'] ?
            account['externalCurrentLevelData']['mapValue'] : zeroWidthSpace,
      },
    ];
  }

  /**
   */
  render() {
    const accountsData = this.accounts.map(this.createColumnData);
    const newTbody = document.createElement('tbody');

    accountsData.forEach((accountColumns) => {
      const tr = document.createElement('tr');

      // Building the DOM this way so we're not interpreting content from the server as HTML.
      // Only ever as textContent or attribute values.
      accountColumns.forEach((column) => {
        const td = document.createElement('td');
        td.setAttribute('data-colheader', column.header);
        const a = document.createElement('a');
        domSafe.setAnchorHref(a, `${column.id}/`); // TODO (mstrutt) link should come from the backend
        // a.href = `${column.id}/`;
        a.textContent = column.content;
        td.appendChild(a);
        tr.appendChild(td);
      });

      newTbody.appendChild(tr);
    });

    // Although we're building the HTML up in a loop, this is the only point
    // at which it joins the DOM. Should cause only one reflow/pain
    this.tbody.parentNode.replaceChild(newTbody, this.tbody);
    this.tbody = newTbody;
  }
}
