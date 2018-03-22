/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {
  form: '#registration-form',
  confirmationScreen: '.tr-registration__confirmation',
  submitBtn: 'button',
};

/**
 * CSS Classes.
 * @enum {string}
 */
const CLASSES = {
  hidden: 'tr-u-display-none',
}


/**
 * Custom Element Registration Class.
 * @extends {HTMLElement}
 */
export default class Registration extends HTMLElement {
  constructor () {
    super();
  }

  /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   */
  connectedCallback () {
    this.$form = this.querySelector(DOM_SELECTORS.form);
    this.$submitBtn = this.$form.querySelector(DOM_SELECTORS.submitBtn);
    this.$confirmationScreen = this.querySelector(DOM_SELECTORS.confirmationScreen);
    this.$form.addEventListener('submit', this.generateLink.bind(this));
    this.$form.addEventListener('input', this.formChange.bind(this));
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
   * Link generation.
   *
   * @param {event} e Form submit event.
   */
  generateLink (e) {
    // Show step two.
    this.showConfirmation();
    e.preventDefault();
  }

  /**
   * Show registration confirmation.
   */
  showConfirmation () {
    this.$form.classList.add(CLASSES.hidden);
    this.$confirmationScreen.classList.remove(CLASSES.hidden);
  }
}
