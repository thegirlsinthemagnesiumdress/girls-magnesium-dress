goog.module('dmb.components.dimensionTab.template');

/* eslint-disable max-len */
const dimensionTabTemplate = `

<div class="dmb-report-page__tab-content">

  <div class="h-c-grid">
    <div class="dmb-report-page__tab-static-col h-c-grid__col h-c-grid__col--5">
      <h2 class="dmb-print-page-header h-c-headline h-c-headline--one h-u-mb-std">{[dimensionTabCtrl.dimensionHeaders[dmbDimensionTab]]}</h2>
      <p>
      {[ dimensionTabCtrl.dimensionHeadersDescription[dmbDimensionTab] ]}
      </p>
    </div>

    <div class="dmb-report-page__tab-dynamic-col h-c-grid__col h-c-grid__col--7">
      <div class="dmb-report-page__tab-progress-circle">
        <div class="dmb-progress-circle dmb-progress-circle--{[dmbDimensionTab]}" data-progress="52.5">
          <svg
              dmb-progress-circle="dimensionTabCtrl.dmb"
              class="dmb-progress-circle__prog-svg"
              width="121" height="121" viewBox="0 0 120 120">
            <circle class="dmb-progress-circle__bg-bar" cx="60" cy="60" r="54" fill="none" stroke-width="12" />
            <circle class="dmb-progress-circle__prog-bar" cx="60" cy="60" r="54" fill="none" stroke-width="12" />
          </svg>
          <div class="dmb-progress-circle__icon"></div>
        </div>
        <div>
          <span class="dmb-progress-circle__result">{[ dimensionTabCtrl.dmb|number : 1 ]}</span>
          <span class="dmb-progress-circle__target">/
            <span class="dmb-progress-circle__target--value">4.0</span>
          </span>
        </div>
      </div>
      <div>
        <h3 class="h-c-headline h-c-headline--three h-u-mb-std">
          <span class="dmb-report-page__headline-accent">You are</span> <strong>{[ dimensionTabCtrl.floorDMB|dmbLevelText ]} </strong>
        </h3>
      <p>
          {[ dimensionTabCtrl.dimensionLevelDescription[dmbDimensionTab][dimensionTabCtrl.floorDMB] ]}
        </p>
      </div>
    </div>
  </div>

  <dmb-progress-table
    data-rating-main="dimensionTabCtrl.dmb"
    data-industry-avg="dimensionTabCtrl.industryDmb"
    data-industry-best="dimensionTabCtrl.industryDmb_bp"
    data-company-name="{[company_name]}">
  </dmb-progress-table>
  <div>
    <h3 class="h-c-headline h-c-headline--three h-u-mb-std">
      <span ng-if="dimensionTabCtrl.floorDMB < 3" class="dmb-report-page__headline-accent">You could be</span> <strong>{[ (dimensionTabCtrl.dmb + 1)|dmbLevelText ]}</strong>
      <span ng-if="dimensionTabCtrl.floorDMB >= 3" class="dmb-report-page__headline-accent">Congratulations, you're in the top 2% for marketing maturity</strong>
    </h3>

    <p
        ng-if="dimensionTabCtrl.floorDMB < 3"
        class="h-c-headline h-c-headline--four h-u-mb-xl">Here's how you get there:</p>
    <p
        ng-if="dimensionTabCtrl.floorDMB >= 3"
        class="h-c-headline h-c-headline--four h-u-mb-xl">Here's how to get even better:</p>

    <ul class="dmb-report-page__recommendations">

      <li ng-repeat="recomendation in dimensionTabCtrl.dimensionLevelRecomendations[dmbDimensionTab][dimensionTabCtrl.floorDMB - 1]">
        <h4 class="h-c-headline h-c-headline--five h-u-mb-std">{[ recomendation.header ]}</h4>
        <p>
          {[ recomendation.text ]}
        </p>
      </li>
    </ul>
  </div>

</div> <!-- .dmb-report-page__tab-content -->
`;
/* eslint-enable max-len */

exports = dimensionTabTemplate;
