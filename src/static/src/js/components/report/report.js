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

module.factory('dmbLevelsFactory', ['tenantConf', (tenantConf) => {
  // Factory that takes a non-integer number and an optional map of strings
  // and returns the current level value (minimum number in range),
  // the next level value (minimum number in range)
  // and the value corresponding to the nearest key in the map
  return (value, sourceMap) => {
    if (!angular.isDefined(value)) {
      return '';
    }

    if (!sourceMap) {
      // Default to `tenantConf.levels` if no map given
      sourceMap = tenantConf.levels;
    }

    const sourceKeys = Object.keys(sourceMap).sort();
    for (const [index, val] of sourceKeys.entries()) {
      // If last element
      if (index == sourceKeys.length - 1) {
        return {
          current: {
            value: val,
            mapValue: sourceMap[val],
          },
          next: {
            value: val,
            mapValue: sourceMap[val],
          },
        };
      } else if (value >= val && value < sourceKeys[index + 1]) {
        const nextLevel = sourceKeys[index + 1];
        // Including the return twice for early break when condition met
        return {
          current: {
            value: val,
            mapValue: sourceMap[val],
          },
          next: {
            value: nextLevel,
            mapValue: sourceMap[nextLevel],
          },
        };
      }
    }
  };
}]);

module.factory('resultInTopLevel', ['tenantConf', (tenantConf) => {
  return (value) => {
    if (!angular.isDefined(value)) {
      return '';
    }

    const levelsArray = Object.keys(tenantConf.levels).sort();
    return value >= levelsArray[levelsArray.length - 1];
  };
}]);


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

/**
 * Report angular module.
 * @type {!angular.Module}
 */
exports.module = module;


