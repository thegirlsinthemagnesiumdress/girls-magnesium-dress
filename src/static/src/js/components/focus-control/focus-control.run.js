goog.module('dmb.components.focusControl.run');

/**
 * Class for handling focus control on the page. Hiding all outlines when the
 * user uses the mouse, but showing the outlines again when the tab key is
 * pressed.
 */
class FocusControl {
  /**
   * Creates the style element and attaches the event listeners
   */
  constructor() {
    this.element = document.createElement('style');
    this.cssSnippet = ':focus{outline:0}::-moz-focus-inner{border:0}:focus-within *{outline:0 !important}';

    document.querySelector('head').appendChild(this.element);

    this.mouseDownHandler = document.addEventListener('mousedown', this.handleMouseDown.bind(this));
    this.keyDownHandler = document.addEventListener('keydown', this.handleKeyDown.bind(this));
  }

  /**
   * Adds the hide-focus styles to the style tag
   */
  handleMouseDown() {
    this.element.innerHTML = this.cssSnippet;
  }

  /**
   * Removes the hide-focus styles, but only when the TAB key is pressed
   *
   * @param  {Event} event The native keydown event
   */
  handleKeyDown(event) {
    if (event.keyCode === 9) {
      this.element.innerHTML = '';
    }
  }

  /**
   * Removes the event listeners and the styles from the document
   */
  destroy() {
    document.removeEventListener('mousedown', this.mouseDownHandler);
    document.removeEventListener('keydown', this.keyDownHandler);

    if (this.element) {
      document.querySelector('head').removeChild(this.element);
    }

    this.element = null;
  }
}

/**
 * Sets up the focus control for the page
 *
 * @return {FocusControl} returns an new instance of the FocusControl class
 */
function Run() {
  return new FocusControl();
}


exports = {
  main: Run,
};
