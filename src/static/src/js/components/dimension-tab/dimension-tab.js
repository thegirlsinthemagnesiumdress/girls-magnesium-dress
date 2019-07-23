goog.module.declareNamespace('dmb.components.dimensionTab');

import * as directive from '../dimension-tab/dimension-tab.directive';

/** @const {string} */
const MODULE_NAME = 'dimensionTab';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
