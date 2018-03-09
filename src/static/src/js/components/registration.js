const DOM_SELECTORS = {
  form: '#registration-form',
  confirmationScreen: '.tr-registration__confirmation',
  submitBtn: 'button',
};

const CLASSES = {
  hidden: 'tr-u-display-none',
}

export default class Registration extends HTMLElement {
  constructor () {
    super();
  }

  connectedCallback () {
    setTimeout(() => {
      this.$form = this.querySelector(DOM_SELECTORS.form);
      this.$submitBtn = this.$form.querySelector(DOM_SELECTORS.submitBtn);
      this.$confirmationScreen = this.querySelector(DOM_SELECTORS.confirmationScreen);
      this.$form.addEventListener('submit', this.generateLink.bind(this));
      this.$form.addEventListener('input', this.formChange.bind(this));
    }, 0);
  }

  formChange (e) {
    const isValid = this.$form.checkValidity();
    this.$submitBtn.disabled = !isValid;
  }

  generateLink (e) {
    // Show step two.
    this.showConfirmation();
    e.preventDefault();
  }

  showConfirmation () {
    this.$form.classList.add(CLASSES.hidden);
    this.$confirmationScreen.classList.remove(CLASSES.hidden);
  }
}
