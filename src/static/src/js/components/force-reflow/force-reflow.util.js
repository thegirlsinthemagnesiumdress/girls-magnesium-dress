goog.module('dmb.components.forceReflow.util');

/**
 * It forces a browser reflow.
 * @param {HTNLElement} element
 */
function forceReflow(element=document.body) {
  window['__forceReflow__'] = !!element.offsetHeight;
}

exports = forceReflow;
