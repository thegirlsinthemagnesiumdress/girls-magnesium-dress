goog.module.declareNamespace('dmb.components.registration');

import * as controller from './registration.controller';


/** @const {string} */
const MODULE_NAME = 'registration';


/**
 * Allows to submit a company to the BE.
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);
