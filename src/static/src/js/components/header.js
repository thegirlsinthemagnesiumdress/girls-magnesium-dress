/**
 * @fileoverview Custom Element for Accordion component.
 */
import pubsub from '../pubsub';
import { isResponsive } from '../initFullpage';

/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {};

/**
 * CSS Classes.
 * @enum {string}
 */
const CLASSES = {
  sticky: 'tr-header--sticky',
}

/**
 * Amount of pixels of scroll that have
 * to be exceeded to get the sticky
 * header to appear.
 * @const {number}
 */
const MOBILE_THREESHOLD = 2;


/**
 * Custom Element Header Class.
 * @extends {HTMLElement}
 */
export default class Header extends HTMLElement {
  constructor () {
    super();

    this.subscriptions = [];
    this.onScroll = this.onScroll.bind(this);
  }

  /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   */
  connectedCallback () {
    this.subscriptions
      .push(pubsub.subscribe('section-leave', (topic, ...args) => {
        this.sectionLeaveCb(...args);
      }));

    this.subscriptions
      .push(pubsub.subscribe('after-responsive', (topic, ...args) => {
        this.afterResponsiveCb(...args);
      }));
    this.subscriptions
      .push(pubsub.subscribe('fullpage-init', () => {
        this.afterResponsiveCb();
      }));
  }

  /**
   * Invoked when the custom element is disconnected
   * from the document's DOM.
   */
  disconnectedCallback () {
    this.subscriptions.forEach((sub) => pubsub.unsubscribe(sub));
    this.destroyScrollMonitor();
  }

  /**
   * Fullpage.js onLeave event handler.
   * The method set the header to be sticky or not.
   *
   * @param {number} index Leaving section index.
   * @param {number} nextIndex Next section index.
   * @param {string} direction Whether the direction is UP or DOWN.
   */
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

  /**
   * Fullpage.js afterResponsive event handler.
   * Initialize or destroy the scroll monitor.
   */
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

  /**
   * Scroll Monitor initialization.
   */
  initScrollMonitor () {
    document.addEventListener('scroll', this.onScroll);
  }

  /**
   * Scroll Monitor destruction.
   */
  destroyScrollMonitor () {
    document.removeEventListener('scroll', this.onScroll);
  }

  /**
   * Scroll monitor event handler.
   * Used on handle header behavior on mobile viewports.
   * @param {event} e
   */
  onScroll (e) {
    const scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
    if (scrollTop > MOBILE_THREESHOLD) {
      this.classList.add(CLASSES.sticky);
    } else {
      this.classList.remove(CLASSES.sticky);
    }
  }
}
