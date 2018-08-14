goog.module('dmb.components.focusControl');

const run = goog.require('dmb.components.focusControl.run');


/** @const {string} */
const MODULE_NAME = 'focusControl';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.run(run.main);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
