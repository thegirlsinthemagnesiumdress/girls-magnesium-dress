import axios from 'axios'
import { escapeHtml } from '../utils'

const API_ENDPOINT = '/api/survey/';

const DOM_SELECTORS = {
  form: '#registration-form',
  confirmationScreen: '.tr-registration__confirmation',
  submitBtn: 'button',
  confirmationPage: '#form-confirmation',
  csrf:'input[name=csrfmiddlewaretoken]',
  clipboard: '[data-clipboard-text]'
};

const CLASSES = {
  hidden: 'tr-u-display-none',
}

export default class Registration extends HTMLElement {

  connectedCallback () {
    this.$form = this.querySelector(DOM_SELECTORS.form);
    this.$template = this.querySelector(DOM_SELECTORS.confirmationPage);
    this.$submitBtn = this.$form.querySelector(DOM_SELECTORS.submitBtn);
    this.$confirmationScreen = this.querySelector(DOM_SELECTORS.confirmationScreen);
    this.$form.addEventListener('submit', this.generateConfirmation.bind(this));
    this.$form.addEventListener('input', this.formChange.bind(this));

    this.csrf = this.$form.querySelector(DOM_SELECTORS.csrf).value;
  }

  formChange (e) {
    const isValid = this.$form.checkValidity();
    this.$submitBtn.disabled = !isValid;
  }

  getConfirmationTemplate (context) {
    let template = this.$template.textContent;

    template = template.replace(/\[\[survey_link\]\]/g, escapeHtml(context.link));
    template = template.replace(/\[\[survey_sponsor_link\]\]/g, escapeHtml(context.link_sponsor));
    template = template.replace(/\[\[company_name\]\]/g, escapeHtml(context.company_name));

    return template
  }

  generateConfirmation (e) {
    // Show step two.
    const formData = new FormData(this.$form);

    const postData = {
      'company_name': formData.get('company_name')
    };

    axios.post(API_ENDPOINT, postData, {
      headers: {
        'X-CSRFToken': this.csrf
      }
    })
      .then((res) => {
        this.$form.parentNode.insertAdjacentHTML('beforeend', this.getConfirmationTemplate(res.data));
        // Initialize clipboard.
        new ClipboardJS(DOM_SELECTORS.clipboard); // eslint-disable-line
        this.$form.classList.add(CLASSES.hidden);
      });
    e.preventDefault();
  }

  showConfirmation () {
    this.$form.classList.add(CLASSES.hidden);
    this.$confirmationScreen.classList.remove(CLASSES.hidden);
  }
}
