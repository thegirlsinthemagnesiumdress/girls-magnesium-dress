goog.module('dmb.components.progressGrid.template');

const template = `
<div
    class="dmb-progress-grid dmb-progress-grid--level-{[progressGridCtrl.floorDmbFactory_(ratingMain)]}"
    ng-class="{
      'dmb-progress-grid--overflow-v': progressGridCtrl.verticalOverflow,
      'dmb-progress-grid--overflow-h': progressGridCtrl.horizontalOverflow}"
    aria-label="
      Your company rating is {[ratingMain|number:1]}.
      The industry average is {[industryAvg|number:1]}.
      The industry best is {[industryBest|number:1]}.">

  <!-- col-bg -->
  <div
      class="dmb-progress-grid__col-bg dmb-progress-grid__col-bg--level-{[$index]}"
      ng-repeat="level in progressGridCtrl.levels">
  </div>

  <!-- grid headings -->
  <div
      class="dmb-progress-grid__heading dmb-progress-grid__heading--level-{[$index]} h-c-eyebrow"
      ng-repeat="level in progressGridCtrl.levels"
      aria-hidden="true">
    {[level]}
  </div>

  <!-- bar labels -->
  <div
      class="dmb-progress-grid__label dmb-progress-grid__label--company h-u-font-weight-medium"
      aria-hidden="true">
    {[companyName]}
  </div>
  <div
      class="dmb-progress-grid__label dmb-progress-grid__label--ind-avg h-u-font-weight-regular"
      aria-hidden="true">
    <button
        dmb-side-panel-trigger="#dmb-report-left-side-panel-two"
        aria-label="Get more informations about the industry average">
       <svg role="img" class="dmb-svg dmb-svg--info" width="20px" height="20px">
          <use xlink:href="#info"></use>
        </svg>
    </button> Industry average
  </div>
  <div
      class="dmb-progress-grid__label dmb-progress-grid__label--ind-best h-u-font-weight-retegular"
      aria-hidden="true">
    <button
        dmb-side-panel-trigger="#dmb-report-left-side-panel-two"
        aria-label="Get more informations about the industry best">
       <svg role="img" class="dmb-svg dmb-svg--info" width="20px" height="20px">
          <use xlink:href="#info"></use>
        </svg>
    </button> Industry best
  </div>

  <!-- vertical bars -->
  <div
      class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--company"
      data-value="{[ratingMain|number:1]}"
      data-level-name="{[progressGridCtrl.getLevelName(ratingMain)]}"
      ng-style="{height: progressGridCtrl.getProgress(ratingMain)}">
  </div>
  <div
      class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--ind-avg"
      data-value="{[industryAvg|number:1]}"
      data-level-name="{[progressGridCtrl.getLevelName(industryAvg)]}"
      ng-style="{height: progressGridCtrl.getProgress(industryAvg)}">
  </div>
  <div
      class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--ind-best"
      data-value="{[industryBest|number:1]}"
      data-level-name="{[progressGridCtrl.getLevelName(industryBest)]}"
      ng-style="{height: progressGridCtrl.getProgress(industryBest)}">
  </div>

  <!-- horizontal bars -->
  <div
      class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--company"
      data-value="{[ratingMain|number:1]}"
      ng-style="{width: progressGridCtrl.getProgress(ratingMain)}">
  </div>
  <div
      class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--ind-avg"
      data-value="{[industryAvg|number:1]}"
      ng-style="{width: progressGridCtrl.getProgress(industryAvg)}">
  </div>
  <div
      class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--ind-best"
      data-value="{[industryBest|number:1]}"
      ng-style="{width: progressGridCtrl.getProgress(industryBest)}">
  </div>

  <!-- "Not available" banners -->
  <div
      class="dmb-progress-grid__banner dmb-progress-grid__banner--ind-avg h-c-footnote"
      ng-if="industryReady && !industryAvg">
    Industry average is not available yet, sorry!
  </div>
  <div
      class="dmb-progress-grid__banner dmb-progress-grid__banner--ind-best h-c-footnote"
      ng-if="industryReady && !industryBest">
    Industry best is not available yet, sorry!
  </div>
</div>
`;

exports = template;

/* EXAMPLE HTML

<dmb-progress-grid
    data-company-name="{[reportCtrl.survey.company_name]}"
    data-rating-main="reportCtrl.result.dmb"
    data-industry-avg="reportCtrl.industryResult.dmb"
    data-industry-best="reportCtrl.industryResult.dmb_bp"
    data-industry-ready="!!reportCtrl.industryResult">
</dmb-progress-grid>
*/
