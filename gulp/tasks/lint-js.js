var eslint = require('gulp-eslint');
var path = require('path');

var PATHS = require(path.resolve('gulp', 'paths'));

module.exports = function(gulp) {
  return function(callback) {
    var appJs = PATHS.JS_SOURCES;
    var thirdPartyJs = [`!${path.join(PATHS.SRC.JS, 'modernizr.custom.js')}`];

    return gulp.src(appJs.concat(thirdPartyJs))
      .pipe(eslint())
      .pipe(eslint.format());
  };
};
