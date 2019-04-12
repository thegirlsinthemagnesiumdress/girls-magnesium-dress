goog.module('dmb.components.languageSelector.directive');


const languageSelectorCtrl = goog.require('dmb.components.languageSelector.controller');
const languageSelectorTemplate = goog.require('dmb.components.languageSelector.template');

/**
 * Language selector directive.
 * @ngInject
 * @return {Object} Config for the directive
 */
function LanguageSelectorDirective() {
  return {
    restrict: 'E',
    scope: {
      'languages': '@',
      'url': '@',
      'selectedLanguage': '@',
    },
    controller: languageSelectorCtrl.main,
    controllerAs: languageSelectorCtrl.CONTROLLER_AS_NAME,
    template: languageSelectorTemplate,
  };
}


/** @const {string} */
LanguageSelectorDirective.DIRECTIVE_NAME = 'dmbLanguageSelector';


exports = {
  main: LanguageSelectorDirective,
  DIRECTIVE_NAME: LanguageSelectorDirective.DIRECTIVE_NAME,
};
