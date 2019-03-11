Qualtrics.SurveyEngine.addOnReady(function () {
  jQuery("#Wrapper").addClass("dmb-survey--start");
});

Qualtrics.SurveyEngine.addOnUnload(function () {
  jQuery("#Wrapper").removeClass("dmb-survey--start");
});