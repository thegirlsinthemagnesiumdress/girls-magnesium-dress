goog.module.declareNamespace('dmb.components.scroll');

import * as scrollService from './scroll.service';
import * as directive from './scroll-aware.directive';
import * as pinTopDirective from './scroll-pin-top.directive';


/** @const {string} */
const MODULE_NAME = 'scroll';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.factory(scrollService.SERVICE_NAME, scrollService.main);
module.directive(directive.DIRECTIVE_NAME, directive.main);
module.directive(pinTopDirective.DIRECTIVE_NAME, pinTopDirective.main);
