import pubsub from '../pubsub';
import { isResponsive } from '../initFullpage';

const DOM_SELECTORS = {};

const CLASSES = {
  sticky: 'tr-header--sticky',
}

const MOBILE_THREESHOLD = 2;

export default class Header extends HTMLElement {
  constructor () {
    super();

    this.onScroll = this.onScroll.bind(this);

    this.subscriptions = [];
    this.subscriptions
      .push(pubsub.subscribe('section-leave', (topic, ...args) => {
        this.sectionLeaveCb(...args);
      }));

    this.subscriptions
      .push(pubsub.subscribe('after-responsive', (topic, ...args) => {
        this.afterResponsiveCb(...args);
      }));
  }

  connectedCallback () {
    this.subscriptions
      .push(pubsub.subscribe('fullpage-init', () => {
        this.afterResponsiveCb();
      }));
  }

  disconnectedCallback () {
    this.subscriptions.forEach((sub) => pubsub.unsuscribe(sub));
    this.destroyScrollMonitor();
  }

  sectionLeaveCb (index, nextIndex, direction) {
    if (!this.isResponsive) {
      if (nextIndex === 1) {
        this.classList.remove(CLASSES.sticky);
      }

      if (nextIndex >= 2) {
        this.classList.add(CLASSES.sticky);
      }
    }
  }

  afterResponsiveCb () {
    this.isResponsive = isResponsive();
    if (this.isResponsive) {
      this.initScrollMonitor();
      this.onScroll();
    } else {
      this.destroyScrollMonitor()
      this.sectionLeaveCb();
    }
  }

  initScrollMonitor () {
    document.addEventListener('scroll', this.onScroll);
  }

  destroyScrollMonitor () {
    document.removeEventListener('scroll', this.onScroll);
  }

  onScroll (e) {
    const scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
    if (scrollTop > MOBILE_THREESHOLD) {
      this.classList.add(CLASSES.sticky);
    } else {
      this.classList.remove(CLASSES.sticky);
    }
  }
}
