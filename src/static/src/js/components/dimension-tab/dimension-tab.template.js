goog.module('dmb.components.dimensionTab.template');

/* eslint-disable max-len */
const dimensionTabTemplate = `

<div class="dmb-report-page__tab-content dmb-tab">

  <div class="dmb-tab__header-grid h-c-grid">
    <div class="dmb-report-page__tab-static-col h-c-grid__col  h-c-grid__col--12 h-c-grid__col-l--5">
      <h2 class="dmb-print-page-header h-c-headline h-c-headline--one">{[dimensionTabCtrl.dimensionHeaders[dmbDimensionTab]]}</h2>
      <p>
      {[ dimensionTabCtrl.dimensionHeadersDescription[dmbDimensionTab] ]}
      </p>
    </div>

    <div class="dmb-report-page__tab-dynamic-col h-c-grid__col h-c-grid__col--12 h-c-grid__col-l--7">
      <div class="h-c-grid dmb-tab__subgrid">
        <div class="h-c-grid__col h-c-grid__col--12 h-c-grid__col-l--4">
            <div class="dmb-progress-circle dmb-progress-circle--dimension-main dmb-progress-circle--{[dmbDimensionTab]}"">
              <svg
                  dmb-progress-circle="dimensionTabCtrl.dmb"
                  class="dmb-progress-circle__prog-svg"
                  width="121" height="121" viewBox="0 0 120 120">
                <circle class="dmb-progress-circle__bg-bar" cx="60" cy="60" r="54" fill="none" stroke-width="12" />
                <circle class="dmb-progress-circle__prog-bar" cx="60" cy="60" r="54" fill="none" stroke-width="12" />
              </svg>
              <div class="dmb-progress-circle__icon"></div>
            </div>
            <div class="dmb-report-page__tab-progress-circle-results dmb-progress-circle__results">
              <span class="dmb-progress-circle__result">{[ dimensionTabCtrl.dmb|number : 1 ]}</span><span class="dmb-progress-circle__target">/<span class="dmb-progress-circle__target--value">4.0</span>
              </span>
            </div>
        </div>

        <div class="h-c-grid__col h-c-grid__col--12 h-c-grid__col-l--8">
          <h3 class="dmb-h-alt-font">
            <span class="dmb-report-page__headline-accent">You are </span><br><strong>{[ dimensionTabCtrl.floorDMB|dmbLevelText ]} </strong>
          </h3>
          <p>
            {[ dimensionTabCtrl.dimensionLevelDescription[dmbDimensionTab][dimensionTabCtrl.floorDMB] ]}
          </p>
        </div>
      </div>
    </div>
  </div>

  <dmb-progress-table
    data-rating-main="dimensionTabCtrl.dmb"
    data-industry-avg="dimensionTabCtrl.industryDmb"
    data-industry-best="dimensionTabCtrl.industryDmb_bp"
    data-company-name="{[company_name]}">
  </dmb-progress-table>

  <div class="dmb-report-page__recommendation-block dmb-tab__recommendation-block">
    <h3 class="h-c-headline h-c-headline--three">
      <span ng-if="dimensionTabCtrl.floorDMB < 3" class="dmb-report-page__headline-accent">You could be</span>
      <strong ng-if="dimensionTabCtrl.floorDMB < 3">{[ (dimensionTabCtrl.dmb + 1)|dmbLevelText ]}</strong>
      <span ng-if="dimensionTabCtrl.floorDMB >= 3" class="dmb-report-page__headline-accent">Congratulations,</span>
      <strong ng-if="dimensionTabCtrl.floorDMB >= 3">you're in the top 2% for marketing maturity</strong>
    </h3>

    <p
        ng-if="dimensionTabCtrl.floorDMB < 3"
        class="h-c-headline h-c-headline--four">Here's how you get there:</p>
    <p
        ng-if="dimensionTabCtrl.floorDMB >= 3"
        class="h-c-headline h-c-headline--four">Here's how to get even better:</p>

    <ul class="dmb-report-page__recommendations dmb-tab__recommendations">

      <li class="dmb-report-page__recommendation dmb-tab__recommendation dmb-report-page__recommendation--{[ recommendation.cta.class ]}"
        ng-repeat="recommendation in dimensionTabCtrl.dimensionLevelRecommendations[dmbDimensionTab][dimensionTabCtrl.floorDMB ]">
        <h4 class="h-c-headline h-c-headline--five h-u-font-weight-medium dmb-h-mb--small">{[ recommendation.header ]}</h4>
        <p>
          {[ recommendation.text ]}
        </p>
        <a class="dmb-button dmb-button--secondary dmb-report-page__cta" target="_blank" href="{[recommendation.cta.link]}" ng-if="recommendation.cta">
          <div class="dmb-button__icon dmb-report-page__cta-icon"></div>
          <div class="dmb-button__text dmb-report-page__cta-text">{[ recommendation.cta.text ]}</div>
        </a>
      </li>
    </ul>
  </div>

</div> <!-- .dmb-report-page__tab-content -->
`;
/* eslint-enable max-len */

exports = dimensionTabTemplate;
