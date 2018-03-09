const DOM_SELECTORS = {
  form: '#registration-form'
  confirmationScreen: '.register__confirmation'
};

const CLASSES = {}

export default class Register extends HTMLElement {
  constructor () {
    super();
  }

  connectedCallback () {
    this.$form = this.querySelector(DOM_SELECTORS.form);
    this.$confirmationScreen = this.querySelector(DOM_SELECTORS.confirmationScreen);
    this.$form.addEventListener('submit', this.generateLink.bind(this));
  }

  generateLink () {
    // Show step two.

  }

  showConfirmation () {
    thi
  }
}
