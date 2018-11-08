goog.module('dmb.components.sidePanel.class');

const FocusTrap = goog.require('dmb.components.sidePanel.focusTrap');

/**
 * Enum of the classes used in the component
 * @const
 * @enum {string}
 */
const classes = {
  ACTIVE: 'dmb-side-panel--active',
  BACKDROP: 'dmb-backdrop',
  BACKDROP_ACTIVE: 'dmb-backdrop--active',
  BODY_HAS_MODAL: 'dmb-body--has-modal',
  HIDDEN: 'dmb-h-hidden',
  VISIBLE: 'dmb-h-visible',
};

/**
 * Side panel class
 */
class SidePanel {
  /**
   * Constructor
   * @param  {Element} element The panel element to set up.
   * @param  {boolean} bindTriggers Whether events on the triggers or not.
   */
  constructor(element, bindTriggers=true) {
    /**
     * @const
     * @type {Element}
     */
    this.el = element;

    /**
     * The id of the element
     * @const
     * @type {string}
     * @export
     */
    this.id = element.id;

    /**
     * Storing if the modal is visible or not
     * @type {boolean}
     * @export
     */
    this.isVisible = false;

    /**
     * Array of all the elements on the page that can open this side panel
     * @type {Array.<Element>}
     */
    this.triggerEls = [...document.querySelectorAll(`[dmb-side-panel-trigger="#${this.id}"]`)];

    /**
     * Find any buttons inside the modal for closing it
     * @type {Array.<Element>}
     */
    this.closeEls = [...this.el.querySelectorAll('[dmb-side-panel-close]')];

    /**
     * The trigger that opened the side panel, used for focusing on close
     * @type {?EventTarget}
     * @export
     */
    this.lastTrigger = null;

    /**
     * Bound context for triggerClickHandler
     * @type {Function}
     * @export
     */
    this.onTriggerClick = this.triggerClickHandler.bind(this);

    /**
     * Bound context for closeClickHandler
     * @type {Function}
     * @export
     */
    this.onCloseClick = this.closeClickHandler.bind(this);

    /**
     * Bound context for escapeKeyHandler
     * @type {Function}
     * @export
     */
    this.onEscapeKey = this.escapeKeyHandler.bind(this);

    /**
     * Element to be used as the backdrop while the side panel is open
     * @type {Element}
     * @export
     */
    this.backdropEl = this.getOrSetBackdrop();


    /**
     * Instance of the FocusTrap
     * @type {?FocusTrap}
     * @export
     */
    this.focusTrapInstance = null;

    if (bindTriggers) {
      this.bindTriggers();
    }
    this.bindEvents();

    this.el.setAttribute('aria-modal', 'true');
    this.el.setAttribute('role', 'dialog');
    this.el.setAttribute('aria-hidden', 'true');
    this.el.setAttribute('tabindex', '-1');
    this.el.classList.add(classes.HIDDEN);
  }


  /**
   * Opens the side panel
   * @export
   */
  open() {
    if (this.isVisible === true) {
      return;
    }

    this.isVisible = true;

    // Attributes & Classes
    this.el.setAttribute('aria-hidden', 'false');
    this.el.classList.remove(classes.HIDDEN);
    this.backdropEl.classList.remove(classes.HIDDEN);
    document.body.classList.add(classes.BODY_HAS_MODAL);
    rafPromise()
      .then(() => {
        this.el.classList.add(classes.ACTIVE);
        this.backdropEl.classList.add(classes.BACKDROP_ACTIVE);
      });

    // Events
    this.backdropEl.addEventListener('click', this.onCloseClick);
    document.addEventListener('keydown', this.onEscapeKey);
    this.focusTrapInstance = new FocusTrap(this.el);

    window.setTimeout(() => {
      this.el.focus();
    });
  }


  /**
   * Closes the side panel
   * @export
   */
  close() {
    if (this.isVisible === false) {
      return;
    }

    this.isVisible = false;

    // Attributes & Classes
    this.el.setAttribute('aria-hidden', 'true');
    this.el.classList.remove(classes.ACTIVE);
    transitionEndPromise(this.el, 'transform')
      .then(() => this.el.classList.add(classes.HIDDEN));
    document.body.classList.remove(classes.BODY_HAS_MODAL);
    this.backdropEl.classList.remove(classes.BACKDROP_ACTIVE);
    transitionEndPromise(this.backdropEl, 'opacity')
      .then(() => this.backdropEl.classList.add(classes.HIDDEN));

    // Events
    this.backdropEl.removeEventListener('click', this.onCloseClick);
    document.removeEventListener('keydown', this.onEscapeKey);
    if (this.focusTrapInstance) {
      this.focusTrapInstance = this.focusTrapInstance.destroy();
    }

    if (this.lastTrigger) {
      this.lastTrigger.focus();
      this.lastTrigger = null;
    }
  }


  /**
   * Using one shared element for all panels needing a backdrop. Get the existing one (if it exists) or create a new one
   * @return {Element} The backdrop element
   */
  getOrSetBackdrop() {
    const existingBackdrop = document.querySelector(`.${classes.BACKDROP}`);

    if (existingBackdrop) {
      return existingBackdrop;
    }

    const backdropEl = document.createElement('div');
    backdropEl.classList.add(classes.BACKDROP);
    backdropEl.classList.add(classes.HIDDEN);
    document.body.appendChild(backdropEl);

    return backdropEl;
  }


  /**
   * Binds the event listeners to all of the triggerEls
   */
  bindTriggers() {
    this.triggerEls.forEach((trigger) => {
      trigger.addEventListener('click', this.onTriggerClick);
    });
  }

  /**
   * Binds the event listeners to all of the triggerEls
   */
  bindEvents() {
    this.closeEls.forEach((close) => {
      close.addEventListener('click', this.onCloseClick);
    });
  }


  /**
   * Handles when a side panel trigger is clicked on
   * @param  {Event} event The native click event
   */
  triggerClickHandler(event) {
    event.preventDefault();
    this.lastTrigger = event.currentTarget;
    this.open();
  }


  /**
   * Handles when a close button is clicked
   * @param  {Event} event The native click event
   */
  closeClickHandler(event) {
    event.preventDefault();
    this.close();
  }


  /**
   * Handles keypresses and closes the side-panel if ESCAPE is pressed
   * @param {Event} event The native keydown event
   */
  escapeKeyHandler(event) {
    if (event.keyCode !== 27) {
      return;
    }

    this.close();
  }


  /**
   * Handles the unbinding of any events outside of this component
   * @export
   */
  destroy() {
    this.triggerEls.forEach((trigger) => {
      trigger.removeEventListener('click', this.onTriggerClick);
    });
  }
}


/**
 * Helper function for request animation frame
 * @return {Promise} a promise that resolves in the next frame
 */
function rafPromise() {
  return new Promise((resolve) => {
    window.requestAnimationFrame(resolve);
  });
}


/**
 * Helper function for transitions end events
 * @param  {Element} element The element to listen for events on
 * @param  {string=} property The name of the CSS property to listen for the end transition of. Useful when multiple
 *                            properties have different transitions
 * @return {Promise} A promise that resolves when the desired transition end has occurred
 */
function transitionEndPromise(element, property) {
  return new Promise((resolve) => {
    const transitionend = (e) => {
      if (property && e.propertyName !== property) {
        return;
      }
      element.removeEventListener('transitionend', transitionend);
      resolve();
    };
    element.addEventListener('transitionend', transitionend);
  });
}

exports = SidePanel;
