Qualtrics.SurveyEngine.addOnReady(function () {
  var element = jQuery("#" + this.questionId);
  element.addClass("dmb-survey-user-details");
  inputElements = element.find(".InputText");
  inputElements.first().attr("placeholder", "Enter your email address (required)");
  inputElements.last().attr("placeholder", "Who else should be emailed the report? (optional)");
});