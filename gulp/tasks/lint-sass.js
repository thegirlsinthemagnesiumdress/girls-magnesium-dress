var path = require('path');
var sassLint = require('gulp-sass-lint');

var PATHS = require(path.resolve('gulp', 'paths'));


module.exports = function(gulp) {
  return function() {
    return gulp.src(PATHS.CSS_SOURCES)
      .pipe(sassLint({
        configFile: '.sass-lint.yml'
      }))
      .pipe(sassLint.format())
      .pipe(sassLint.failOnError());
  };
};
