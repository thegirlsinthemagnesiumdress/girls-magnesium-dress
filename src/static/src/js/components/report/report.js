import * as directive from './report.directive';
import * as service from './report.service';
import {dmbLevelsFactory} from './report-factories';


/** @const {string} */
const MODULE_NAME = 'report';


/**
 * @type {!angular.Module}
 */
export const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);
module.service(service.SERVICE_NAME, service.main);

module.factory('dmbLevelsFactory', ['tenantConf', dmbLevelsFactory]);

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
