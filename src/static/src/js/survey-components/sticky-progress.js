import * as scrollServiceConfig from '../components/scroll/scroll.service';


const scrollService = scrollServiceConfig.main();

/**
 * Init funciton to create the progress bar if it exists in the DOM
 * @return {ProgressBar} returns the newly created ProgressBar instance
 */
export function init() {
  return new ProgressBar('ProgressBar', 'SkinContent');
}

/**
 * The Progress Bar class
 */
class ProgressBar {
  /**
   * @param {string} elementId The progressBar element's id
   * @param {string} positionElementId The id of the element to have the progress bar positioned at the top of
   */
  constructor(elementId, positionElementId) {
    this.id = elementId;
    this.positionId = positionElementId;

    this.el = null;
    this.positionEl = null;

    this.findElements();

    this.positionElOffset = null;
    this.stickyClass = 'is-sticky';
    this.hiddenClass = 'dmb-h-hidden';

    this.resizeTimeout = null;

    this.onScrollHandler = this.onScroll.bind(this);
    this.onResizeHandler = this.onResize.bind(this);
    this.onLoadHandler = this.onLoad.bind(this);

    scrollService.addListener(this.onScrollHandler);
    window.addEventListener('resize', this.onResizeHandler);
    window['Qualtrics']['SurveyEngine']['addOnReady'](this.onLoadHandler);
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

    const progress = this.el.querySelector('.ProgressBarFillContainer');
    const progressText = progress.textContent.match(/[.\d]+%/);
    const progressPercent = progressText && progressText[0];

    if (progressPercent === '0%') {
      this.el.classList.add(this.hiddenClass);
    } else {
      this.el.classList.remove(this.hiddenClass);
    }
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
    window.clearTimeout(this.resizeTimeout);
    this.resizeTimeout = window.setTimeout(() => {
      this.onScroll(window.scrollY);
    }, 32);
  }
}
