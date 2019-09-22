var imagemin = require('gulp-imagemin');
var path = require('path');

var PATHS = require(path.resolve('gulp', 'paths'));


module.exports = function(gulp) {
  return {
    build: function() {
      gulp.src(PATHS.BUILD.IMG + '*')
        .pipe(imagemin())
        .pipe(gulp.dest(PATHS.BUILD.IMG));
    },

    dev: function() {
      gulp.src(PATHS.SRC.IMG + '*')
        .pipe(imagemin())
        .pipe(gulp.dest(PATHS.SRC.IMG));
    }
  };
};
