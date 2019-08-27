import * as directive from './progress-grid.directive';


/** @const {string} */
const MODULE_NAME = 'progressGrid';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
