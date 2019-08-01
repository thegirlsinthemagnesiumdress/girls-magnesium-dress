goog.module.declareNamespace('dmb.components.languageSelector');

import * as controller from './language-selector.controller';


/** @const {string} */
const MODULE_NAME = 'languageSelector';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);
