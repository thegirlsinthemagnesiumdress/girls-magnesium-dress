const DOM_SELECTORS = {
  accordion: '.tr-accordion',
  accordionSection: '.tr-accordion-section',
  accordionSectionHeadings: '.tr-accordion-section dt'
};

const CLASSES = {
  hidden: '.tr-accordion-section-closed',
}

export default class Accordion extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback () {
    this.$accordion = this.querySelector(DOM_SELECTORS.accordion);
    this.$accordionSections = this.querySelectorAll(DOM_SELECTORS.accordionSection);
    this.$accordionSectionHeadings = this.querySelectorAll(DOM_SELECTORS.accordionSectionHeadings);
    this.$accordionSectionHeadings.forEach((el) => {
      el.addEventListener('click', this.toggle.bind(this));
    });
    this.hideAll();
  }

  hideAll () {
    this.$accordionSections.forEach(function (el) {
      el.classList.add(CLASSES.hidden);
    });
  }

  toggle (e) {
    console.log(e);
    this.hideAll();
    console.log('click');
  }
}
