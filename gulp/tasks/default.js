var path = require('path');
var runSequence = require('run-sequence');

var ENVIRONMENTS = require(path.resolve('gulp', 'environments'));


module.exports = function(gulp) {
  return function(callback) {
    process.env.GULP_ENV = ENVIRONMENTS.DEV;

    return runSequence(
      'clean',
      'symlink:dev',
      [
        'sass',
        'compile-js'
      ],
      [
        'lint-sass',
        // 'lint-js'
      ],
      'watch'
    );
  };
};
