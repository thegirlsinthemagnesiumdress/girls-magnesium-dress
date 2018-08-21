goog.module('dmb.components.headerFix');

const HeaderFoundation = goog.require('glue.ui.header.HeaderFoundation');


/** @const {string} */
const MODULE_NAME = 'headerFix';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.run(headerFixRun);


/**
 * @param {!Object} scrollService
 * @ngInject
 */
function headerFixRun(scrollService) {
  const headerEl = document.querySelector('.glue-header');

  if (!headerEl) {
    return;
  }

  scrollService.addListener(onScroll);

  /**
   * Handles the scroll event. Brings the header back at the top of the page
   * @param  {number} scrollY The vertical scroll position of the page
   */
  function onScroll(scrollY) {
    if (scrollY > 0) {
      return;
    }

    headerEl.classList.remove(HeaderFoundation.cssClasses.IS_WHOLLY_SCROLLED);
  }
}


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
