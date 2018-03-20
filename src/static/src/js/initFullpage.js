import pubsub from './pubsub';
import jQuery from 'jquery';

let isRes = false;

jQuery(document).ready(() => {
  jQuery('#fullpage').fullpage({
    sectionSelector: '.fp-section',
    fixedElements: '#tr-header',
    // Desktop breakpoint.
    responsiveWidth: '1000',
    responsiveHeight: '768',
    onLeave: (...args) => {
      pubsub.publish('section-leave', ...args);
    },
    afterResponsive: (...args) => {
      isRes = args[0];
      pubsub.publish('after-responsive', ...args);
    }
  });

  // Checks if snap scroll is initialized or not. There may be a better approach
  // to detect this.
  isRes = document.body.style.overflow !== 'hidden';

  pubsub.publish('fullpage-init', true);
});

function isResponsive () {
  return isRes;
}

export {
  isResponsive
};
