import axios from 'axios'

const API_ENDPOINT = '/api/survey';

/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {
  form: '#registration-form',
  confirmationScreen: '.tr-registration__confirmation',
  submitBtn: 'button',
  confirmationPage: '#form-confirmation',
  csrf:'input[name=csrfmiddlewaretoken]',
  clipboard: '[data-clipboard-text]',
  surveyLink: '#survey-link',
  company: '.tr-registration__company-name',
  getStartedSponsor: '.tr-registration__start-sponsor'
};

/**
 * CSS Classes.
 * @enum {string}
 */
const CLASSES = {
  hidden: 'tr-u-display-none',
  formError: 'tr-registration__form--error'
}

/**
 * Custom Element Registration Class.
 * @extends {HTMLElement}
 */
export default class Registration extends HTMLElement {

  /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   */
  connectedCallback () {
    this.$form = this.querySelector(DOM_SELECTORS.form);
    this.$template = this.querySelector(DOM_SELECTORS.confirmationPage);
    this.$formError = this.querySelector(DOM_SELECTORS.confirmationPage);
    this.$submitBtn = this.$form.querySelector(DOM_SELECTORS.submitBtn);
    this.$confirmationScreen = this.querySelector(DOM_SELECTORS.confirmationScreen);
    this.$form.addEventListener('submit', this.generateConfirmation.bind(this));
    this.$form.addEventListener('input', this.formChange.bind(this));

    this.csrf = this.$form.querySelector(DOM_SELECTORS.csrf).value;
  }

  /**
   * Form input event handler.
   * @param {event} e Input event.
   */
  formChange (e) {
    const isValid = this.$form.checkValidity();
    this.$submitBtn.disabled = !isValid;
  }

  /**
   * Retrieves the template and populate it with the data passed in.
   *
   * @param {object} context Template context.
   * @return {HtmlElement} Confirmation element.
   */
  getConfirmationNode (context) {
    let template = this.$template.textContent;
    const confirmationNode = document.createRange().createContextualFragment(template);

    // Set survey link.
    const surveyLinkNode = confirmationNode.querySelector(DOM_SELECTORS.surveyLink);
    surveyLinkNode.textContent = context.link;
    surveyLinkNode.setAttribute('href', context.link);

    // Set clipboard text attribute with link.
    confirmationNode.querySelector(DOM_SELECTORS.clipboard).setAttribute('data-clipboard-text', context.link);

    // Set company name.
    confirmationNode.querySelector(DOM_SELECTORS.company).textContent = context.company_name;

    // Set sponsor link href.
    confirmationNode.querySelector(DOM_SELECTORS.getStartedSponsor).setAttribute('href', context.link_sponsor);

    return confirmationNode;
  }

  /**
   * Posts the company name to the server and updates UI with confirmation
   * page.
   * @param {*} e
   */
  generateConfirmation (e) {
    // Show step two.
    this.$form.classList.remove(CLASSES.formError);
    const postData = {
      'company_name': this.$form.elements['company_name'].value
    };

    axios.post(API_ENDPOINT, postData, {
      headers: {
        'X-CSRFToken': this.csrf,
      }
    })
      .then((res) => {
        this.$form.parentNode.insertBefore(this.getConfirmationNode(res.data), this.$form.nextElementSibling);
        // Initialize clipboard.
        new ClipboardJS(DOM_SELECTORS.clipboard); // eslint-disable-line
        this.$form.classList.add(CLASSES.hidden);
        this.$form.reset();
      }, () => {
        // Show error
        this.$form.classList.add(CLASSES.formError);
        this.$form.reset();
      });

    e.preventDefault();
  }
}
