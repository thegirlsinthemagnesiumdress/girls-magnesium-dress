goog.module('dmb.survey.scrollToFirstError');

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
  window['Qualtrics']['SurveyEngine']['addOnReady'](scrollToFirstError);
}

/**
 * Sets the scroll position to the first error or the top of the questions (if
 * not on the first page or the survey)
 */
function scrollToFirstError() {
  const className = '.ValidationError';
  let firstError;
  // Get all validation errors
  const elements = document.querySelectorAll(className);
  // Get the first visible validation error element
  elements.forEach((elem) => {
    const style = getComputedStyle(elem);
    if (!firstError && style.display != 'none') {
      firstError = elem;
    }
  });
  // If there is a validation error visible then scroll to the error
  if (firstError) {
    // Get the parent so the whole element is visible on scroll
    firstError = firstError.closest('.QuestionOuter');
    // Use element.scollIntoView instead of window.scroll since all of the window
    // scroll methods refused to work.
    // Scrolls the page so the element in question is in the viewport
    firstError.scrollIntoView(true);
  }
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
