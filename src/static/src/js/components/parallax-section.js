import pubsub from '../pubsub';

// FullPage initialization
const DOM_SELECTORS = {
  parallaxedImg: '.tr-parallax-section__parallaxed-img',
  eyebrow: '.tr-parallax-section__eyebrow',
};

const CLASSES = {
  parallaxBefore: 'tr-parallax-section__parallaxed-img--before',
  parallaxAfter: 'tr-parallax-section__parallaxed-img--after',
  eyebrowSticky: 'tr-parallax-section__eyebrow--sticky',
  eyebrowhidden: 'tr-parallax-section__eyebrow--hidden',
  eyebrowFadedout: 'tr-parallax-section__eyebrow--faded-out'
}

export default class ParallaxSection extends HTMLElement {
  constructor () {
    super();

    this.subscribtions = [];
    this.subscribtions
      .push(pubsub.subscribe('section-leave', (topic, ...args) => {
        this.sectionLeaveCb(...args);
      }));
  }

  connectedCallback () {
    // Fullpage.js updates the dom and inserts a wrapper to our sections.
    const sectionWrp = this.parentNode.parentNode;
    this.index = [...sectionWrp.parentNode.children].indexOf(sectionWrp) + 1;
    this.$parallaxedImg = this.querySelector(DOM_SELECTORS.parallaxedImg);
    this.$eyebrow = this.querySelector(DOM_SELECTORS.eyebrow);
  }

  sectionLeaveCb (index, nextIndex, direction) {

    if (nextIndex === this.index - 1) {
      this.$parallaxedImg.classList.add(CLASSES.parallaxBefore)
      this.unpinEyebrow();
    }

    if (nextIndex === this.index) {
      this.$parallaxedImg.classList.remove(CLASSES.parallaxBefore)
      this.$parallaxedImg.classList.remove(CLASSES.parallaxAfter)
    }

    if (nextIndex === this.index + 1) {
      this.pinEyebrow(direction === 'up');
      this.$parallaxedImg.classList.add(CLASSES.parallaxAfter)
    }

    if (nextIndex === this.index + 2) {
      this.unpinEyebrow(true);
    }
  }

  /**
   *
   * Clones the eyebrows and sets it to have a sticky behavior.
   * @param {bool} animateOpacity Whether or not we animate the eyebrow opacity when pinning.
   */
  pinEyebrow (animateOpacity) {
    if (!this.eyebrowSticky) {
      this.rect = this.rect ? this.rect : this.$eyebrow.getBoundingClientRect();
      // We need to clone the eyebrow and append it to the body in order to keep the
      // position fixe to working. Fullpage.js transforms the page and that affects
      // fixed positioning. https://www.w3.org/TR/css-transforms-1/#module-interactions
      this.$clonedEyebrow = this.$eyebrow.cloneNode(true);
      this.$clonedEyebrow.classList.add(CLASSES.eyebrowSticky);
      this.$clonedEyebrow.style.top = `${this.rect.y}px`;
      this.$clonedEyebrow.style.left = `${this.rect.x}px`;
      this.$clonedEyebrow.style.width = `${this.rect.width}px`;
      this.$clonedEyebrow.style.height = `${this.rect.height}px`;
      this.$eyebrow.classList.add(CLASSES.eyebrowhidden);

      document.body.appendChild(this.$clonedEyebrow);

      if (animateOpacity) {
        this.$clonedEyebrow.classList.add(CLASSES.eyebrowFadedout);

        // Removing a class straight after appending to the DOM
        // prevents the animation to happen. This is a workarounf.
        // TODO: there might be a nicer approach
        setTimeout(() => {
          this.$clonedEyebrow.classList.remove(CLASSES.eyebrowFadedout);
        }, 100);
      }

      this.eyebrowSticky = true;
    }
  }

  /**
   * Removes the cloned sticky eyebrow from the dom.
   * @param {bool} animateOpacity Whether or not we animate the opacity when unpinning the element.
   */
  unpinEyebrow (animateOpacity) {
    if (this.$clonedEyebrow) {
      if (animateOpacity) {
        this.$clonedEyebrow.addEventListener('transitionend', () => {
          this.$clonedEyebrow.parentNode.removeChild(this.$clonedEyebrow);
        });

        this.$clonedEyebrow.classList.add(CLASSES.eyebrowFadedout)
      } else {
        this.$clonedEyebrow.parentNode.removeChild(this.$clonedEyebrow);
      }
    }
    this.eyebrowSticky = false;
    this.$eyebrow.classList.remove(CLASSES.eyebrowhidden);
  }
}
