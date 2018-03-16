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

  // I couldn't find a better way to check if
  // snap scroll is initialized or not.
  isRes = document.body.style.overflow !== 'hidden';

  pubsub.publish('fullpage-init', true);
});

function isResponsive () {
  return isRes;
}

export {
  isResponsive
};
