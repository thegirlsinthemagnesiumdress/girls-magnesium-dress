import * as directive from './progress-table.directive';


/** @const {string} */
const MODULE_NAME = 'progressTable';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
