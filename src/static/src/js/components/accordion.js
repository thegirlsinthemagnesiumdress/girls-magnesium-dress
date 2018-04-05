/**
 * @fileoverview Custom Element for Accordion component.
 */


/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {
  accordion: '.tr-accordion',
  accordionSection: '.tr-accordion-section',
  accordionSectionHeadings: '.tr-accordion-section dt',
};

/**
 * CSS Classes.
 * @enum {string}
 */
const CLASSES = {
  accordionSection: 'tr-accordion-section',
  hidden: 'tr-accordion-section-closed',
}

/**
 * Custom Element Accordion Class.
 * @extends{HTMLElement}
 */
export default class Accordion extends HTMLElement {
  constructor () {
    super();
    this.toggle = this.toggle.bind(this);
  }

  /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   */
  connectedCallback () {
    this.$accordion = this.querySelector(DOM_SELECTORS.accordion);
    this.$accordionSections = this.querySelectorAll(DOM_SELECTORS.accordionSection);
    this.$accordionSectionHeadings = this.querySelectorAll(DOM_SELECTORS.accordionSectionHeadings);

    this.$accordionSectionHeadings.forEach((el) => {
      el.addEventListener('click', this.toggle);
    });

    this.hideAll();
  }

  /**
   * Invoked when the custom element is disconnected
   * from the document's DOM.
   */
  disconnectedCallback () {
    this.$accordionSectionHeadings.forEach((el) => {
      el.removeEventListener('click', this.toggle);
    });
  }

  /**
   * Collapses the accordion's elements.
   */
  hideAll () {
    this.$accordionSections.forEach(function (el) {
      el.classList.add(CLASSES.hidden);
    });
  }

/**
 * Toggles an accordion element to be visible or
 * collapsed.
 * @param {event} e
 */
  toggle (e) {
    var el = e.target;
    while ((el = el.parentElement) && !el.classList.contains(CLASSES.accordionSection));
    if (el.classList.contains(CLASSES.hidden)) {
      this.hideAll();
    }
    el.classList.toggle(CLASSES.hidden);
  }
}
