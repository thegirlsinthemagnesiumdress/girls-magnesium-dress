goog.module.declareNamespace('dmb.components.report');

import * as directive from './report.directive';
import * as service from './report.service';


/** @const {string} */
const MODULE_NAME = 'report';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
module.service(service.SERVICE_NAME, service.main);

module.factory('dmbLevelsFactory', ['tenantConf', (tenantConf) => {
  // Factory that takes a non-integer number and an optional map of strings
  // and returns the current level value (minimum number in range),
  // the next level value (minimum number in range)
  // and the value corresponding to the nearest key in the map
  return (score, sourceMap) => {
    if (!angular.isDefined(score)) {
      return '';
    }

    if (!sourceMap) {
      // Default to `tenantConf.levels` if no map given as this is most common use case
      sourceMap = tenantConf.levels;
    }

    // Get source keys which are the levels
    const levelKeys = Object.keys(sourceMap).sort();
    for (const [index, levelMinimum] of levelKeys.entries()) {
      let nextLevelMinimum = levelKeys[index + 1];
      if (score >= levelMinimum && (score < nextLevelMinimum || !nextLevelMinimum)) {
        nextLevelMinimum = nextLevelMinimum || levelMinimum;
        return {
          'current': {
            'value': levelMinimum,
            'mapValue': sourceMap[levelMinimum],
          },
          'next': {
            'value': nextLevelMinimum,
            'mapValue': sourceMap[nextLevelMinimum],
          },
        };
      }
    }
  };
}]);

module.factory('resultInTopLevel', ['tenantConf', (tenantConf) => {
  const levelsArray = Object.keys(tenantConf.levels).sort();

  return (value) => {
    if (!angular.isDefined(value)) {
      return '';
    }

    return value >= levelsArray[levelsArray.length - 1];
  };
}]);


module.factory('floorDmbFactory', ['tenantConf', (tenantConf) => {
  const levelsTotal = tenantConf.levelsTotal;
  return (dmb) => {
    if (!angular.isDefined(dmb)) {
      return null;
    }
    return Math.min(Math.floor(dmb), (levelsTotal - 1));
  };
}]);

module.filter('dmbLevelText', ['floorDmbFactory', 'tenantConf', (floorDmbFactory, tenantConf)=> {
  return (dmb) => {
    return angular.isDefined(dmb) ? tenantConf.levels[floorDmbFactory(dmb)] : '';
  };
}]);

module.filter('underscoreToHyphen', () => {
  return (stringToConvert) => {
    return angular.isDefined(stringToConvert) ? stringToConvert.replace(/_/g, '-') : '';
  };
});
