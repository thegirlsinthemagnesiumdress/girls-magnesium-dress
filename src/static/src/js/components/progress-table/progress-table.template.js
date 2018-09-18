goog.module('dmb.components.progressTable.template');

const template = `
<div class="dmb-progress-table dmb-h-mb--big dmb-progress-table--{[progressTableCtrl.getClass(ratingMain)]}">
  <div class="dmb-progress-table__col"></div>
  <div class="dmb-progress-table__col dmb-progress-table__col--nascent">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">Nascent</h3>
    <div class="dmb-progress-table__row dmb-progress-table__row--main"
      aria-label="Your Company is Emerging"
      ng-style="{width: progressTableCtrl.getProgressWidth(ratingMain)}"
      data-rating="{[ratingMain|number:1]}">
      <div class="dmb-progress-table__label">
        <span class="dmb-progress-table__company">{[companyName]}</span>
        <span class="dmb-progress-table__rating" aria-label="Your company rating">{[ratingMain|number:1]}</span>
      </div>
    </div>
    <div class="dmb-progress-table__row dmb-progress-table__row--ind-avg"
      ng-style="{width: progressTableCtrl.getProgressWidth(industryAvg)}"
      data-rating="{[industryAvg|number:1]}">
      <div class="dmb-progress-table__label">
        <button class="dmb-report-page__info" dmb-side-panel-trigger="#dmb-report-left-side-panel-two">
        </button>&nbsp;Industry average
        <span class="dmb-progress-table__rating" aria-label="industry average rating">{[industryAvg|number:1]}</span>
      </div>
    </div>
    <div class="dmb-progress-table__row dmb-progress-table__row--ind-best"
      ng-style="{width: progressTableCtrl.getProgressWidth(industryBest)}"
      data-rating="{[industryBest|number:1]}">
      <div class="dmb-progress-table__label">
        <button class="dmb-report-page__info" dmb-side-panel-trigger="#dmb-report-left-side-panel-two">
        </button>&nbsp;Industry best
        <span class="dmb-progress-table__rating" aria-label="industry best rating">{[industryBest|number:1]}</span>
      </div>
    </div>
    <div class="dmb-progress-table__banner h-c-headline h-c-headline--subhead h-u-font-weight-medium"
      ng-if="!industryAvg">
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
