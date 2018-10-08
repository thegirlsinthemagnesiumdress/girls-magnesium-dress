goog.module('dmb.components.scroll.service');

/**
 * scrollService angular factory
 * @return {Object} The external bindings for the factory
 */
function scrollService() {
  let listeners = [];
  let isListening = false;
  let frameHandled = false;

  return {
    addListener,
    removeListener,
    getElementOffsetTop,
  };

  /**
   * Registers an event listener for scrolling
   * @param {Function} toAdd A function to be called when scrolling happens
   */
  function addListener(toAdd) {
    listeners.push(toAdd);

    if (!isListening) {
      document.addEventListener('scroll', onScroll);
      isListening = true;
    }
  }

  /**
   * @param  {Function} toRemove Removing a function from the list of those to be called
   */
  function removeListener(toRemove) {
    listeners = listeners.filter((listener) => listener !== toRemove);

    if (!listeners.length) {
      document.removeEventListener('scroll', onScroll);
      isListening = false;
    }
  }

  /**
   * Triggered when the native scroll event happens. Throttles this using RAF
   */
  function onScroll() {
    if (frameHandled) {
      return;
    }

    window.requestAnimationFrame(onNextFrame);
    frameHandled = true;
  }

  /**
   * Fired the first frame after a scroll event. Calls all of the listeners with the scroll value.
   */
  function onNextFrame() {
    const {scrollY} = window;
    listeners.forEach((listener) => listener(scrollY));
    frameHandled = false;
  }

    /**
   *
   * @param {HTMLElement} elem
   * @return {number} distance from top of the document.
   */
  function getElementOffsetTop( elem ) {
    let location = 0;
    if (elem.offsetParent) {
        do {
            location += elem.offsetTop;
            elem = elem.offsetParent;
        } while (elem);
    }
    return location >= 0 ? location : 0;
  }
}

exports = {
  SERVICE_NAME: 'scrollService',
  main: scrollService,
};
