Qualtrics.SurveyEngine.addOnload(function () {
  jQuery("#" + this.questionId).addClass("dmb-survey-banner-container");
});

Qualtrics.SurveyEngine.addOnReady(function () {
  jQuery("#Wrapper").addClass("dmb-survey--in-progress");
});