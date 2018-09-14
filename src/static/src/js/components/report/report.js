goog.module('dmb.components.report');

const directive = goog.require('dmb.components.report.directive');


/** @const {string} */
const MODULE_NAME = 'report';


/**
 * @type {!angular.Module}
 */
const module = angular.module(MODULE_NAME, []);


module.directive(directive.DIRECTIVE_NAME, directive.main);

// /**
//  * Returns level string
//  * @param {*} dmb
//  */
// function dmbLevelNumberyText(dmb) {
//   return `${Math.floor(dmb)} - ${Math.ceil(dmb)}`;
// }

// /**
//  * Returns level string
//  * @param {*} dmb
//  */
// function dmbLevelText(dmb) {
//   const levels = {
//     0: 'Nascent',
//     1: 'Emerging',
//     2: 'Connected',
//     3: 'Multi-moment',
//   };

//   return levels[Math.floor(dmb)];
// }


// /**
//  * Returns level string
//  * @param {*} dmb
//  */
// function dmbProgressText(dmb) {
//   return `${dmb.toFixed(2)}/4.0`;
// }

module.filter('dmbLevelText', ()=> {
  return (dmb) => {
    const levels = {
      0: 'Nascent',
      1: 'Emerging',
      2: 'Connected',
      3: 'Multi-moment',
    };

    return angular.isDefined(dmb) ? levels[Math.floor(dmb)] : '';
  };
});

// module.filter('dmbProgressText', ()=> {
//   return (dmb) => {
//     return angular.isDefined(dmb) ? `${dmb.toFixed(2)}/4.0` : '';
//   };
// });

module.filter('dmbLevelNumberyText', ()=> {
  return (dmb) => {
    return angular.isDefined(dmb) ? `${Math.floor(dmb)} - ${Math.ceil(dmb)}` : '';
  };
});

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
