import pubsub from '../pubsub';

const DOM_SELECTORS = {};

const CLASSES = {
  sticky: 'tr-header--sticky'
}

export default class ParallaxSection extends HTMLElement {
  constructor () {
    super();

    this.subscriptions = [];
    this.subscriptions
      .push(pubsub.subscribe('section-leave', (topic, ...args) => {
        this.sectionLeaveCb(...args);
      }));
  }

  connectedCallback () {
  }

  sectionLeaveCb (index, nextIndex, direction) {
    if (nextIndex === 1) {
      this.classList.remove(CLASSES.sticky);
    }

    if (nextIndex === 2) {
      this.classList.add(CLASSES.sticky);
    }
  }
}
