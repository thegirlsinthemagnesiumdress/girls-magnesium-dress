goog.module('dmb.survey');

/**
 * Defining the properties we use on the globally provided Qualtrics instance
 *
 * @type {{
 *  SurveyEngine: {
      addOnload:Function,
      addOnReady:Function,
      addOnUnload:Function
 *  }
 * }}
 */
window.Qualtrics;

const focusControl = goog.require('dmb.components.focusControl.run');
const scrollToFirstError = goog.require('dmb.survey.scrollToFirstError');
const sidePanel = goog.require('dmb.survey.sidePanel');
const stickyProgress = goog.require('dmb.survey.stickyProgress');

focusControl.main();
scrollToFirstError.init();
sidePanel.init();
stickyProgress.init();
