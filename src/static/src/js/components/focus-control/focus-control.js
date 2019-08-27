import * as run from './focus-control.run';


/** @const {string} */
const MODULE_NAME = 'focusControl';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);

module.run(run.main);
