goog.module('dmb.components.progressGrid.template');

const template = `
<div
    class="dmb-progress-grid dmb-progress-grid--level-{[progressGridCtrl.floorDmbFactory_(ratingMain)]}">

    <!-- This list is visually hidden and only read out by screen readers -->
    <ul class="h-u-visually-hidden">
      <li>
        <span ng-if="!ratingMain">
          Fetching your company rating...
        </span>
        <span ng-if="ratingMain">
          Your company, {[companyName]}, has a rating of {[ratingMain|number:1]},
          which is a maturity level of {[progressGridCtrl.getLevelName(ratingMain)]}.
        </span>
      </li>
      <li>
        <span ng-if="!industryReady">
          Fetching industry average...
        </span>
        <span ng-if="industryReady">
          The industry average is {[industryAvg|number:1]},
          which is a maturity level of {[progressGridCtrl.getLevelName(industryAvg)]}.
        </span>
      </li>
      <li>
        <span ng-if="!industryReady">
          Fetching industry best...
        </span>
        <span ng-if="industryReady">
          The industry best is {[industryBest|number:1]},
          which is a maturity level of {[progressGridCtrl.getLevelName(industryBest)]}.
        </span>
      </li>
    </ul>

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
  <div class="dmb-progress-grid__label dmb-progress-grid__label--company h-u-font-weight-medium">
    {[companyName]}
  </div>
  <div class="dmb-progress-grid__label dmb-progress-grid__label--ind-avg h-u-font-weight-regular">
    <button
        class="dmb-h-hidden--print"
        dmb-side-panel-trigger="#dmb-industry-side-panel"
        aria-label="Get more information about the industry average">
       <svg role="img" class="dmb-svg dmb-svg--info" width="20px" height="20px">
          <use xlink:href="#info"></use>
        </svg>
    </button>
    <span aria-hidden="true">Industry average</span>
  </div>
  <div class="dmb-progress-grid__label dmb-progress-grid__label--ind-best h-u-font-weight-regular">
    <button
        class="dmb-h-hidden--print"
        dmb-side-panel-trigger="#dmb-industry-side-panel"
        aria-label="Get more information about the industry best">
       <svg role="img" class="dmb-svg dmb-svg--info" width="20px" height="20px">
          <use xlink:href="#info"></use>
        </svg>
    </button>
    <span aria-hidden="true">Industry best</span>
  </div>

  <!-- vertical bars -->
  <div
      class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--company"
      data-value="{[ratingMain|number:1]}"
      data-level-name="{[progressGridCtrl.getLevelName(ratingMain)]}"
      ng-style="{height: progressGridCtrl.getProgress(ratingMain)}"
      aria-hidden="true">
  </div>
  <div
      class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--ind-avg"
      data-value="{[industryAvg|number:1]}"
      data-level-name="{[progressGridCtrl.getLevelName(industryAvg)]}"
      ng-style="{height: progressGridCtrl.getProgress(industryAvg)}"
      aria-hidden="true">
  </div>
  <div
      class="dmb-progress-grid__v-bar dmb-progress-grid__v-bar--ind-best"
      data-value="{[industryBest|number:1]}"
      data-level-name="{[progressGridCtrl.getLevelName(industryBest)]}"
      ng-style="{height: progressGridCtrl.getProgress(industryBest)}"
      aria-hidden="true">
  </div>

  <!-- horizontal bars -->
  <div
      class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--company"
      data-value="{[ratingMain|number:1]}"
      ng-style="{width: progressGridCtrl.getProgress(ratingMain)}"
      aria-hidden="true">
  </div>
  <div
      class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--ind-avg"
      data-value="{[industryAvg|number:1]}"
      ng-style="{width: progressGridCtrl.getProgress(industryAvg)}"
      aria-hidden="true">
  </div>
  <div
      class="dmb-progress-grid__h-bar dmb-progress-grid__h-bar--ind-best"
      data-value="{[industryBest|number:1]}"
      ng-style="{width: progressGridCtrl.getProgress(industryBest)}"
      aria-hidden="true">
  </div>

  <!-- "Not available" banners -->
  <div
      class="dmb-progress-grid__banner dmb-progress-grid__banner--ind-avg h-u-font-weight-regular"
      ng-if="industryReady && !industryAvg">
    Not available yet
  </div>
  <div
      class="dmb-progress-grid__banner dmb-progress-grid__banner--ind-best h-u-font-weight-regular"
      ng-if="industryReady && !industryBest">
    Not available yet
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
