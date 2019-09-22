var path = require('path');
var runSequence = require('run-sequence');


module.exports = function(gulp) {
  return function(callback) {
    runSequence(
      'clean',
      'symlink:dev',
      'lint-js',
      'karma',
      callback
    );
  };
};
