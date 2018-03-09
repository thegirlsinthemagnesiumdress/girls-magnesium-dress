const DOM_SELECTORS = {
  form: '#registration-form',
  confirmationScreen: '.tr-registration__confirmation'
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
      this.$confirmationScreen = this.querySelector(DOM_SELECTORS.confirmationScreen);
      this.$form.addEventListener('submit', this.generateLink.bind(this));
    }, 0);
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
