var path = require('path');
var runSequence = require('run-sequence');

var ENVIRONMENTS = require(path.resolve('gulp', 'environments'));


module.exports = function(gulp) {
  return function(callback) {
    process.env.GULP_ENV = ENVIRONMENTS.PROD;

    return runSequence(
      'clean',
      [
        'compile-js',
        'sass'
      ],
      callback
    );
  };
};
