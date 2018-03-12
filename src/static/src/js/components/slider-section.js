const DOM_SELECTORS = {
  slideContainer: '.section-slider__container'
};

const CLASSES = {
  sticky: 'tr-header--sticky'
}

const CAROUSEL_COLORS = [
  'tr-u-bg-color--blue-darker',
  'tr-u-bg-color--blue',
  'tr-u-bg-color--mariner',
];

export default class SliderSection extends HTMLElement {
  constructor () {
    super();
  }

  connectedCallback () {
    window.$('.section-slider__container').slick({
      autoplay: true,
      dots: true,
      fade: true,
      arrows: false
    }).on('beforeChange', (e, slick, currentSlide, nextSlide) => {
      CAROUSEL_COLORS.forEach((c) => this.classList.remove(c));
      this.classList.add(CAROUSEL_COLORS[nextSlide]);
    });

  }
}
