goog.module('dmb.components.forceReflow');

const reflow = goog.require('dmb.components.forceReflow.util');

/** @const {string} */
const MODULE_NAME = 'forceReflow';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);

module.factory('forceReflow', () => reflow);


/**
 * Registration angular module.
 * @type {!angular.Module}
 */
exports.module = module;
