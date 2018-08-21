/* global Qualtrics */
goog.module('dmb.survey.stickyProgress');

const scrollServiceConfig = goog.require('dmb.components.scroll.service');

const scrollService = scrollServiceConfig.main();

/**
 * Init funciton to create the progress bar if it exists in the DOM
 * @return {ProgressBar} returns the newly created ProgressBar instance
 */
function init() {
  return new ProgressBar('ProgressBar', 'SkinContent');
}

/**
 * The Progress Bar class
 */
class ProgressBar {
  /**
   * @param {Element} element The progressBar element
   * @param {Element} positionElement The element to have the progress bar positioned at the top of
   */
  constructor(elementId, positionElementId) {
    this.id = elementId;
    this.positionId = positionElementId;

    this.findElements();

    this.positionElOffset = null;
    this.stickyClass = 'is-sticky';

    this.onScrollHandler = this.onScroll.bind(this);
    this.onResizeHandler = this.onResize.bind(this);
    this.onLoadHandler = this.onLoad.bind(this);

    scrollService.addListener(this.onScrollHandler);
    window.addEventListener('resize', this.onResizeHandler);
    Qualtrics.SurveyEngine.addOnReady(this.onLoadHandler);
  }

  /**
   * Finds and binds el and positionEl
   */
  findElements() {
    this.el = document.getElementById(this.id);
    this.positionEl = document.getElementById(this.positionId);

    if (!this.el || !this.positionEl) {
      console.warn('Progress bar not found'); // eslint-disable-line no-console
    }
  }

  /**
   * Handles the Qualtrics load event, finds new elements and refreshes the positioning
   */
  onLoad() {
    this.findElements();
    this.positionElOffset = null;
    this.onScroll(window.scrollY);
  }

  /**
   * Handles checking the position when the browser scrolls
   * @param  {number} scrollY The vertical offset of the page
   */
  onScroll(scrollY) {
    if (!this.positionElOffset) {
      this.positionElOffset = this.positionEl.offsetTop;
      this.el.style.top = `${this.positionElOffset}px`;
    }

    if (scrollY >= this.positionElOffset) {
      this.el.classList.add(this.stickyClass);
    } else {
      this.el.classList.remove(this.stickyClass);
    }
  }

  /**
   * Handles the browser resize event, no throttling, just setting a value to null
   */
  onResize() {
    this.positionElOffset = null;
  }
}

exports = {
  init,
};
