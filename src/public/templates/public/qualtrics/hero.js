Qualtrics.SurveyEngine.addOnload(function () {

});

Qualtrics.SurveyEngine.addOnReady(function () {
  jQuery('#Wrapper').addClass('dmb-retail dmb-survey--start');

  var urlBox = jQuery('#dmb-survey-url');
  urlBox.val(window.location.href);
  var copyMessageEl = jQuery('#dmb-copy-message');

  jQuery('#dmb-copy-btn').click(function () {
    // Clear selection range in case user has text selected in page
    console.log('clicked');
    if (window.getSelection) {
      if (window.getSelection().empty) {  // Chrome
        window.getSelection().empty();
      } else if (window.getSelection().removeAllRanges) {  // Firefox
        window.getSelection().removeAllRanges();
      }
    } else if (document.selection) {  // IE
      document.selection.empty();
    }

    // Select URL text
    var range = document.createRange();
    range.selectNode(urlBox[0]);
    window.getSelection().addRange(range);

    // Copy URL text to clipboard
    try {
      var successful = document.execCommand('copy');
      if (successful) {
        copyMessageEl.text('Copied to clipboard!');
        copyMessageEl.removeClass('dmb-survey-copy-url__message--error');
        copyMessageEl.addClass('dmb-survey-copy-url__message--success');
      } else {
        copyMessageEl.text('Sorry, unable to copy.');
        copyMessageEl.removeClass('dmb-survey-copy-url__message--success');
        copyMessageEl.addClass('dmb-survey-copy-url__message--error');
      }
    } catch (err) {
      copyMessageEl.text('Sorry, unable to copy.');
      copyMessageEl.removeClass('dmb-survey-copy-url__message--success');
      copyMessageEl.addClass('dmb-survey-copy-url__message--error');
    }
  });
});

Qualtrics.SurveyEngine.addOnUnload(function () {
  jQuery("#Wrapper").removeClass("dmb-survey--start");
});
