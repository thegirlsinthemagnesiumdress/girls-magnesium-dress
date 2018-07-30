// In src/app.js
goog.module('dmb.app');

const glueApp = goog.require('glue.app');
const glueCommon = goog.require('glue.ng.common');
const glueZippy = goog.require('glue.ng.zippy');
const header = goog.require('glue.ng.ui.header');

/** @type {!angular.Module} */
const module = angular.module('dmb', [
  glueCommon.module.name, // Progressive enhancement/browser detections.
  glueZippy.module.name,
  'ngAnimate',
  header.module.name,
  'hercules_template_bundle'
]);

// Conditionally start the app if it's a supported browser.
glueApp.bootstrap(module.name);
exports = module;
