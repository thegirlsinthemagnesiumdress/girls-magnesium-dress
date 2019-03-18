goog.module('dmb.components.progressGrid.template');

const template = `
<div class="dmb-progress-grid dmb-progress-grid--level-{[progressGridCtrl.floorDmbFactory_(companyLevel)]}">
  <!-- col-bg -->
  <div class="dmb-progress-grid__col-bg dmb-progress-grid__col-bg--level-{[$index]}"
    ng-repeat="level in progressGridCtrl.levels">
  </div>

  <!-- grid headings -->
  <div
      class="dmb-progress-grid__heading dmb-progress-grid__heading--level-{[$index]} h-c-eyebrow"
      ng-repeat="level in progressGridCtrl.levels">
    {[level]}
  </div>

  <!-- bar labels -->
  <div class="dmb-progress-grid__label dmb-progress-grid__label--company h-u-font-weight-medium">
    {[companyName]}
  </div>
  <div class="dmb-progress-grid__label dmb-progress-grid__label--ind-avg h-u-font-weight-regular">
    <button dmb-side-panel-trigger="#dmb-report-left-side-panel-two"
      aria-label="Get more informations about the industry average">
    </button> Industry average
  </div>
  <div class="dmb-progress-grid__label dmb-progress-grid__label--ind-best h-u-font-weight-regular">
    <button dmb-side-panel-trigger="#dmb-report-left-side-panel-two"
      aria-label="Get more informations about the industry best">
    </button> Industry best
  </div>

  <!-- vertical bars -->
  <div class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--company"
    data-value="{[companyLevel|number:1]}" data-level-name="{[progressGridCtrl.getLevelName(companyLevel)]}"
    ng-style="{height: progressGridCtrl.getProgress(companyLevel)}">
  </div>
  <div class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--ind-best"
    data-value="{[industryAvg|number:1]}"
    data-level-name="{[progressGridCtrl.getLevelName(industryAvg)]}"
    ng-style="{height: progressGridCtrl.getProgress(industryAvg)}">
  </div>
  <div class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--ind-avg"
    data-value="{[industryBest|number:1]}"
    data-level-name="{[progressGridCtrl.getLevelName(industryBest)]}"
    ng-style="{height: progressGridCtrl.getProgress(industryBest)}">
  </div>

  <!-- horizontal bars -->
  <div class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--company"
    data-value="{[companyLevel|number:1]}" ng-style="{width: progressGridCtrl.getProgress(companyLevel)}">
  </div>
  <div class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--ind-avg"
    data-value="{[industryAvg|number:1]}"
    ng-style="{width: progressGridCtrl.getProgress(industryAvg)}">
  </div>
  <div class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--ind-best"
    data-value="{[industryBest|number:1]}"
    ng-style="{width: progressGridCtrl.getProgress(industryBest)}">
  </div>
</div>
`;

exports = template;

/* EXAMPLE HTML

<dmb-progress-grid
    data-company-name="{[reportCtrl.survey.company_name]}"
    data-company-level="reportCtrl.result.dmb"
    data-industry-avg="reportCtrl.industryResult.dmb"
    data-industry-best="reportCtrl.industryResult.dmb_bp"
    data-industry-ready="!!reportCtrl.industryResult">
</dmb-progress-grid>
*/
