goog.declareModuleId('dmb.app');

// In src/app.js
import * as glueApp from '@google/glue/lib/app/app';

// Glue Angular
import * as glueCommon from '@google/glue/lib/ng/common/common';

// Glue Vanilla
import {GlueExpansionPanelsPanelGroup} from '@google/glue/lib/ui/expansionpanels/panelgroup/component';
import {Header} from '@google/glue/lib/ui/header/component';
import {PaginationPages} from '@google/glue/lib/ui/pagination/pages/component';
import {Tabs} from '@google/glue/lib/ui/tabs/component';

import * as focusControl from './components/focus-control/focus-control';
import * as headerFix from './components/header-fix/header-fix';
import * as registration from './components/registration/registration';
import * as scrollHandler from './components/scroll/scroll';
import * as sidePanel from './components/side-panel/side-panel';
import * as report from './components/report/report';
import * as reportList from './components/report-admin/report-admin';
import * as progressCircle from './components/progress-circle/progress-circle';
import * as progressGrid from './components/progress-grid/progress-grid';
import * as progressTable from './components/progress-table/progress-table';
import * as forceReflow from './components/force-reflow/force-reflow';
import * as tenant from './tenants/tenantconf';
import * as languageSelector from './components/language-selector/language-selector';
import * as copyComponent from './components/copy-component/copy-component';
import * as exportReports from './components/export/export-reports';
import * as languageCode from './components/language-code/language-code';
import tabState from './components/tab-state/tab-state';

import Clippy from './components/clippy/clippy';

/** @type {!angular.Module} */
export const module = angular.module('dmb', [
  focusControl.module.name,
  glueCommon.module.name, // Progressive enhancement/browser detections.
  'ngAnimate',
  headerFix.module.name,
  registration.module.name,
  scrollHandler.module.name,
  sidePanel.module.name,
  report.module.name,
  reportList.module.name,
  progressCircle.module.name,
  progressGrid.module.name,
  progressTable.module.name,
  forceReflow.module.name,
  tenant.module.name,
  languageSelector.module.name,
  copyComponent.module.name,
  exportReports.module.name,
  'hercules_template_bundle',
  'ngclipboard',
  languageCode.module.name,
]);

try {
  const bootstrapDatString = document.querySelector('[data-bootstrap-data]').dataset['bootstrapData'];
  const bootstrapData = bootstrapDatString ? JSON.parse(bootstrapDatString) : {};
  module.constant('bootstrapData', bootstrapData);
} catch (e) {
  console.warn('Not valid json');
}


const csrfTokenElement = document.querySelector('[name="csrfmiddlewaretoken"]');
const csrfToken = csrfTokenElement ? csrfTokenElement.value : '';
module.constant('csrfToken', csrfToken);

const bootstrapDataElement = document.getElementById('bootstrap-data');
// Add static url as constant
module.constant('dmbStaticUrl', bootstrapDataElement.dataset['staticUrl']);
// Detect CSS Grid support
const cssGridSupport = typeof bootstrapDataElement['style']['grid'] === 'string';
module.constant('cssGridSupport', cssGridSupport);

// Conditionally start the app if it's a supported browser.
glueApp.bootstrap(module.name);

// Attach copy component to elements with the custom dmb-copy-to-clipboard attribute.
document.querySelectorAll('[dmb-clippy]').forEach(Clippy.attachTo);

// Initialise Glue Vanilla components
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.glue-expansion-panels').forEach(GlueExpansionPanelsPanelGroup.attachTo);
  document.querySelectorAll('.glue-header').forEach(Header.attachTo);
  document.querySelectorAll('.glue-pagination-pages').forEach(PaginationPages.attachTo);
  document.querySelectorAll('.glue-tabs').forEach(Tabs.attachTo);
});

// Initialise Vanilla DMB components
document.querySelectorAll('[data-glue-pagination]').forEach(tabState);
