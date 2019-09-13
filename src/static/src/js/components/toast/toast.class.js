/**
 * Class for handling the Toast UI
 */
export default class Toast {
  /**
   * Helper method for easily attaching this class to an element
   * @param {Element} element
   * @return {Toast}
   * @export
   */
  static attachTo(element) {
    return new Toast(element);
  }

  /**
   * Constructor
   * @param {Element} element
   */
  constructor(element) {
    this.element = element;
    this.stateAttribute = 'data-toast-state';
    this.activeClass = 'dmb-toast--active';
    this.messages = this.element.querySelectorAll(`[${this.stateAttribute}]`);
  }

  /**
   * @param {string} state
   * @export
   */
  setState(state) {
    this.messages.forEach((message) => message.style.display = 'none');
    const message = this.element.querySelector(`[${this.stateAttribute}="${state}"]`);
    if (!message) {
      console.warn(`Unable to find message for '${state}'`);
      return;
    }
    message.style.display = '';
  }

  /**
   * Shows and then hides the toast
   * @export
   */
  show() {
    if (this.element.classList.contains(this.activeClass)) {
      return;
    }
    const onAnimationEnd = () => {
      this.element.classList.remove(this.activeClass);
      this.element.removeEventListener('animationend', onAnimationEnd);
    };
    this.element.addEventListener('animationend', onAnimationEnd);
    this.element.classList.add(this.activeClass);
  }
}
