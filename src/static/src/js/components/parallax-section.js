/**
 * This component handles scroll animations/parallax for both the 200vh
 * sections and 100vh sections with animated content.
 *
 * 200vh sections:
 * - Pin/unpin eyebrow.
 * - Parallax animation of the image assets.
 * - Parallax-y background.
 *
 * 100vh sections:
 * - Parallax animation of the image asset.
 */

import pubsub from '../pubsub';
import { isResponsive } from '../initFullpage';

// FullPage initialization
const DOM_SELECTORS = {
  parallaxedImg: '.tr-parallax-section__parallaxed-img',
  eyebrow: '.tr-parallax-section__eyebrow--pin',
};

const CLASSES = {
  parallaxBefore: 'tr-parallax-section__parallaxed-img--before',
  parallaxAfter: 'tr-parallax-section__parallaxed-img--after',
  parallaxNoTransition: 'tr-parallax-section__parallaxed-img--no-transition',
  eyebrowSticky: 'tr-parallax-section__eyebrow--sticky',
  eyebrowHidden: 'tr-parallax-section__eyebrow--hidden',
  eyebrowFadedout: 'tr-parallax-section__eyebrow--faded-out',
  eyebrowTransition: 'tr-parallax-section__eyebrow--transition-opacity',
  fpEnabled: 'fp-enabled'
};

const imgAfterOffset = 20;

export default class ParallaxSection extends HTMLElement {
  constructor () {
    super();

    this.subscriptions = [];
    this.subscriptions
      .push(pubsub.subscribe('section-leave', (topic, ...args) => {
        this.sectionLeaveCb(...args);
      }));

    this.subscriptions
      .push(pubsub.subscribe('after-responsive', (topic, ...args) => {
        this.afterResponsiveCb(...args);
      }));
  }

  connectedCallback () {
    pubsub.subscribe('fullpage-init', () => {
      // Fullpage.js updates the dom and inserts a wrapper to our sections.
      const sectionWrp = this.parentNode.parentNode;
      this.index = [...sectionWrp.parentNode.children].indexOf(sectionWrp) + 1;
      this.$parallaxedImg = this.querySelector(DOM_SELECTORS.parallaxedImg);
      this.$eyebrow = this.querySelector(DOM_SELECTORS.eyebrow);
      this.isResponsive = isResponsive();
      const imgTargetSelector = this.$parallaxedImg.getAttribute('data-parallax-target');
      this.$targetImgPositionEl = imgTargetSelector ? document.querySelector(imgTargetSelector) : null;

      // Seems like even if fullpage is initialized
      // the browser hasn't finished layouting the page at this point.
      // I've had to add a long timeout to get the right sizes/positions.
      window.setTimeout(() => {
        this.setImageAfterOffset();
      }, 500);
    });
  }

  setImageAfterOffset () {
    if (this.$targetImgPositionEl) {
      let containedBefore;
      let containedAfter;

      this.$parallaxedImg.classList.add(CLASSES.parallaxNoTransition);

      // Remove before/after classes (and inline styles) and save if they were set to be
      // able to restore them after the calculation is done.
      this.$parallaxedImg.style.transform = '';

      if (this.$parallaxedImg.classList.contains(CLASSES.parallaxBefore)) {
        containedBefore = true;
        this.$parallaxedImg.classList.remove(CLASSES.parallaxBefore);
      }

      if (this.$parallaxedImg.classList.contains(CLASSES.parallaxAfter)) {
        containedAfter = true;
        this.$parallaxedImg.classList.remove(CLASSES.parallaxAfter);
      }

      this.imageOffsetAfter = this.getDistance(this.$parallaxedImg, this.$targetImgPositionEl) + imgAfterOffset;

      // Restore after/before after the calculation is done.
      if (containedBefore) {
        this.$parallaxedImg.classList.add(CLASSES.parallaxBefore);
      }

      if (containedAfter) {
        this.$parallaxedImg.classList.add(CLASSES.parallaxBefore);
      }

      this.$parallaxedImg.classList.remove(CLASSES.parallaxNoTransition);
    }
  }

  sectionLeaveCb (index, nextIndex, direction) {
    if (!this.isResponsive) {
      if (nextIndex === this.index - 1) {
        this.$parallaxedImg.classList.add(CLASSES.parallaxBefore);

        if (this.$eyebrow) {
          this.unpinEyebrow();
        }
      }

      if (nextIndex === this.index) {
        this.$parallaxedImg.classList.remove(CLASSES.parallaxBefore);
        this.$parallaxedImg.classList.remove(CLASSES.parallaxAfter);
        this.$parallaxedImg.style.transform = '';
      }

      if (nextIndex === this.index + 1) {
        if (this.$eyebrow) {
          this.pinEyebrow(direction === 'up');
        }

        if (this.imageOffsetAfter) {
          this.$parallaxedImg.style.transform = `translateY(${this.imageOffsetAfter}px)`;
        }

        this.$parallaxedImg.classList.add(CLASSES.parallaxAfter);
      }

      if (nextIndex === this.index + 2) {
        if (this.$eyebrow) {
          this.unpinEyebrow(true);
        }
      }
    }
  }

  afterResponsiveCb (isResponsive) {
    this.isResponsive = isResponsive;

    if (this.isResponsive && this.$eyebrow) {
      this.unpinEyebrow();
    }
  }

  /**
   *  Calculate the distance between
   * @param {HTMLElement} $el1
   * @param {HTMLElement} $el2
   *
   * @return {number}
   */
  getDistance($el1, $el2) {
    const rect1 = $el1.getBoundingClientRect();
    const rect2 = $el2.getBoundingClientRect();
    return (rect2.y + rect2.height) - (rect1.y + rect1.height);
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
      this.$eyebrow.classList.add(CLASSES.eyebrowHidden);

      document.body.appendChild(this.$clonedEyebrow);

      if (animateOpacity) {
        this.$clonedEyebrow.classList.add(CLASSES.eyebrowFadedout);
        this.$clonedEyebrow.classList.add(CLASSES.eyebrowTransition);

        // Removing a class straight after appending to the DOM
        // prevents the animation to happen. This is a workarounf.
        // TODO: there might be a nicer approach
        setTimeout(() => {
          this.$clonedEyebrow.classList.remove(CLASSES.eyebrowFadedout);
          const transitionEndCb = (e) => {
            this.$clonedEyebrow.classList.remove(CLASSES.eyebrowTransition);
            this.$clonedEyebrow.removeEventListener('transitionend', transitionEndCb);
          }

          this.$clonedEyebrow.addEventListener('transitionend', transitionEndCb);
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
    if (this.$clonedEyebrow && this.eyebrowSticky === true) {
      if (animateOpacity) {
        const transitionEndCb = (e) => {
          this.$clonedEyebrow.parentNode.removeChild(this.$clonedEyebrow);
          this.$clonedEyebrow.classList.remove(CLASSES.eyebrowTransition)
          this.$clonedEyebrow.removeEventListener('transitionend', transitionEndCb);
        }

        this.$clonedEyebrow.addEventListener('transitionend', transitionEndCb);

        this.$clonedEyebrow.classList.add(CLASSES.eyebrowFadedout);
        this.$clonedEyebrow.classList.add(CLASSES.eyebrowTransition);
      } else {
        this.$clonedEyebrow.parentNode.removeChild(this.$clonedEyebrow);
      }
    }
    this.eyebrowSticky = false;
    this.$eyebrow.classList.remove(CLASSES.eyebrowHidden);
  }
}
