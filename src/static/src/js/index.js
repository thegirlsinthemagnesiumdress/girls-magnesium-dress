import fullpage from 'fullpage.js/dist/jquery.fullpage';
import jQuery from "jquery";
import ParallaxSection from './components/parallax-section'

window.$ = jQuery;

// Custom elements.
window.customElements.define('tr-parallax-section', ParallaxSection);

// FullPage initialization
const DOM_SELECTORS = {
  parallaxedImg: '.tr-section-double__parallaxed-img',
};

const CLASSES = {
  parallaxBefore: 'tr-section-double__parallaxed-img--before',
  parallaxAfter: 'tr-section-double__parallaxed-img--after',
}


$(document).ready(function() {
  const parallaxedImg = document.querySelector(DOM_SELECTORS.parallaxedImg);

  $('#fullpage').fullpage({
    sectionSelector: '.fp-section',
    onLeave: function(index, nextIndex, direction) {
      var leavingSection = $(this);

      if (nextIndex == 1) {
        parallaxedImg.classList.add(CLASSES.parallaxBefore)
      }

      //after leaving section 2
      if (nextIndex == 2) {
        parallaxedImg.classList.remove(CLASSES.parallaxBefore)
        parallaxedImg.classList.remove(CLASSES.parallaxAfter)
      }

      if (nextIndex == 3) {
        parallaxedImg.classList.add(CLASSES.parallaxAfter)
      }
    }
  });
});
