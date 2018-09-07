goog.module('dmb.components.sidePanel.focusTrap');

const FOCUSABLE_ELEMENT_SELECTOR = [
  'a',
  'audio',
  'button',
  'datalist',
  'iframe',
  'input',
  'object',
  'progress',
  'select',
  'textarea',
  'video',
  '[contentEditable="true"]',
  '[tabindex]:not([tabindex="-1"])',
].join(', ');


/**
 * FocusTrap class
 */
class FocusTrap {
  /**
   * Constructor
   * @param  {Element} element The element to trap focus within
   */
  constructor(element) {
    this.element = element;

    this.firstFocusableElement = null;
    this.lastFocusableElement = null;

    this.keyHandler = this.handleKeypress.bind(this);

    this.findFocusableElements();

    document.addEventListener('keydown', this.keyHandler, true);
  }


  /**
   * Finds the first and last focusable elements
   */
  findFocusableElements() {
    let focusableElements = this.element.querySelectorAll(FOCUSABLE_ELEMENT_SELECTOR);
    this.firstFocusableElement = focusableElements[0];
    this.lastFocusableElement = focusableElements[focusableElements.length - 1];
  }


  /**
   * Handles the keypress event, looking for the TAB key and checking if the
   * focus is about to shift outside of the element
   * @param  {Event} event The native keydown event
   */
  handleKeypress(event) {
    // We only care about TAB here
    if (event.keyCode !== 9) {
      return;
    }

    if (event.shiftKey) {
      // If they're going up and they're already on the first element, stop it
      // and shift them to the last element
      if (event.target === this.firstFocusableElement) {
        event.preventDefault();
        this.lastFocusableElement.focus();
      }
      return;
    }

    // If they're going down and they're already on the last element, stop it
    // and shift them to the first element
    if (event.target === this.lastFocusableElement) {
      event.preventDefault();
      this.firstFocusableElement.focus();
    }
  }


  /**
   * Unbinds events and tears down saved values
   * @return {null}
   */
  destroy() {
    document.removeEventListener('keydown', this.keyHandler, true);

    this.firstFocusableElement = null;
    this.lastFocusableElement = null;

    this.keyHandler = null;

    return null;
  }
}

exports = FocusTrap;
