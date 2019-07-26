goog.module.declareNamespace('dmb.components.languageCode');


/** @const {string} */
const MODULE_NAME = 'languageCode';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.constant('LANGUAGE_CODE', document.documentElement.getAttribute('lang') || 'en' );
