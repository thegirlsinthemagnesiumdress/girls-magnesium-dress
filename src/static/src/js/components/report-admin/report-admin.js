import * as directive from './report-list.directive';

/** @const {string} */
const MODULE_NAME = 'reportAdmin';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);

module.directive(directive.DIRECTIVE_NAME, directive.main);
