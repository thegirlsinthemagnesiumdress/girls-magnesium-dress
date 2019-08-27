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


export const main = LanguageSelectorController;
export const CONTROLLER_NAME = LanguageSelectorController.CONTROLLER_NAME;
