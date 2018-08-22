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

const scrollPosition = goog.require('dmb.survey.scrollPosition');
const stickyProgress = goog.require('dmb.survey.stickyProgress');

scrollPosition.init();
stickyProgress.init();
