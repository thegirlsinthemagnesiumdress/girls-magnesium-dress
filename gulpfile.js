

const sass = require('gulp-sass');

const gulp = require('gulp');
const path = require('path');
const hercules = require('glue').gulp.hercules;
var sourcemaps = require('gulp-sourcemaps');
var sassLint = require('sass-lint');
var eslint = require('gulp-eslint');
var del = require('del');
const templateCache = require('gulp-angular-templatecache');
const autoprefixer = require('gulp-autoprefixer');
const rename = require('gulp-rename');
const notify = require('gulp-notify');
const livereload = require('gulp-livereload');
const gap = require('gulp-append-prepend');



var STATIC_DIR = './src/static';
var DEV_STATIC_DIR = STATIC_DIR + '/dev/';
var DIST_DIR = STATIC_DIR + '/dist/';
const TEMPLATE_SRC = [
  'node_modules/glue/hercules/lib/components/**/*.html',
  '!node_modules/glue/hercules/lib/components/**/*_test.html',
];

gulp.task('js-dev', function() {
  return gulp.src(path.join(STATIC_DIR, '/**/*.js'))
      .pipe(hercules.js.dev())
      .pipe(gulp.dest(path.join(DEV_STATIC_DIR, 'js')))
      .pipe(livereload());
});

gulp.task('js', function() {
  return gulp.src(path.join(STATIC_DIR, '/**/*.js'))
      .pipe(hercules.js.prod({
        entry_point: 'dmb.app',
      }))
      .pipe(gap.prependFile(path.join(DEV_STATIC_DIR, 'js')))
      .pipe(gulp.dest(path.join(DIST_DIR, 'js')));
});

gulp.task('js-detect', function() {
  return gulp.src(path.join(STATIC_DIR, '/**/*.js'))
      // Note that entry_point matches the namespace defined in detect.js
      .pipe(hercules.js.prod({entry_point: 'dmb.detect'}))
      .pipe(rename('detect.min.js'))
      .pipe(gulp.dest(path.join(DIST_DIR, 'js')));
});

gulp.task('js-templates', function() {
  return gulp.src(TEMPLATE_SRC)
    .pipe(templateCache({
        module: 'hercules_template_bundle',
        standalone: true,
        transformUrl: (url) => {
          // TODO: You may have to modify the url here depending
          // on your setup. This is to make the path look more like
          // the path glue directives are looking for.
          return `/glue/${url}`;
        }
      }
    ))
    .pipe(gulp.dest(path.join(DEV_STATIC_DIR, 'js')));
});

// gulp.task('copy-hercules-assets', function() {
//   return gulp.src('node_modules/glue/hercules/lib/assets/icons/svgs.inc.html')
//     .pipe(rename('_hercules-icons.html'))
//     .pipe(gulp.dest(PATHS.templates));
// });


/** @const {Object<*>} */
var SASS_CONFIG = {
  outputStyle: 'compressed',
  includePaths: [
    'node_modules/glue'
  ]
};

gulp.task('clean', function() {
  return del([
    path.join(DEV_STATIC_DIR, 'js', '**/*'),
    path.join(DEV_STATIC_DIR, 'scss', '**/*'),
    path.join(DIST_DIR, 'js', '**/*'),
    path.join(DIST_DIR, 'scss', '**/*'),
  ]);
});


gulp.task('sass-dev', function() {
  // Fill out the line below with the path to your main Sass file.
  return gulp.src(path.join(STATIC_DIR, '/**/*.scss'))
      .pipe(sass(SASS_CONFIG).on('error', sass.logError))
      .pipe(sourcemaps.init())
      .pipe(autoprefixer({
        browsers: ['last 2 versions'],
        cascade: false
      }))
      .pipe(sourcemaps.write())
      .pipe(rename('main.min.css'))
      .pipe(gulp.dest(path.join(DEV_STATIC_DIR, 'css')))
      .pipe(livereload())
      .pipe(notify({
        message: 'Sass compilation complete.'
      }));
});

gulp.task('sass', function() {
  // Fill out the line below with the path to your main Sass file.
  return gulp.src(path.join(STATIC_DIR, '/**/*.scss'))
      .pipe(sass(SASS_CONFIG).on('error', sass.logError))
      .pipe(autoprefixer({
        browsers: ['last 2 versions'],
        cascade: false
      }))
      .pipe(rename('main.min.css'))
      .pipe(gulp.dest(path.join(DIST_DIR, 'css')))
      .pipe(notify({
        message: 'Sass compilation complete.'
      }));
});

gulp.task('js-lint', function() {
  return gulp.src([
    path.join(STATIC_DIR, '/**/*.js'),
  ])
    .pipe(eslint())
    .pipe(eslint.format());
});

gulp.task('sass-lint', function() {
  return gulp.src(path.join(STATIC_DIR, '/**/*.scss'))
    .pipe(sassLint())
    .pipe(sassLint.format());
});

gulp.task('watch', function() {
  livereload.listen();
  gulp.watch(path.join(STATIC_DIR, '/**/*.js'), gulp.parallel(
    'js-lint',
    'js-dev'
  ));

  gulp.watch(path.join(STATIC_DIR, '/**/*.scss'), gulp.parallel(
    'sass-lint',
    'sass-dev'
  ));
});

gulp.task('lint', gulp.parallel(
  'js-lint',
  'sass-lint'
));

gulp.task('build', gulp.series(
  'clean',
  'js-detect',
  'js-templates',
  'js',
  'sass'
));

gulp.task('default', gulp.series(
  'clean',
  gulp.parallel(
    // 'js-lint',
    // 'sass-lint',
    'js-templates',
    'js-dev',
    'sass-dev'
  ),
  'watch'
));
