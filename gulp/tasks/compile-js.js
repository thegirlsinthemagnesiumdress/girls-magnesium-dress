const sourcemaps = require('gulp-sourcemaps');
const browserify = require('browserify');
const PATHS = require('../paths');
const path = require('path');
const buffer = require('vinyl-buffer');
const source = require('vinyl-source-stream');
const gulpif = require('gulp-if');
const onError = require('../utils/on-error');
const ENVIRONMENTS = require(path.resolve('gulp', 'environments'));
var uglify = require('gulp-uglify')

module.exports = function js(gulp) {
  return function(callback) {
    const dev = process.env.GULP_ENV === ENVIRONMENTS.DEV;

    const b = browserify('source/js/main.js', {
      debug: true,
    })
      .transform('babelify');
    console.log(dev)
    return b.bundle()
      // .on('error', onError)
      .pipe(source('site.min.js'))
      .pipe(buffer())
      .pipe(gulpif(dev, sourcemaps.init({ loadMaps: true })))
      .pipe(gulpif(!dev, uglify({
        compress: {
          drop_console: true,
        },
      })))
      // .on('error', onError)
      .pipe(gulpif(dev, sourcemaps.write('./')))
      .pipe(gulp.dest(PATHS.DIST.JS));
  };
};
