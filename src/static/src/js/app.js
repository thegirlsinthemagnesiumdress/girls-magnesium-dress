goog.module.declareNamespace('dmb.app');

// In src/app.js
import * as glueApp from '@google/glue/lib/app/app';

// Glue Angular
import * as glueCommon from '@google/glue/lib/ng/common/common';
import * as glueZippy from '@google/glue/lib/ng/zippy/zippy';
import * as tabby from '@google/glue/lib/ng/tabby/tabby';

// Glue Vanilla
import {Header} from '@google/glue/lib/ui/header/component';

const focusControl = goog.require('dmb.components.focusControl');
import * as headerFix from './components/header-fix/header-fix';
const registration = goog.require('dmb.components.registration');
import * as scrollHandler from './components/scroll/scroll';
const sidePanel = goog.require('dmb.components.sidePanel');
const report = goog.require('dmb.components.report');
const reportList = goog.require('dmb.components.reportAdmin');
const progressCircle = goog.require('dmb.components.progressCircle');
const progressGrid = goog.require('dmb.components.progressGrid');
const progressTable = goog.require('dmb.components.progressTable');
const dimensionTab = goog.require('dmb.components.dimensionTab');
const forceReflow = goog.require('dmb.components.forceReflow');
const tenant = goog.require('dmb.components.tenant');
const languageSelector = goog.require('dmb.components.languageSelector');
const copyComponent = goog.require('dmb.components.copyComponent');
const exportReports = goog.require('dmb.components.exportReports');
import * as languageCode from './components/language-code/language-code';


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
  reportList.module.name,
  progressCircle.module.name,
  progressGrid.module.name,
  progressTable.module.name,
  dimensionTab.module.name,
  tabby.module.name,
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

// Initialise GLue Vanilla components
document.querySelectorAll('.glue-header').forEach(Header.attachTo);
