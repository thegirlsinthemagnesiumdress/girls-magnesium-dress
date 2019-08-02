goog.module.declareNamespace('dmb.components.sidePanel');

import * as directive from './side-panel.directive';
import * as triggerDirective from './side-panel-trigger.directive';
import * as service from './side-panel.service';


/** @const {string} */
const MODULE_NAME = 'sidePanel';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
module.directive(triggerDirective.DIRECTIVE_NAME, triggerDirective.main);
module.service(service.SERVICE_NAME, service.main);
