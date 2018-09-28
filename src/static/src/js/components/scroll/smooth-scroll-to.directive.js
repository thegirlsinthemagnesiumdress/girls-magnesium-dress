/**
 * @fileoverview AngularJS directive that copies  glue smooth scroll component but makes
 * the hash change configurable. (Hash change is disabled by default).
 *
 * Example:
 *
 * Use as a directive
 * 1) Use smooth scroll directive without glue jumplink directive
 * <a href="##red-box" glue-smooth-scroll>Link</a>
 *
 * 2) Use smooth scroll directive with glue jumplink directive
 * <a href="#red-box" glue-smooth-scroll>Link</a>
 *
 * 3) Use smooth scroll directive with configurations
 * <a href="##red-box" glue-smooth-scroll glue-smooth-scroll-duration="1000"
 * glue-smooth-scroll-easing="easeInSine">Link</a>
 *
 *  4) Use smooth scroll directive with configurations
 * <a href="##red-box" glue-smooth-scroll glue-smooth-scroll-duration="1000"
 * glue-smooth-scroll-hash="false">Link</a>
 *
 * For documentation and demo see
 * https://glue-docs.appspot.com/docs/components/angularjs/smoothscroll#demo-smoothscroll-with-jumplink
 * https://glue-docs.appspot.com/docs/components/angularjs/smoothscroll#demo-smoothscroll-as-a-directive
 * https://glue-docs.appspot.com/docs/components/angularjs/smoothscroll/api/
 */

goog.module('dmb.components.scroll.smoothScrollDirective');


const SmoothScrollCtrl = goog.require('dmb.components.scroll.SmoothScrollCtrl');


/** @const {string} */
const DIRECTIVE_NAME = 'dmbSmoothScroll';


/**
 * Glue smooth scroll Directive, it allows an animated smooth scroll from
 * one location within the document to another. It broadcasts a
 * 'startScroll' event when scroll starts and broadcasts a 'endScroll' when
 * scroll ends. Configurable parameters include duration of the scroll, offset
 * of the target element, the easing function and URL hash.
 * Generally Glue scroll directive is preferred for links, but Glue SmoothScroll
 * directive is preferred for animated scroll.
 * @param {!service.SmoothScrollService} glueSmoothScrollService Glue smooth
 *     scroll service.
 * @param {!angular.$location} $location Angular location service.
 * @return {!angular.Directive} Smooth scroll directive definition object.
 * @ngInject
 */
function directive(glueSmoothScrollService, $location) {
  return {
    restrict: 'A',
    controller: SmoothScrollCtrl.main,
  };
}


exports = {
  DIRECTIVE_NAME,
  main: directive,
};
