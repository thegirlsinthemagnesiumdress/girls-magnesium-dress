import {forceReflow} from './force-reflow.util';

/** @const {string} */
const MODULE_NAME = 'forceReflow';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);

module.factory('forceReflow', () => forceReflow);
