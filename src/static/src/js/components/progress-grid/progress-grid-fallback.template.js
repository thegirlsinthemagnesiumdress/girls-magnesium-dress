goog.module('dmb.components.progressGridFallback.template');

const template = `
<div class="dmb-progress-table">
  <div class="dmb-progress-table__col"></div>
  <div class="dmb-progress-table__col dmb-progress-table__col--level-0">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">{[progressGridCtrl.levels[0]]}</h3>
    <div class="dmb-progress-table__row-wrp">
      <div class="dmb-progress-table__row dmb-progress-table__row--main"
          ng-class="{
            'dmb-progress-table__row--no-value': ratingMain == null,
            'dmb-progress-table__row--value-four': ratingMain == 4
          }"
          ng-style="{width: progressGridCtrl.getProgress(ratingMain)}"
          aria-label="Your Company is {[progressGridCtrl.getLevelName(ratingMain)]}"
          data-rating="{[ratingMain|number:1]}">
        <div class="dmb-progress-table__label" aria-hidden="true">
          <span class="dmb-progress-table__company">{[companyName]}</span>
          <span class="dmb-progress-table__rating" aria-label="Your company rating">{[ratingMain|number:1]}</span>
        </div>
      </div>
    </div>
    <div class="dmb-progress-table__row-wrp">
      <div ng-if="industryReady && !industryAvg" class="dmb-progress-table__banner">
        Industry average is not available yet, sorry!
      </div>
      <div
        class="dmb-progress-table__row dmb-progress-table__row--ind-avg"
          ng-class="{
            'dmb-progress-table__row--no-value': industryAvg == null,
            'dmb-progress-table__row--value-four': industryAvg == 4
          }"
          ng-style="{width: progressGridCtrl.getProgress(industryAvg)}"
          data-rating="{[industryAvg|number:1]}">
        <div class="dmb-progress-table__label">
          <span class="dmb-progress-table__company">
            <button class="dmb-report-page__info" dmb-side-panel-trigger="#dmb-report-left-side-panel-two"
                aria-label="Get more informations about the industry average">
              <svg role="img" class="dmb-svg dmb-svg--info" width="20px" height="20px">
                <use xlink:href="#info-dark"></use>
              </svg>
            </button>&nbsp;<span aria-hidden="{[industryAvg == null]}">Industry average</span>
          </span>
          <span class="dmb-progress-table__rating" aria-label="industry average rating">{[industryAvg|number:1]}</span>
        </div>
      </div>
    </div>
    <div class="dmb-progress-table__row-wrp">
      <div ng-if="industryReady && !industryBest" class="dmb-progress-table__banner">
        Industry best is not available yet, sorry!
      </div>
      <div class="dmb-progress-table__row dmb-progress-table__row--ind-best"
          ng-class="{
            'dmb-progress-table__row--no-value': industryBest == null,
            'dmb-progress-table__row--value-four': industryBest == 4
          }"
          ng-style="{width: progressGridCtrl.getProgress(industryBest)}"
          data-rating="{[industryBest|number:1]}">
        <div class="dmb-progress-table__label">
          <span class="dmb-progress-table__company">
            <button class="dmb-report-page__info" dmb-side-panel-trigger="#dmb-report-left-side-panel-two"
                aria-label="Get more informations about the Industry best">
              <svg role="img" class="dmb-svg dmb-svg--info" width="20px" height="20px">
                <use xlink:href="#info-dark"></use>
              </svg>
            </button>&nbsp;<span aria-hidden="{[industryAvg == null]}">Industry best</span>
          </span>
          <span class="dmb-progress-table__rating" aria-label="industry best rating">{[industryBest|number:1]}</span>
        </div>
      </div>
    </div>
  </div>
  <div class="dmb-progress-table__col dmb-progress-table__col--level-1">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">{[progressGridCtrl.levels[1]]}</h3>
  </div>
  <div class="dmb-progress-table__col dmb-progress-table__col--level-2">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">{[progressGridCtrl.levels[2]]}</h3>
  </div>
  <div class="dmb-progress-table__col dmb-progress-table__col--level-3">
    <h3 class="dmb-progress-table__col-heading" aria-hidden="true">{[progressGridCtrl.levels[3]]}</h3>
  </div>
</div>
`;

exports = template;
