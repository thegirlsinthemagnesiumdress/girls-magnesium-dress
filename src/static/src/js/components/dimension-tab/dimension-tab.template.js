goog.module('dmb.components.dimensionTab.template');

/* eslint-disable max-len */
const dimensionTabTemplate = `
<div
    class="dmb-dimension-tabs__content dmb-dimension-tabs__content--level-{[dimensionTabCtrl.floorDMB]}">

  <div class="dmb-dimension-tabs__intro">
    <div class="h-c-grid">
      <div class="dmb-dimension-tabs__logo-col h-c-grid__col h-c-grid__col--2 h-c-grid__col--offset-1">
        <img
            ng-src="{[dimensionTabCtrl.dmbStaticUrl]}img/retail/dimensions/{[dimensionTabCtrl.dimensionClassNames[dmbDimensionTab]]}.svg"
            alt="{[dmbDimensionTab]} logo"
            class="dmb-dimension-tabs__logo">
      </div>
      <div class="h-c-grid__col h-c-grid__col--8 h-c-grid__col--offset-1">
        <h3 class="h-c-headline h-c-headline--three">
          {[dimensionTabCtrl.dimensionHeaders[dmbDimensionTab]]}
        </h3>
        <p class="h-c-headline h-c-headline--subhead">
          {[dimensionTabCtrl.dimensionHeadersDescription[dmbDimensionTab]]}
        </p>
      </div>
    </div>
  </div>

  <div class="dmb-dimension-tabs__results">
    <div class="h-c-grid">
      <div class="dmb-dimension-tabs__results-highlight h-c-grid__col h-c-grid__col--4 h-u-text-center">
        <div class="dmb-dimension-tabs__results-heading h-c-headline h-c-headline--two">
          {[dimensionTabCtrl.levels[dimensionTabCtrl.floorDMB]]}
        </div>
        <div class="dmb-dimension-tabs__results-subheading h-u-font-weight-regular">
          in this dimension
        </div>
        <div class="dmb-dimension-tabs__results-value h-c-headline h-c-headline--three">
          {[dimensionTabCtrl.dmb|number:1]}/{[dimensionTabCtrl.levelsTotal]}
        </div>
      </div>
      <div class="h-c-grid__col h-c-grid__col--7">
        {[ dimensionTabCtrl.dimensionLevelDescription[dmbDimensionTab][dimensionTabCtrl.floorDMB]]}
      </div>
    </div>
  </div>

  <div class="dmb-dimension-tabs__progress-grid">
    <dmb-progress-grid
        data-company-name="{[companyName]}"
        data-rating-main="dimensionTabCtrl.dmb"
        data-industry-avg="dimensionTabCtrl.industryDmb"
        data-industry-best="dimensionTabCtrl.industryDmb_bp"
        data-industry-ready="!!dimensionTabCtrl.industryResult">
    </dmb-progress-grid>
  </div>


  <div class="h-c-grid">
    <div class="h-c-grid__col h-c-grid__col--10 h-c-grid__col--offset-1">
      <h4 class="dmb-dimension-tabs__recommendations-header h-c-headline h-c-headline--four">
        <img
            ng-src="{[dimensionTabCtrl.dmbStaticUrl]}img/retail/dimensions/{[dimensionTabCtrl.dimensionClassNames[dmbDimensionTab]]}.svg"
            alt="{[dimensionTabCtrl.dimensionHeaders[dmbDimensionTab]]} logo">
        {[dimensionTabCtrl.dimensionHeaders[dmbDimensionTab]]}
      </h4>
      <h4 class="h-c-headline h-c-headline--two">
        <span ng-if="dimensionTabCtrl.floorDMB < (dimensionTabCtrl.levelsTotal - 1)">
          You could be {[dimensionTabCtrl.levels[dimensionTabCtrl.floorDMB + 1]]}
        </span>
        <span ng-if="dimensionTabCtrl.floorDMB === (dimensionTabCtrl.levelsTotal - 1)">
          Congratulations, you're in the top group for data maturity
        </span>
      </h4>

      <div class="dmb-dimension-tabs__recommendations">
        <h4 class="h-c-headline h-c-headline--four">
          <span ng-if="dimensionTabCtrl.floorDMB < (dimensionTabCtrl.levelsTotal - 1)">
            Here's how you get there:
          </span>
          <span ng-if="dimensionTabCtrl.floorDMB === (dimensionTabCtrl.levelsTotal - 1)">
            Here's how to get even better:
          </span>
        </h4>

        <ul class="dmb-dimension-tabs__recommendation-list">
          <li
              class="dmb-dimension-tabs__recommendation"
              ng-repeat="recommendation in dimensionTabCtrl.dimensionLevelRecommendations[dmbDimensionTab][dimensionTabCtrl.floorDMB]">
            <h5 class="dmb-dimension-tabs__recommendation-heading h-c-headline h-c-headline--subhead h-u-font-weight-medium">
              {[recommendation.header]}
            </h5>
            <p>
              {[recommendation.text]}
            </p>
            <a
                ng-if="recommendation.cta"
                class="dmb-dimension-tabs__recommendation-cta dmb-h-hidden--print h-c-button h-c-button--secondary"
                href="{[recommendation.cta.link]}"
                target="_blank">
              {[recommendation.cta.text]}
            </a>
          </li>
        </ul>
      </div>

    </div>
  </div>



</div>
`;
/* eslint-enable max-len */

exports = dimensionTabTemplate;
