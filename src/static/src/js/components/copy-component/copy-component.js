import * as controller from '../copy-component/copy-component.controller';


/** @const {string} */
const MODULE_NAME = 'copyComponent';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.controller(controller.CONTROLLER_NAME, controller.main);
