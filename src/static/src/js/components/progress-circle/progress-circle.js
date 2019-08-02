goog.module.declareNamespace('dmb.components.progressCircle');

import * as directive from './progress-circle.directive';


/** @const {string} */
const MODULE_NAME = 'progressCircle';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
