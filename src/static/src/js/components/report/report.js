goog.module('dmb.components.report');

const directive = goog.require('dmb.components.report.directive');
const service = goog.require('dmb.components.report.service');


/** @const {string} */
const MODULE_NAME = 'report';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
module.service(service.SERVICE_NAME, service.main);

module.factory('floorDmbFactory', ['tenantConf', (tenantConf) => {
  const levelsTotal = tenantConf.levelsTotal;
  return (dmb) =>
    (angular.isDefined(dmb) ? Math.min(Math.floor(dmb), (levelsTotal - 1)) : null);
}]);

module.filter('dmbLevelText', ['floorDmbFactory', 'tenantConf', (floorDmbFactory, tenantConf)=> {
  return (dmb) => {
    return angular.isDefined(dmb) ? tenantConf.levels[floorDmbFactory(dmb)] : '';
  };
}]);

module.filter('dmbRangeText', ['floorDmbFactory', 'tenantConf', (floorDmbFactory, tenantConf) => {
  return (dmb) => {
    if (!angular.isDefined(dmb)) {
      return '';
    }

    const floor = floorDmbFactory(dmb);
    const ceil = Math.min(Math.ceil(dmb), tenantConf.levelsTotal);
    return `${floor}-${ceil}`;
  };
}]);

module.filter('dmbPercentageNumber', ['tenantConf', (tenantConf)=> {
  const levelsTotal = tenantConf.levelsTotal;
  return (dmb) => {
    return angular.isDefined(dmb) ? dmb / levelsTotal * 100 : 0;
  };
}]);


/**
 * Report angular module.
 * @type {!angular.Module}
 */
exports.module = module;


