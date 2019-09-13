// eslint-disable-next-line no-unused-vars
import tenantConfiguration, {TenantConfiguration} from '../../tenants/tenantconf.class';

/**
 * Raw factory function for use with AngularjS
 * @param {TenantConfiguration} tenantConf Will be the AngularJS injected service of tenantConf
 * @return {function(number, Object=): Object}
 */
export function dmbLevelsFactory(tenantConf) {
  // Factory that takes a non-integer number and an optional map of strings
  // and returns the current level value (minimum number in range),
  // the next level value (minimum number in range)
  // and the value corresponding to the nearest key in the map
  return factoryFunction;
  /**
   * @param {number} score
   * @param {Object=} sourceMap
   * @return {Object}
   */
  function factoryFunction(score, sourceMap) {
    if (!angular.isDefined(score)) {
      return {};
    }

    if (!sourceMap) {
      if (tenantConf.levels === null) {
        return {};
      }
      // Default to `tenantConf.levels` if no map given as this is most common use case
      sourceMap = tenantConf.levels;
    }

    // Get source keys which are the levels
    const levelKeys = Object.keys(sourceMap).sort();
    for (const [index, levelMinimum] of levelKeys.entries()) {
      let nextLevelMinimum = levelKeys[+index + 1];
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
    // If we haven't hit a match, still return an Object
    return {};
  }
}

// Initialising with Vanilla tenantConf for Vanilla JS use
export const dmbLevels = dmbLevelsFactory(tenantConfiguration);
