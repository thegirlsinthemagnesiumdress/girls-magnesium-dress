var path = require('path');
var watch = require('gulp-watch');
var runSequence = require('run-sequence');

var PATHS = require(path.resolve('gulp', 'paths'));


module.exports = function(gulp) {
  return function() {
    watch(PATHS.CSS_SOURCES, function() {
      runSequence(
        'sass'
        //, 'lint-sass'
      );
    });
    watch(PATHS.JS_SOURCES, function() {
      runSequence('compile-js'
      // , 'lint-js'
    );
    });
  };
};
