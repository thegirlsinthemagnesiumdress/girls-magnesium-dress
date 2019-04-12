goog.module('dmb.components.languageSelector.controller');


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
    this.form.submit();
  }
}


/** @const {string} */
LanguageSelectorController.CONTROLLER_NAME = 'LanguageSelectorCtrl';


exports = {
  main: LanguageSelectorController,
  CONTROLLER_NAME: LanguageSelectorController.CONTROLLER_NAME,
};
