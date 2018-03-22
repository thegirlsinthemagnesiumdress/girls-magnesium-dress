import jQuery from 'jquery';

/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {
  slideContainer: '.section-slider__container'
};

/**
 * List of background colors.
 */
const CAROUSEL_COLORS = [
  'tr-u-bg-color--blue-darker',
  'tr-u-bg-color--blue',
  'tr-u-bg-color--mariner',
];


/**
 * Custom Element Slider Section Class.
 * @extends {HTMLElement}
 */
export default class SliderSection extends HTMLElement {
   /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   *
   * Initialize Slick Carousel.
   */
  connectedCallback () {
    jQuery(DOM_SELECTORS.slideContainer).slick({
      autoplay: true,
      arrows: false,
      dots: true,
      fade: true,
      pauseOnHover: false,
      pauseOnDotsHover: true
    }).on('beforeChange', (e, slick, currentSlide, nextSlide) => {
      CAROUSEL_COLORS.forEach((c) => this.classList.remove(c));
      this.classList.add(CAROUSEL_COLORS[nextSlide]);
    });
  }
}
