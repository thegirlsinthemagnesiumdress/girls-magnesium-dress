goog.module('dmb.components.copyComponent.controller');

const MESSAGE_CLASS = 'dmb-copy-comp__message';
const MESSAGE_SUCCESS_CLASS = `${MESSAGE_CLASS}--success`;
const MESSAGE_ERROR_CLASS = `${MESSAGE_CLASS}--error`;

/**
 * CopyComponent class controller.
 */
class CopyComponentCtrl {
  /**
   * CopyComponent controller
   * @param {!angular.Scope} $scope
   * @param {!angular.JQLite} $element
   *
   * @ngInject
   */
  constructor($scope, $element) {
    this.el = $element[0];
    this.copyMessageEl = this.el.querySelector(`.${MESSAGE_CLASS}`);
  }

  /**
   * Fn to run when copy is successful
   * @export
   */
  copySuccess() {
    this.copyMessageEl.classList.remove(MESSAGE_ERROR_CLASS);
    this.copyMessageEl.classList.add(MESSAGE_SUCCESS_CLASS);
  }

  /**
   * Fn to run when copy is unsuccessful
   * @export
   */
  copyError() {
    this.copyMessageEl.classList.remove(MESSAGE_SUCCESS_CLASS);
    this.copyMessageEl.classList.add(MESSAGE_ERROR_CLASS);
  }
}


/** @const {string} */
CopyComponentCtrl.CONTROLLER_NAME = 'CopyComponentCtrl';


exports = {
  main: CopyComponentCtrl,
  CONTROLLER_NAME: CopyComponentCtrl.CONTROLLER_NAME,
};
