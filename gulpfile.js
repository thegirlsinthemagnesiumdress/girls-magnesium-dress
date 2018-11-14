

const sass = require('gulp-sass');

const gulp = require('gulp');
const path = require('path');
const hercules = require('glue').gulp.hercules;
const sourcemaps = require('gulp-sourcemaps');
const sassLint = require('gulp-sass-lint');
const eslint = require('gulp-eslint');
const del = require('del');
const templateCache = require('gulp-angular-templatecache');
const autoprefixer = require('gulp-autoprefixer');
const rename = require('gulp-rename');
const notify = require('gulp-notify');
const livereload = require('gulp-livereload');
const gap = require('gulp-append-prepend');
const rev = require('gulp-rev');


const STATIC_DIR = './src/static';
const SRC_STATIC_DIR = './src/static/src';
const DEV_STATIC_DIR = STATIC_DIR + '/dev/';
const DIST_DIR = STATIC_DIR + '/dist/';

const PATHS = {
  src: {
    js: path.join(SRC_STATIC_DIR, 'js'),
    scss: path.join(SRC_STATIC_DIR, 'scss'),
  },
  dev: {
    js: path.join(DEV_STATIC_DIR, 'js'),
    scss: path.join(DEV_STATIC_DIR, 'css'),
  },
  dist: {
    js: path.join(DIST_DIR, 'js'),
    scss: path.join(DIST_DIR, 'css'),
  },
  manifest: path.join('src', 'rev-manifest.json'),
};


const TEMPLATE_SRC = [
  'node_modules/glue/hercules/lib/components/**/*.html',
  '!node_modules/glue/hercules/lib/components/**/*_test.html',
];

gulp.task('js-dev', function() {
  return gulp.src(`${PATHS.src.js}/**/*.js`)
      .pipe(hercules.js.dev())
      .pipe(gulp.dest(PATHS.dev.js))
      .pipe(livereload());
});

gulp.task('js', function() {
  return gulp.src(`${PATHS.src.js}/**/*.js`)
      .pipe(hercules.js.prod({
        entry_point: 'dmb.app',
        hide_warnings_for: 'node_modules/glue/',
        js_output_file: 'js/main.min.js',
      }))
      .pipe(gap.prependFile(path.join(PATHS.dev.js, 'templates.js')))
      .pipe(gap.prependFile('node_modules/ngclipboard/dist/ngclipboard.min.js'))
      .pipe(gap.prependFile('node_modules/clipboard/dist/clipboard.min.js'))
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev())
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev.manifest(PATHS.manifest, {
        merge: true,
      }))
      .pipe(gulp.dest('./'));
});

gulp.task('js-detect', function() {
  return gulp.src(`${PATHS.src.js}/**/*.js`)
      // Note that entry_point matches the namespace defined in detect.js
      .pipe(hercules.js.prod({
        entry_point: 'dmb.detect',
        js_output_file: 'js/detect.min.js',

      }))
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev())
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev.manifest(PATHS.manifest, {
        merge: true,
      }))
      .pipe(gulp.dest('./'));
});

gulp.task('js-survey', function() {
  return gulp.src(`${PATHS.src.js}/**/*.js`)
      // Note that entry_point matches the namespace defined in survey.js
      .pipe(hercules.js.prod({
        entry_point: 'dmb.survey',
        hide_warnings_for: 'node_modules/glue/',
        js_output_file: 'js/survey.min.js',
      }))
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev())
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev.manifest(PATHS.manifest, {
        merge: true,
      }))
      .pipe(gulp.dest('./'));
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
    .pipe(gulp.dest(PATHS.dev.js));
});

/** @const {Object<*>} */
const SASS_CONFIG = {
  outputStyle: 'compressed',
  includePaths: [
    'node_modules/glue'
  ]
};

const AUTOPREFIXER_CONFIG = {
  browsers: ['last 2 versions'],
  cascade: false,
};

gulp.task('clean-dev', function() {
  return del([
    path.join(PATHS.dev.js, '**/*'),
    path.join(PATHS.dev.scss, '**/*'),
  ]);
});

gulp.task('clean-dist', function() {
  return del([
    path.join(PATHS.dist.js, '**/*'),
    path.join(PATHS.dist.scss, '**/*'),
    PATHS.manifest,
  ]);
});


gulp.task('sass-dev', function() {
  // Fill out the line below with the path to your main Sass file.
  return gulp.src(`${PATHS.src.scss}/**/*.scss`)
      .pipe(sourcemaps.init())
      .pipe(sass(SASS_CONFIG).on('error', sass.logError))
      .pipe(autoprefixer(AUTOPREFIXER_CONFIG))
      .pipe(sourcemaps.write('./'))
      .pipe(gulp.dest(PATHS.dev.scss))
      .pipe(livereload())
      .pipe(notify({
        message: 'Sass compilation complete.'
      }));
});

gulp.task('sass', function() {
  // Fill out the line below with the path to your main Sass file.
  return gulp.src(`${PATHS.src.scss}/**/*.scss`)
      .pipe(sass(SASS_CONFIG).on('error', sass.logError))
      .pipe(autoprefixer(AUTOPREFIXER_CONFIG))
      .pipe(gap.prependFile('node_modules/angular/angular-csp.css'))
      .pipe(rename({
        dirname: 'css',
      }))
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev())
      .pipe(gulp.dest(DIST_DIR))
      .pipe(rev.manifest(PATHS.manifest, {
        merge: true,
      }))
      .pipe(gulp.dest('./'))
      .pipe(notify({
        message: 'Sass compilation complete.',
      }));
});

gulp.task('js-lint', function() {
  return gulp.src([
    `${PATHS.src.js}/**/*.js`,
    `!${PATHS.src.js}/legacy/**/*.js`,
  ])
    .pipe(eslint())
    .pipe(eslint.format());
});

gulp.task('sass-lint', function() {
  return gulp.src([
    `${PATHS.src.scss}/**/*.scss`,
    `!${PATHS.src.scss}/legacy/**/*.scss`,
  ])
    .pipe(sassLint())
    .pipe(sassLint.format());
});


function copy(src, dest) {
  return gulp.src(src).pipe(gulp.dest(dest));
}

gulp.task('fonts-dev', function() {
  const outputDir = path.join(DEV_STATIC_DIR, 'fonts');
  const src = [
    `${SRC_STATIC_DIR}/fonts/**/*.{otf,ttf,svg,woff,eot}`,
  ];

  return copy(src, outputDir);
});

gulp.task('fonts-dist', function() {
  const outputDir = path.join(DIST_DIR, 'fonts');
  const src = [
    `${SRC_STATIC_DIR}/fonts/**/*.{otf,ttf,svg,woff,eot}`,
  ];

  return copy(src, outputDir);
});

gulp.task('images-dev', function() {
  const outputDir = path.join(DEV_STATIC_DIR, 'img');
  const src = [
    `${SRC_STATIC_DIR}/img/**/*.{jpg,png,svg,gif}`,
  ];

  return copy(src, outputDir);
});

gulp.task('images-dist', function() {
  const outputDir = path.join(DIST_DIR, 'img');
  const src = [
    `${SRC_STATIC_DIR}/img/**/*.{jpg,png,svg,gif}`,
  ];

  return copy(src, outputDir);
});

gulp.task('watch', function() {
  livereload.listen();
  gulp.watch(`${PATHS.src.js}/**/*.js`, gulp.parallel(
    'js-lint',
    'js-dev'
  ));

  gulp.watch(`${SRC_STATIC_DIR}/img/**/*.{jpg,png,svg,gif}`, gulp.parallel('images-dev'));
  gulp.watch(`${SRC_STATIC_DIR}/fonts/**/*.{otf,ttf,svg,woff,eot}`, gulp.parallel('fonts-dev'));

  gulp.watch(`${PATHS.src.scss}/**/*.scss`, gulp.parallel(
    'sass-lint',
    'sass-dev'
  ));
});

gulp.task('lint', gulp.parallel(
  'js-lint',
  'sass-lint'
));

gulp.task('build',
  gulp.parallel(
    gulp.series(
    'clean-dist',
    'js-templates',
    'js-detect',
    'js-survey',
    'js',
    'sass'
    ),
    'images-dist',
    'fonts-dist'
  )
);

gulp.task('default', gulp.series(
  'clean-dev',
  gulp.parallel(
    'js-lint',
    'sass-lint',
    'js-templates',
    'js-dev',
    'sass-dev',
    'fonts-dev',
    'images-dev'
  ),
  'watch'
));
