        //{% if language.code == LANGUAGE_CODE %}selected="selected"{% endif %}>
goog.module('dmb.components.languageSelector.controller');

const FORM_ELEMENT = 'language-form';

/**
 * LanguageSelector class controller.
 */
class LanguageSelectorController {
  /**
   * LanguageSelector controller
   * @param {!angular.Scope} $scope
   * @param {!angular.JQLite} $element
   *
   * @ngInject
   */
  constructor($scope, $element) {
    this.form = $element[0];
  }

  /**
   * @export
   */
  changeLanguage() {
    console.log('submitting');
    this.form.submit();
  }
}


/** @const {string} */
LanguageSelectorController.CONTROLLER_NAME = 'LanguageSelectorCtrl';



exports = {
  main: LanguageSelectorController,
  CONTROLLER_NAME: LanguageSelectorController.CONTROLLER_NAME
};
