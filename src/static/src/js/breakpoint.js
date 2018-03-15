import { debounce } from './utils';
import pubsub from './pubsub';

export const BREAKPOINTS = {
  'SMALL': 0,
  'MOBILE': 1,
  'TABLET': 2,
  'DESKTOP': 3,
  'LARGE_DESKTOP': 4
};

export const topic = 'breakpoints';

class BreakpointsService {
  constructor () {
    this.onResize_ = this.onResize_.bind(this);
    window.addEventListener('resize', debounce(this.onResize_, 200));
    this.onResize_();
  }

  getCurrent () {
    return this.currentBp_;
  }

  getFromStyle_ () {
    const cssBpName = window.getComputedStyle(document.body, ':before')
        .getPropertyValue('content').replace(/"/g, '');

    return BREAKPOINTS[cssBpName];
  }

  onResize_ () {
    const currentBp = this.getFromStyle_();
    if (currentBp !== this.currentBp_) {
      this.currentBp_ = currentBp;
      pubsub.publish(topic, this.currentBp_);
    }
  }
}

export default new BreakpointsService();
