/**
 * @fileoverview Custom Element to handle scroll animation on scroll.
 *
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
import { debounce } from '../utils';
import { isResponsive } from '../initFullpage';

/**
 * Dom Selectors.
 * @enum {string}
 */
const DOM_SELECTORS = {
  parallaxedImg: '.tr-parallax-section__parallaxed-img',
  eyebrow: '.tr-parallax-section__eyebrow--pin'
};

/**
 * CSS Classes.
 * @enum {string}
 */
const CLASSES = {
  parallaxBefore: 'tr-parallax-section__parallaxed-img--step-minus-1',
  parallaxStep: 'tr-parallax-section__parallaxed-img--step',
  parallaxNoTransition: 'tr-parallax-section__parallaxed-img--no-transition',
  eyebrowSticky: 'tr-parallax-section__eyebrow--sticky',
  eyebrowHidden: 'tr-parallax-section__eyebrow--hidden',
  eyebrowFadedout: 'tr-parallax-section__eyebrow--faded-out',
  eyebrowTransition: 'tr-parallax-section__eyebrow--transition-opacity',
  fpEnabled: 'fp-enabled'
};

/**
 * Vertical positional offset summed to image final position.
 * @const {number}
 */
const imgAfterOffset = 20;


/**
 * Custom Element Section Class.
 * @extends {HTMLElement}
 */
export default class ParallaxSection extends HTMLElement {
  constructor () {
    super();
    this.debouncedResize = debounce(this.onResize.bind(this), 200);

    this.subscriptions = [];
  }


  /**
   * Invoked when the custom element is first connected
   * to the document's DOM.
   */
  connectedCallback () {
    this.$parallaxedImg = this.querySelector(DOM_SELECTORS.parallaxedImg);
    this.$eyebrow = this.querySelector(DOM_SELECTORS.eyebrow);
    const imgTargetSelector = this.$parallaxedImg.getAttribute('data-parallax-target');
    this.$targetImgPositionEl = imgTargetSelector ? document.querySelector(imgTargetSelector) : null;
    this.subSectionsNumber = window.parseInt(this.getAttribute('data-sub-sections-number'), 10) || 2;


    this.subscriptions
      .push(pubsub.subscribe('section-leave', (topic, ...args) => {
        this.sectionLeaveCb(...args);
      }));

    this.subscriptions
      .push(pubsub.subscribe('after-responsive', (topic, ...args) => {
        this.afterResponsiveCb(...args);
      }));

      this.subscriptions
        .push(pubsub.subscribe('fullpage-init', () => {
          // Fullpage.js updates the dom and inserts a wrapper to our sections.
          this.$sectionWrp = this.parentNode.parentNode;
          this.index = [...this.$sectionWrp.parentNode.children].indexOf(this.$sectionWrp) + 1;
          this.isResponsive = isResponsive();

          if (!this.$parallaxedImg.complete || this.$parallaxedImg.naturalWidth === 0) {
            this.$parallaxedImg.onload = this.onSectionRendered.bind(this);
          } else {
            this.onSectionRendered();
          }

          window.addEventListener('resize', this.debouncedResize);
        }));
  }

  /**
   * Invoked when the custom element is disconnected
   * from the document's DOM.
   */
  disconnectedCallback () {
    window.removeEventListener('resize', this.debouncedResize);
    this.subscriptions.forEach((sub) => pubsub.unsubscribe(sub));
    this.subSectionsNumber = 0;
  }

  /**
   * Fullpage.js onLeave event handler.
   * Handles eyebrow pinning and image animations.
   *
   * @param {number} index Leaving section index.
   * @param {number} nextIndex Next section index.
   * @param {string} direction Whether the direction is UP or DOWN.
   */
  sectionLeaveCb (index, nextIndex, direction) {
    if (!this.isResponsive) {
      const stepClasses = [...this.$parallaxedImg.classList].filter((cssClass) => cssClass.match(CLASSES.parallaxStep));

      // Previous step.
      if (nextIndex === this.index - 1) {
        stepClasses.forEach((cssClass) => this.$parallaxedImg.classList.remove(cssClass));
        this.$parallaxedImg.classList.add(CLASSES.parallaxBefore);

        if (this.$eyebrow) {
          this.unpinEyebrow();
        }
      }

      // Current step.
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
      }

      if (nextIndex >= this.index && nextIndex <= this.index + this.subSectionsNumber) {
        this.$parallaxedImg.classList.remove(CLASSES.parallaxBefore);

        // Remove step classes.
        stepClasses.forEach((cssClass) => this.$parallaxedImg.classList.remove(cssClass));

        // Add current step class.
        this.$parallaxedImg.classList.add(`${CLASSES.parallaxStep}-${nextIndex - this.index}`);
      }

      if (nextIndex === this.index + this.subSectionsNumber - 1 &&
          nextIndex !== this.index + 1) {
        if (this.$eyebrow) {
          this.pinEyebrow(direction === 'up');
        }
      }

      if (nextIndex === this.index + this.subSectionsNumber) {
        if (this.$eyebrow) {
          this.unpinEyebrow(true);
        }
      }
    }
  }

    /**
   * Fullpage.js afterResponsive event handler.
   * Initializes or destroys the scroll monitor.
   *
   * @param {bool} isResponsive Whethere snap scroll is enable or not.
   */
  afterResponsiveCb (isResponsive) {
    this.isResponsive = isResponsive;

    if (this.isResponsive && this.$eyebrow) {
      this.unpinEyebrow();
    }
  }

  /**
   * Callback executed when the section has completed rendering.
   */
  onSectionRendered () {
    window.setTimeout(() => {
      this.setImageAfterOffset();
      this.setEyebrowRect();
    })
  }

  /**
   * Calculates the final image position.
   */
  setImageAfterOffset () {
    if (this.$targetImgPositionEl) {
      let containedBefore;
      let containedAfter;
      let transformed;

      const stepClasses = [...this.$parallaxedImg.classList].filter((cssClass) => cssClass.match(CLASSES.parallaxStep));
      const currentStepClass = stepClasses.length > 0 ? stepClasses[0] : 0;


      this.$parallaxedImg.classList.add(CLASSES.parallaxNoTransition);

      // Removes before/after classes (and inline styles) and saves if they were
      // set to be able to restore them after the calculation is done.
      if (this.$parallaxedImg.style.transform) {
        this.$parallaxedImg.style.transform = '';
        transformed = true;
      }

      if (currentStepClass) {
        this.$parallaxedImg.classList.remove(currentStepClass);
      }

      this.imageOffsetAfter = this.getDistance(this.$parallaxedImg, this.$targetImgPositionEl) + imgAfterOffset;

      if (currentStepClass) {
        this.$parallaxedImg.classList.add(currentStepClass);
      }

      if (transformed) {
        this.$parallaxedImg.style.transform = `translateY(${this.imageOffsetAfter}px)`;
      }

      window.setTimeout(() => {
        this.$parallaxedImg.classList.remove(CLASSES.parallaxNoTransition);
      });
    }
  }

  /**
   *  Calculates the distance between two elements.
   *
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
   * Saves the eyebrow position.
   */
  setEyebrowRect() {
    if (this.$eyebrow) {
      const sectionWrapper = this.$sectionWrp.getBoundingClientRect();
      const eyebrowRect = this.$eyebrow.getBoundingClientRect();
      this.eyebrowRect = {
        x: eyebrowRect.x,
        y: eyebrowRect.y - sectionWrapper.y,
        width: eyebrowRect.width,
        height: eyebrowRect.height
      };
    }
  }

  /**
   * Clones the eyebrows and sets it to have a sticky behavior.
   *
   * @param {bool} animateOpacity Whether or not the eyebrow opacity should be animated when pinning.
   */
  pinEyebrow (animateOpacity) {
    if (!this.eyebrowSticky && this.eyebrowRect) {
      // Clones the eyebrow and appends it to the body in order to keep the
      // position fixed working. Fullpage.js transforms the page and that affects
      // fixed positioning. https://www.w3.org/TR/css-transforms-1/#module-interactions
      this.$clonedEyebrow = this.$eyebrow.cloneNode(true);
      this.$clonedEyebrow.classList.add(CLASSES.eyebrowSticky);
      this.$clonedEyebrow.style.top = `${this.eyebrowRect.y}px`;
      this.$clonedEyebrow.style.left = `${this.eyebrowRect.x}px`;
      this.$clonedEyebrow.style.width = `${this.eyebrowRect.width}px`;
      this.$clonedEyebrow.style.height = `${this.eyebrowRect.height}px`;
      this.$eyebrow.classList.add(CLASSES.eyebrowHidden);

      document.body.appendChild(this.$clonedEyebrow);

      if (animateOpacity) {
        this.$clonedEyebrow.classList.add(CLASSES.eyebrowFadedout);
        this.$clonedEyebrow.classList.add(CLASSES.eyebrowTransition);

        // Removing a class straight after appending to the DOM
        // prevents the animation from happening. This is a workaround.
        // TODO (pchillari): there might be a nicer approach
        setTimeout(() => {
          this.$clonedEyebrow.classList.remove(CLASSES.eyebrowFadedout);
          const transitionEndCb = (e) => {
            this.$clonedEyebrow.classList.remove(CLASSES.eyebrowTransition);
            this.$clonedEyebrow.removeEventListener('transitionend', transitionEndCb);
          };

          this.$clonedEyebrow.addEventListener('transitionend', transitionEndCb);
        }, 100);
      }

      this.eyebrowSticky = true;
    }
  }

  /**
   * Removes the cloned sticky eyebrow from the dom.
   * @param {bool} animateOpacity Whether or not the eyebrow opacity should be animated when unpinning.
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

  /**
   * Updates the pinned eyebrow position.
   */
  updatePinnedEyeBrow() {
    if (this.$clonedEyebrow) {
      this.$clonedEyebrow.style.top = `${this.eyebrowRect.y}px`;
      this.$clonedEyebrow.style.left = `${this.eyebrowRect.x}px`;
      this.$clonedEyebrow.style.width = `${this.eyebrowRect.width}px`;
      this.$clonedEyebrow.style.height = `${this.eyebrowRect.height}px`;
    }
  }

  /**
   * Window resize event handler.
   */
  onResize () {
    const self = this;
    this.setEyebrowRect();
    if (this.eyebrowSticky && this.$eyebrow) {
      this.updatePinnedEyeBrow();
    }
    this.setImageAfterOffset();
  }
}
