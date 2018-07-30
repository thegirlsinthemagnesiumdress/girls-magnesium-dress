import { debounce } from './utils';
import pubsub from './pubsub';

/**
 * Breakpoints list.
 * @enum {number}
 */
export const BREAKPOINTS = {
  'SMALL': 0,
  'MOBILE': 1,
  'TABLET': 2,
  'DESKTOP': 3,
  'LARGE_DESKTOP': 4
};

/**
 * Pub/sub topic.
 */
export const topic = 'breakpoints';


/**
 * Utility class for breakpoints and resize.
 */
class BreakpointsService {
  constructor () {
    this.onResize_ = this.onResize_.bind(this);
    window.addEventListener('resize', debounce(this.onResize_, 200));
    this.onResize_();
  }

  /**
   * Returns the current breakpoint.
   */
  getCurrent () {
    return this.currentBp_;
  }

  /**
   * Gets breakpoints from css.
   */
  getFromStyle_ () {
    const cssBpName = window.getComputedStyle(document.body, ':before')
        .getPropertyValue('content').replace(/"/g, '');

    return BREAKPOINTS[cssBpName];
  }

  /**
   * Resize event handler.
   *
   * Sets the current breakpoint and publishes breakpoint changes.
   */
  onResize_ () {
    const currentBp = this.getFromStyle_();
    if (currentBp !== this.currentBp_) {
      this.currentBp_ = currentBp;
      pubsub.publish(topic, this.currentBp_);
    }
  }
}

export default new BreakpointsService();
