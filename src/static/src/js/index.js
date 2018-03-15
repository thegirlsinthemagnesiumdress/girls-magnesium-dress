import fullpage from 'fullpage.js/dist/jquery.fullpage'; // eslint-disable-line no-unused-vars
import jQuery from 'jquery';
import 'slick-carousel';
import {BreakpointService, BREAKPOINTS} from './breakpoint'

import ParallaxSection from './components/parallax-section';
import Header from './components/header';
import Registration from './components/registration';
import SliderSection from './components/slider-section';
import Accordion from './components/accordion';
import pubsub from './pubsub';

window.$ = jQuery;

// Custom elements.
window.customElements.define('tr-parallax-section', ParallaxSection);
window.customElements.define('tr-header', Header);
window.customElements.define('tr-registration', Registration);
window.customElements.define('tr-slider-section', SliderSection);
window.customElements.define('tr-accordion', Accordion);

window.$(document).ready(() => {

  window.$('#fullpage').fullpage({
    sectionSelector: '.fp-section',
    fixedElements: '#tr-header',
    // Desktop breakpoint.
    responsiveWidth: '1000',
    onLeave: (...args) => {
      pubsub.publish('section-leave', ...args);
    }
  });
});
