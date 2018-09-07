goog.module('dmb.survey.scrollPosition');

/**
 * Binds the event listener
 */
function init() {
  /*
   * Possible events:
   * - addOnload
   * - addOnReady
   * - addOnUnload
   */
  window['Qualtrics']['SurveyEngine']['addOnReady'](setScrollPosition);
}

/**
 * Sets the scroll position to the first error or the top of the questions (if
 * not on the first page or the survey). Depends on the progress bar for
 * working this out.
 */
function setScrollPosition() {
  const progress = document.getElementById('ProgressBarFillContainer');
  const questions = document.getElementById('Questions');

  if (!progress || !questions) {
    return;
  }

  const progressText = progress.textContent.match(/[.\d]+%/);
  const progressPercent = progressText && progressText[0];

  if (!progressPercent || progressPercent === '0%') {
    return;
  }

  const questionOffset = (findError() || questions).getBoundingClientRect().top + window.scrollY;

  // @TODO maybe make this a smooth scroll down the line
  window.scrollTo(0, questionOffset);
}

/**
 * Finds any errors on the page and returns the first visible one
 * @return {Element|undefined} Returns the first visible error if there is one
 */
function findError() {
  const errors = document.querySelectorAll('.ValidationError');
  const visibleErrors = Array.prototype.filter.call(errors, function(error) {
    return error.style.display !== 'none';
  });
  return visibleErrors[0];
}

exports = {
  init,
};
