// In src/app.js
goog.module('dmb.app');

const glueApp = goog.require('glue.app');
const glueCommon = goog.require('glue.ng.common');
const glueZippy = goog.require('glue.ng.zippy');
const header = goog.require('glue.ng.ui.header');
const smoothScroll = goog.require('glue.ng.smoothScroll');
const tabby = goog.require('glue.ng.tabby');
const tableSort = goog.require('glue.ng.tableSort');

const focusControl = goog.require('dmb.components.focusControl');
const headerFix = goog.require('dmb.components.headerFix');
const registration = goog.require('dmb.components.registration');
const scrollHandler = goog.require('dmb.components.scroll');
const sidePanel = goog.require('dmb.components.sidePanel');
const report = goog.require('dmb.components.report');
const progressCircle = goog.require('dmb.components.progressCircle');
const dimensionTab = goog.require('dmb.components.dimensionTab');

/** @type {!angular.Module} */
const module = angular.module('dmb', [
  focusControl.module.name,
  glueCommon.module.name, // Progressive enhancement/browser detections.
  glueZippy.module.name,
  'ngAnimate',
  header.module.name,
  headerFix.module.name,
  registration.module.name,
  scrollHandler.module.name,
  sidePanel.module.name,
  report.module.name,
  progressCircle.module.name,
  dimensionTab.module.name,
  smoothScroll.module.name,
  tabby.module.name,
  tableSort.module.name,
  'hercules_template_bundle',
  'ngclipboard',
]);

const csrfTokenElement = document.querySelector('[name="csrfmiddlewaretoken"]');
const csrfToken = csrfTokenElement ? csrfTokenElement.value : '';
module.constant('csrfToken', csrfToken);

// Conditionally start the app if it's a supported browser.
glueApp.bootstrap(module.name);
exports = module;
