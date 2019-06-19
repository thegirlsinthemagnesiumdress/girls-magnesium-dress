/**
 * @fileoverview Initial feature detections that allow us to style the page
 * differently and prevent FOUC.
 */
goog.module('dmb.detect');


import * as glueApp from '@google/glue/lib/app/app';
import * as glueDetect from '@google/glue/lib/detect/detect';
import * as glueFlexbox from '@google/glue/lib/detect/flexbox/flexbox';

glueDetect.decorateDom(glueFlexbox.feature);

glueApp.blacklist({
  // Set this to the highest level of IE you don't support.
  // Glue 16+ doesn't support IE 10 or lower.
  'ie': 10,
  'android': 4,
});
