import {csrfToken} from '../csrf/csrf';
import Toast from '../toast/toast.class';

/**
 * Handling the export reports form
 */
export default class ExportReports {
  /**
   * Static attach method to allow easy binding in app.js
   * @param {Element} element The element that the class is bound to
   * @return {ExportReports}
   */
  static attachTo(element) {
    return new ExportReports(element);
  }

  /**
   * Constructor
   * @param {Element} element The element that the class is bound to
   */
  constructor(element) {
    this.element = element;
    this.form = this.element.querySelector('form');
    this.button = this.element.querySelector('button[type="submit"]');
    this.toastEl = this.element.querySelector('[data-export-toast]');
    this.toast = new Toast(this.toastEl);
    this.engagementLead = this.element.getAttribute('data-export-engagement-lead');
    this.submitting = false;

    // Context binding
    this.onSubmit = this.onSubmit.bind(this);

    this.form.addEventListener('submit', this.onSubmit);
  }

  /**
   * Handles the form submit
   * @param {Event} event The submit event
   */
  onSubmit(event) {
    event.preventDefault();
    if (this.submitting) {
      return;
    }
    this.export();
  }

  /**
   * Export report data
   * @export
   * @return {Promise}
   */
  export() {
    this.submitting = true;
    this.button.setAttribute('disabled', 'disabled');

    let data = {
      'engagement_lead': this.engagementLead,
    };

    return fetch(this.form.action, {
      method: this.form.method,
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then(() => {
        this.toast.setState('success');
      }, (err) => {
        this.toast.setState('error');
        console.error(err);
      })
      .finally(()=> {
        this.submitting = false;
        this.button.removeAttribute('disabled');
        this.toast.show();
      });
  }
}
