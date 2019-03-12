Qualtrics.SurveyEngine.addOnReady(function () {
  var activeClass = 'dmb-survey-privacy-policy--visible';
  var element = jQuery('#' + this.questionId);
  element.addClass('dmb-survey-policy-checkbox');
  var dmbPrivacyPolicy = element.find('.dmb-survey-privacy-policy');
  var button = element.find('#dmb-read-more');
  button.click(function () {
    dmbPrivacyPolicy.toggleClass(activeClass);
  });
});
