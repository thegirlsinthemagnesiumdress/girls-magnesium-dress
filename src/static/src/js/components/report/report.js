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

module.factory('floorDmbFactory', () => {
  return (dmb) =>
    (angular.isDefined(dmb) ? Math.min(Math.floor(dmb), 3) : null);
});

module.filter('dmbLevelText', ['floorDmbFactory', (floorDmbFactory)=> {
  return (dmb) => {
    const levels = {
      0: 'Nascent',
      1: 'Emerging',
      2: 'Connected',
      3: 'Multi-moment',
    };

    return angular.isDefined(dmb) ? levels[floorDmbFactory(dmb)] : '';
  };
}]);

module.filter('dmbRangeText', ['floorDmbFactory', (floorDmbFactory) => {
  return (dmb) => {
    if (!angular.isDefined(dmb)) {
      return '';
    }

    const floor = floorDmbFactory(dmb);
    const ceil = Math.min(Math.ceil(dmb), 4);
    return `${floor}-${ceil}`;
  };
}]);

module.filter('dmbPercentageNumber', ()=> {
  return (dmb) => {
    return angular.isDefined(dmb) ? dmb / 4 * 100 : 0;
  };
});


/**
 * Report angular module.
 * @type {!angular.Module}
 */
exports.module = module;


