(function() {
  /* global Qualtrics */
  /* eslint-disable no-var */

  /*
   * Possible events:
   * - addOnload
   * - addOnReady
   * - addOnUnload
   */

  Qualtrics.SurveyEngine.addOnReady(setScrollPosition);

  /**
   * Sets the scroll position to the first error or the top of the questions (if
   * not on the first page or the survey). Depends on the progress bar for
   * working this out.
   */
  function setScrollPosition() {
    var progress = document.getElementById('ProgressBarFillContainer');
    var questions = document.getElementById('Questions');

    if (!progress || !questions) {
      return;
    }

    var progressText = progress.textContent.match(/[.\d]+%/);
    var progressPercent = progressText && progressText[0];

    if (!progressPercent || progressPercent === '0%') {
      return;
    }

    var questionOffset = (findError() || questions).getBoundingClientRect().y + window.scrollY;

    console.debug('[Q] scrollTo', questionOffset); // eslint-disable-line

    // @TODO maybe make this a smooth scroll down the line
    window.scrollTo(0, questionOffset);
  }

  /**
   * Finds any errors on the page and returns the first visible one
   * @return {Element|undefined} Returns the first visible error if there is one
   */
  function findError() {
    var errors = document.querySelectorAll('.ValidationError');
    var visibleErrors = Array.prototype.filter.call(errors, function(error) {
      return error.style.display !== 'none';
    });
    return visibleErrors[0];
  }
}());
