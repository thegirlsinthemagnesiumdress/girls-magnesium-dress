goog.module('dmb.survey.headerVisibility');

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
  window['Qualtrics']['SurveyEngine']['addOnload'](tempHideHeader);
  window['Qualtrics']['SurveyEngine']['addOnReady'](setHeaderVisibility);
}

/**
 * Sets the scroll position to the first error or the top of the questions (if
 * not on the first page or the survey). Depends on the progress bar for
 * working this out.
 */
function setHeaderVisibility() {
  const progress = document.getElementById('ProgressBarFillContainer');
  const header = document.getElementById('LogoContainer');
  const hiddenClass = 'dmb-h-hidden';

  if (!progress || !header) {
    return;
  }

  const progressText = progress.textContent.match(/[.\d]+%/);
  const progressPercent = progressText && progressText[0];

  if (!progressPercent || progressPercent === '0%') {
    header.classList.remove(hiddenClass);
  } else {
    header.classList.add(hiddenClass);
  }

  const firstError = [...document.querySelectorAll('.ValidationError')]
    .find((err) => err.style.display !== 'none');

  if (!firstError) {
    window.scrollTo(0, 0);
    return;
  }

  const progressContainer = document.getElementById('ProgressBar');

  const elementOffset = firstError.closest('.QuestionBody')
    .getBoundingClientRect().top + window.scrollY;
  const stickyHeight = progressContainer.offsetHeight + 20; // padding for good measure

  const newY = elementOffset - stickyHeight;

  // Need to trigger our scroll after theirs
  setTimeout(() => {
    window.scrollTo(0, newY);
  }, 0);
}


/**
 * the onload event happens before the progress is updated, and the onReady
 * event happens after they've scrolled up to show the header. This hides the
 * header temporarily for that transitional period until we can properly
 * detect if it should be there
 */
function tempHideHeader() {
  const header = document.getElementById('LogoContainer');
  const hiddenClass = 'dmb-h-hidden';

  if (!header) {
    return;
  }

  header.classList.add(hiddenClass);
}


exports = {
  init,
};
