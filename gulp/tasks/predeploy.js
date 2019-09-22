var runSequence = require('run-sequence');


module.exports = function(gulp) {
  return function(callback) {
    return runSequence(
      'imagemin:build'
    );
  };
};
