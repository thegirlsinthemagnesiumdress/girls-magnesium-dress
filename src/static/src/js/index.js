import fullpage from 'fullpage.js/dist/jquery.fullpage';
import jQuery from "jquery";
import ParallaxSection from './components/parallax-section'
import pubsub from './pubsub';

window.$ = jQuery;

// Custom elements.
window.customElements.define('tr-parallax-section', ParallaxSection);

window.$(document).ready(() => {
  window.$('#fullpage').fullpage({
    sectionSelector: '.fp-section',
    onLeave: (...args) => {
      pubsub.publish('section-leave', ...args);
    }
  });
});
