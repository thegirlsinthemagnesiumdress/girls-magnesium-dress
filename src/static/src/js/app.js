goog.module.declareNamespace('dmb.app');

// In src/app.js
import * as glueApp from '@google/glue/lib/app/app';

// Glue Angular
import * as glueCommon from '@google/glue/lib/ng/common/common';
import * as glueZippy from '@google/glue/lib/ng/zippy/zippy';
import * as tabby from '@google/glue/lib/ng/tabby/tabby';

// Glue Vanilla
import {Header} from '@google/glue/lib/ui/header/component';

import * as focusControl from './components/focus-control/focus-control';
import * as headerFix from './components/header-fix/header-fix';
import * as registration from './components/registration/registration';
import * as scrollHandler from './components/scroll/scroll';
import * as sidePanel from './components/side-panel/side-panel';
import * as report from './components/report/report';
import * as progressCircle from './components/progress-circle/progress-circle';
import * as progressGrid from './components/progress-grid/progress-grid';
import * as progressTable from './components/progress-table/progress-table';
import * as dimensionTab from './components/dimension-tab/dimension-tab';
import * as forceReflow from './components/force-reflow/force-reflow';
import * as tenant from './tenants/tenantconf';
import * as languageSelector from './components/language-selector/language-selector';
import * as copyComponent from './components/copy-component/copy-component';
import * as languageCode from './components/language-code/language-code';

// Vanilla JS DMB Components
import {csrfToken} from './components/csrf/csrf';
import {bootstrapData} from './components/bootstrap/bootstrap-data';
import AccountsList from './components/accounts-list/accounts-list';
import Clippy from './components/clippy/component';
import ExportReports from './components/export/export-reports';

/** @type {!angular.Module} */
export const module = angular.module('dmb', [
  focusControl.module.name,
  glueCommon.module.name, // Progressive enhancement/browser detections.
  glueZippy.module.name,
  'ngAnimate',
  headerFix.module.name,
  registration.module.name,
  scrollHandler.module.name,
  sidePanel.module.name,
  report.module.name,
  progressCircle.module.name,
  progressGrid.module.name,
  progressTable.module.name,
  dimensionTab.module.name,
  tabby.module.name,
  forceReflow.module.name,
  tenant.module.name,
  languageSelector.module.name,
  copyComponent.module.name,
  'hercules_template_bundle',
  'ngclipboard',
  languageCode.module.name,
]);

module.constant('csrfToken', csrfToken);
module.constant('bootstrapData', bootstrapData);

const bootstrapDataElement = document.getElementById('bootstrap-data');
// Add static url as constant
module.constant('dmbStaticUrl', bootstrapDataElement.dataset['staticUrl']);
// Detect CSS Grid support
const cssGridSupport = typeof bootstrapDataElement['style']['grid'] === 'string';
module.constant('cssGridSupport', cssGridSupport);

// Conditionally start the app if it's a supported browser.
glueApp.bootstrap(module.name);

// Initialise GLue Vanilla components
document.querySelectorAll('.glue-header').forEach(Header.attachTo);

// Attach copy component to elements with the custom dmb-copy-to-clipboard attribute.
document.querySelectorAll('[dmb-accounts-list]').forEach(AccountsList.attachTo);
document.querySelectorAll('[dmb-clippy]').forEach(Clippy.attachTo);
document.querySelectorAll('[dmb-export-reports]').forEach(ExportReports.attachTo);
