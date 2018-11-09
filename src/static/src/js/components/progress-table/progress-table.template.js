goog.module('dmb.components.progressTable.template');

const template = `
<div class="dmb-progress-table dmb-progress-table--{[progressTableCtrl.getClass(ratingMain)]}">
  <div class="dmb-progress-table__col"></div>
  <div class="dmb-progress-table__col dmb-progress-table__col--nascent">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">Nascent</h3>
    <div class="dmb-progress-table__row-wrp">
      <div class="dmb-progress-table__row dmb-progress-table__row--main"
          ng-class="{
            'dmb-progress-table__row--no-value': ratingMain == null,
            'dmb-progress-table__row--value-four': ratingMain == 4
          }"
          ng-style="{width: progressTableCtrl.getProgressWidth(ratingMain)}"
          aria-label="Your Company is {[ ratingMain|dmbLevelText]}"
          data-rating="{[ratingMain|number:1]}">
        <div class="dmb-progress-table__label" aria-hidden="true">
          <span class="dmb-progress-table__company">{[$root.reportCtrl.survey.company_name]}</span>
          <span class="dmb-progress-table__rating" aria-label="Your company rating">{[ratingMain|number:1]}</span>
        </div>
      </div>
    </div>
    <div class="dmb-progress-table__row-wrp" aria-label="{[industryAvg ? '' : 'Industry average is not available yet, sorry!' ]}">
      <div
        class="dmb-progress-table__row dmb-progress-table__row--ind-avg"
          ng-class="{
            'dmb-progress-table__row--no-value': industryAvg == null,
            'dmb-progress-table__row--value-four': industryAvg == 4
          }"
          ng-style="{width: progressTableCtrl.getProgressWidth(industryAvg)}"
          data-rating="{[industryAvg|number:1]}">
        <div class="dmb-progress-table__label">
          <span class="dmb-progress-table__company">
            <button class="dmb-report-page__info" dmb-side-panel-trigger="#dmb-report-left-side-panel-two" aria-label="Get more informations about the industry average">
            </button>&nbsp;<span aria-hidden="{[industryAvg == null]}">Industry average</span>
          </span>
          <span class="dmb-progress-table__rating" aria-label="industry average rating">{[industryAvg|number:1]}</span>
        </div>
      </div>
    </div>
    <div class="dmb-progress-table__row-wrp" aria-label="{[industryAvg ? '' : 'Industry best is not available yet, sorry!' ]}">
      <div class="dmb-progress-table__row dmb-progress-table__row--ind-best"
          ng-class="{
            'dmb-progress-table__row--no-value': industryBest == null,
            'dmb-progress-table__row--value-four': industryBest == 4
          }"
          ng-style="{width: progressTableCtrl.getProgressWidth(industryBest)}"
          data-rating="{[industryBest|number:1]}">
        <div class="dmb-progress-table__label">
          <span class="dmb-progress-table__company">
            <button class="dmb-report-page__info" dmb-side-panel-trigger="#dmb-report-left-side-panel-two" aria-label="Get more informations about the Industry best">
            </button>&nbsp;<span aria-hidden="{[industryAvg == null]}">Industry best</span>
          </span>
          <span class="dmb-progress-table__rating" aria-label="industry best rating">{[industryBest|number:1]}</span>
        </div>
      </div>
    </div>
    <div class="dmb-progress-table__banner h-c-headline h-c-headline--subhead h-u-font-weight-medium"
      ng-if="!industryAvg" aria-hidden="true">
      Industry average and best aren’t available yet, sorry!
    </div>
  </div>
  <div class="dmb-progress-table__col dmb-progress-table__col--emerging">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">Emerging</h3>
  </div>
  <div class="dmb-progress-table__col dmb-progress-table__col--connected">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">Connected</h3>
  </div>
  <div class="dmb-progress-table__col dmb-progress-table__col--multimoment">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">Multi-Moment</h3>
  </div>
</div>
`;

exports = template;
