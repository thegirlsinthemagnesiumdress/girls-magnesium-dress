goog.module.declareNamespace('dmb.components.forceReflow.util');

/**
 * It forces a browser reflow.
 * @param {HTMLElement} element
 */
export function forceReflow(element=document.body) {
  window['__forceReflow__'] = !!element.offsetHeight;
}
