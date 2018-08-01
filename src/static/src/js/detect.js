/**
 * @fileoverview Initial feature detections that allow us to style the page
 * differently and prevent FOUC.
 */
goog.module('dmb.detect');


const glueApp = goog.require('glue.app');
const glueDetect = goog.require('glue.detect');
const glueFlexbox = goog.require('glue.detect.flexbox');

glueDetect.decorateDom(glueFlexbox);

glueApp.blacklist({
  // Set this to the highest level of IE you don't support.
  // Glue 16+ doesn't support IE 10 or lower.
  'ie': 10,
  'android': 4,
});
