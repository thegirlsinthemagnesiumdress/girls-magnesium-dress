import {KEY_CODES} from '../../constants/key-codes';
import {FUZZY_CONSTS} from '../fuzzy-search/fuzzy-search';
import {csrfToken} from '../csrf/csrf';

const domSafe = goog.require('goog.dom.safe');
const creatorBaseUrl = '//moma.corp.google.com/person';
const addAccountEndpoint = 'admin/surveys/add';

const DATA_ATTRS = {
  SID: 'data-sid',
  SLUG: 'data-slug',
  VIEW: 'data-view',
  VIEW_LINK: 'data-view-link',
};

const ELEM_CONSTS = {
  ACCOUNT_DETAILS: {
    ATTR: 'dmb-account-details',
  },
  ACCOUNT_NAME: {
    ATTR: 'dmb-account-name',
  },
  ACCOUNT_ID: {
    ATTR: 'dmb-account-id',
  },
  ACCOUNT_INDUSTRY: {
    ATTR: 'dmb-account-industry',
  },
  ACCOUNT_COUTRY: {
    ATTR: 'dmb-account-country',
  },
  ACCOUNT_USER: {
    ATTR: 'dmb-account-user',
  },
  ADD_ACCOUNT_ERROR: {
    ATTR: 'dmb-add-account-error',
  },
  ADD_ACCOUNT_BTN: {
    ID: 'dmb-add-existing-account',
  },
  ACCOUNT_CREATOR_LINK: {
    ATTR: 'dmb-account-creator-link',
  },
  ACCOUNT_CREATOR_TEXT: {
    ATTR: 'dmb-account-creator-text',
  },
};

const VIEWS = {
  LOOKUP: 'account-lookup',
  DETAILS: 'account-details',
};

/**
 * Account page component to control the add account user flow
 *
 */
export default class AddAccountPage {
  /**
   * Attaches methods to provided element
   *
   * @param {Node} elem : Element to attach account page methods to
   *
   */
  constructor(elem) {
    this.elem = elem;
    this.slug = elem.getAttribute(DATA_ATTRS.SLUG);

    // Cache elements
    this.searchInputEl = elem.querySelector(`[${FUZZY_CONSTS.INPUT.ATTR}]`);
    this.searchInputEl.focus();

    this.addExistingAccountBtn = document.getElementById(ELEM_CONSTS.ADD_ACCOUNT_BTN.ID);

    this.viewLinks = elem.querySelectorAll(`[${DATA_ATTRS.VIEW_LINK}]`);

    this.accountDetailsEl = elem.querySelector(`[${ELEM_CONSTS.ACCOUNT_DETAILS.ATTR}]`);
    this.accountNameEl = this.accountDetailsEl.querySelector(`[${ELEM_CONSTS.ACCOUNT_NAME.ATTR}]`);
    this.accountIdEl = this.accountDetailsEl.querySelector(`[${ELEM_CONSTS.ACCOUNT_ID.ATTR}]`);
    this.accountIndustryEl = this.accountDetailsEl.querySelector(`[${ELEM_CONSTS.ACCOUNT_INDUSTRY.ATTR}]`);
    this.accountCountryEl = this.accountDetailsEl.querySelector(`[${ELEM_CONSTS.ACCOUNT_COUTRY.ATTR}]`);
    this.accountCreatorLinkEl = this.accountDetailsEl.querySelector(`[${ELEM_CONSTS.ACCOUNT_CREATOR_LINK.ATTR}]`);
    this.accountCreatorTextEl = this.accountDetailsEl.querySelector(`[${ELEM_CONSTS.ACCOUNT_CREATOR_TEXT.ATTR}]`);

    this.serverErrorEl = elem.querySelector(`[${ELEM_CONSTS.ADD_ACCOUNT_ERROR.ATTR}]`);

    // `this` bindings
    // mstrutt: NOT SURE IF THESE ARE NEEDED
    this.changeView = this.changeView.bind(this);
    this.changeViewOnEnter = this.changeViewOnEnter.bind(this);
    this.populateAccountDetails = this.populateAccountDetails.bind(this);
    this.addExistingAccount = this.addExistingAccount.bind(this);
    this.addExistingAccountOnEnter = this.addExistingAccountOnEnter.bind(this);

    // Attach event handlers
    this.viewLinks.forEach((elem) => {
      const view = elem.getAttribute(DATA_ATTRS.VIEW_LINK);
      elem.addEventListener('click', () => this.changeView(view));
      elem.addEventListener('keyup', (e) => this.changeViewOnEnter(e, view));
    });

    window.addEventListener('selectResult', this.populateAccountDetails);
    this.addExistingAccountBtn.addEventListener('click', this.addExistingAccount);
    this.addExistingAccountBtn.addEventListener('keyup', this.addExistingAccountOnEnter);
  }

  /**
   * Attaches AddAccountPage functionality to element
   *
   * @param {Node} elem : Element to attach AddAccountPage to
   * @return {AddAccountPage} : Returns a reference to the AddAccountPage instance created
   */
  static attachTo(elem) {
    return new AddAccountPage(elem);
  }


  /**
   * Populates the account details card and shows the account details view
   *
   * @param {Event} e : Event
   */
  populateAccountDetails(e) {
    if (!e.detail) {
      return;
    }

    const account = e.detail;

    const ldap = account['creator'] ? account['creator']['ldap'] : 'Not referred by a googler';

    this.accountDetailsEl.setAttribute(DATA_ATTRS.SID, account['sid']);
    this.accountNameEl.textContent = account['company_name'];
    this.accountIdEl.textContent = account['account_id'];
    this.accountIndustryEl.textContent = account['industry_name'];
    this.accountCountryEl.textContent = account['country_name'];

    if (account['creator']) {  
      domSafe.setAnchorHref(this.accountCreatorLinkEl, `${creatorBaseUrl}/${ldap}`);
    }

    this.accountCreatorTextEl.textContent = ldap;

    this.changeView(VIEWS.DETAILS);
  }

  // ////////////////////////////////////
  // MSTRUTT: can we combine these together?
  /**
   * Adds exisitng account on Enter key press
   *
   * @param {Event} e : Event
   */
  addExistingAccountOnEnter(e) {
    const keyCode = e.keyCode ? e.keyCode : e.which;

    if (keyCode === KEY_CODES.ENTER) {
      this.addExistingAccount();
    }
  }

  /**
   * Change view when Enter key pressed on view change buttons
   *
   * @param {Event} e : Event
   * @param {string} newView : the new view to change to
   *
   */
  changeViewOnEnter(e, newView) {
    const keyCode = e.keyCode ? e.keyCode : e.which;

    if (keyCode === KEY_CODES.ENTER) {
      this.changeView(newView);
    }
  }
  // ////////////////////////////////////

  /**
   * Change the view
   *
   * @param {string} newView : New view name
   *
   */
  changeView(newView) {
    this.elem.setAttribute(DATA_ATTRS.VIEW, newView);

    if (newView === VIEWS.LOOKUP) {
      this.searchInputEl.focus();
      return;
    }

    if (newView === VIEWS.DETAILS) {
      this.serverErrorEl.style.display = 'none';
      return;
    }
  }


  /**
   * Add existing account to user's accounts
   *
   */
  addExistingAccount() {
    const sid = this.accountDetailsEl.getAttribute(DATA_ATTRS.SID);

    fetch(
      `/api/${this.slug}/${addAccountEndpoint}/${sid}/`,
      {
        method: 'PUT',
        headers: {
          'X-CSRFToken': csrfToken,
        },
      })
      .then((resp) => {
        if (resp.status !== 201 && resp.status !== 200) {
          return Promise.reject(`HTTP error status code: ${resp.status}`);
        }

        domSafe.setLocationHref(document.location, `/${this.slug}/admin/accounts/${sid}`);
      })
      .catch(() => {
        this.serverErrorEl.style.display = 'block';
      });
  }
}
