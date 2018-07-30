import jQuery from 'jquery';

/**
 * @fileoverview Custom Element to scroll to second section
 */


/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {};

/**
 * CSS Classes.
 * @enum {string}
 */
const CLASSES = {}

/**
 * Custom Element Learn more Class.
 * @extends{HTMLElement}
 */
export default class LearnMoreBtn extends HTMLElement {
  constructor () {
    super();
    this.scrollTo = this.scrollTo.bind(this);
  }

  /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   */
  connectedCallback () {
    this.addEventListener('click', this.scrollTo);
  }

  /**
   * Invoked when the custom element is disconnected
   * from the document's DOM.
   */
  disconnectedCallback () {
    this.removeEventListener('click', this.scrollTo);
  }


  /**
  * Scrolls to the first section.
  * collapsed.
  * @param {event} e
  */
  scrollTo (e) {
    jQuery.fn.fullpage.moveTo(2);
  }
}
