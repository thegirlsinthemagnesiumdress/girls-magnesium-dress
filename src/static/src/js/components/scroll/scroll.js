goog.module.declareNamespace('dmb.components.scroll');

import * as config from '@google/glue/lib/ng/common/common';
import * as service from '@google/glue/lib/ng/smoothscroll/smoothscroll-service';

import * as scrollService from './scroll.service';
import * as directive from './scroll-aware.directive';
import * as pinTopDirective from './scroll-pin-top.directive';
import * as smoothScrollDirective from './smooth-scroll-to.directive';


/** @const {string} */
const MODULE_NAME = 'scroll';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, [
  config.module.name,
  service.module.name,
]);


module.factory(scrollService.SERVICE_NAME, scrollService.main);
module.directive(directive.DIRECTIVE_NAME, directive.main);
module.directive(pinTopDirective.DIRECTIVE_NAME, pinTopDirective.main);
module.directive(smoothScrollDirective.DIRECTIVE_NAME, smoothScrollDirective.main);
