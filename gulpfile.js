var gulp = require('gulp');
var argv = require('yargs').argv;
var babel = require('gulp-babel');
var sass = require('gulp-sass');
var rename = require('gulp-rename');
var replace = require('gulp-replace');
var livereload = require('gulp-livereload');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var browserify = require('browserify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');
var browserifyHandlebars = require('browserify-handlebars');

var STATIC_DIR = './src/static';
var DEV_STATIC_DIR = STATIC_DIR + '/dev/';
var DIST_DIR = STATIC_DIR + '/dist/';
var TEMPLATES_DIR =  './src/public/templates/';

var SASS_INCLUDES = [
  './src/static/src/scss',

  // Libraries installed with npm
  'node_modules/sass-mq/',
  'node_modules/flexboxgrid-sass/',
  'node_modules/fullpage.js/dist',
  'node_modules/slick-carousel/slick',
];

var ADMIN_STATIC = [
  './src/sitepackages/django/contrib/admin/static/admin/**/*.css',
  './src/sitepackages/django/contrib/admin/static/admin/**/*.js',
  './src/sitepackages/django/contrib/admin/static/admin/**/*.woff'
];

var JASMINE_STATIC = [
  './node_modules/jasmine-core/**/*.js',
  './node_modules/jasmine-core/**/*.css'
];

var DEBUG_TOOLBAR = [
  './src/sitepackages/debug_toolbar/static/debug_toolbar/**/*.css',
  './src/sitepackages/debug_toolbar/static/debug_toolbar/**/*.js'
];

gulp.task('jasmine', function() {
  var outputDir = DIST_DIR;
  if(argv.assets_debug) {
    outputDir = DEV_STATIC_DIR;
  }

  gulp.src(JASMINE_STATIC)
  .pipe(gulp.dest(outputDir + "/jasmine/"));
});

gulp.task('adminstatic', function() {
  var outputDir = DIST_DIR;
  if(argv.assets_debug) {
    outputDir = DEV_STATIC_DIR;
  }

  gulp.src(ADMIN_STATIC)
  .pipe(gulp.dest(outputDir + "/admin/"));
});

gulp.task('toolbarstatic', function() {
  if(argv.assets_debug) {
    var outputDir = DEV_STATIC_DIR;
    gulp.src(DEBUG_TOOLBAR)
    .pipe(gulp.dest(outputDir + "/debug_toolbar/"));
  }
});

gulp.task('js', function() {
  var babelOptions = { presets: ['es2015'] };

  var outputDir = DIST_DIR + 'js/';
  if(argv.assets_debug) {
    outputDir = DEV_STATIC_DIR + 'js/';
    babelOptions.compact = false;
  } else {
    babelOptions.minified = true;
    babelOptions.comments = false;
  }

  console.log('Generating JS files at: ' + outputDir);


  var bundles = [
    // ['./src/core/static/js/index.js', 'common.js'],
    // ['./src/public/static/js/index.js', 'public.js']
    ['./src/static/src/js/index.js', 'main.js']
  ];

  for(var i = 0; i < bundles.length; ++i) {
    var glob = bundles[i][0];
    var dest = bundles[i][1];

    browserify({
      shim: {
        'promise': {
          path: '/node_modules/promise-polyfill/promise.js',
          exports: 'Promise'
        },
        'url-search-params': {
          path: '/node_modules/url-search-params/build/url-search-params.js',
          exports: 'URLSearchParams'
        },
        'whatwg-fetch': {
          path: '/node_modules/whatwg-fetch/fetch.js',
          exports: 'fetch',
          depends: {
            promise: 'promise'
          }
        }
      },
      entries: glob,
      debug: argv.assets_debug
    })
      // .transform(browserifyHandlebars) // We don't need for now.
      .transform(babelify, {
        presets:['es2015'],
        plugins: [
          'transform-custom-element-classes',
        ],
      })
      .bundle()
      .on('error', function(err){
        console.log(err.stack);
      })
      .pipe(source(dest))
      .pipe(replace("{{STATIC_URL}}", argv.static_url))
      .pipe(gulp.dest(outputDir));
  }
});

const jsLibs = [
  'node_modules/clipboard/dist/clipboard.js',
  'node_modules/@webcomponents/custom-elements/custom-elements.min.js'
]

gulp.task('js-libs', function() {

  var outputDir = DIST_DIR + 'js/';
  if(argv.assets_debug) {
    outputDir = DEV_STATIC_DIR + 'js/';
  } else {

  }

  return gulp.src(jsLibs)
    .pipe(concat('lib.js'))
    .pipe(gulp.dest(outputDir));

});

gulp.task('css', function() {
  var sassOptions = { includePaths: SASS_INCLUDES };
  var outputDir = DIST_DIR + 'css/';
  if (argv.assets_debug) {
    outputDir = DEV_STATIC_DIR + 'css/';
    sassOptions.sourceMapEmbed = true;
    sassOptions.outputStyle = 'expanded';
  } else {
    sassOptions.outputStyle = 'compressed';
  }

  console.log('Generating CSS files at: ' + outputDir);

  var bundles = [
    ['./src/static/src/scss/main.scss', 'main.css'],
    // ['./src/core/static/scss/survey.scss', 'survey.css'],
    // ['./src/public/static/scss/main.scss', 'public.css'],

  ];

  for(var i = 0; i < bundles.length; ++i) {
    var input = bundles[i][0];
    var dest = bundles[i][1];

    gulp.src(input)
    .pipe(sass(sassOptions).on('error', sass.logError))
    .pipe(rename(dest))
    .pipe(autoprefixer())
    .pipe(replace("{{STATIC_URL}}", argv.static_url))
    .pipe(gulp.dest(outputDir));
  }
});

gulp.task('fonts', function() {
  var outputDir = DIST_DIR + 'fonts/';
  if(argv.assets_debug) {
    outputDir = DEV_STATIC_DIR + 'fonts/';
  }

  gulp.src([
    './src/static/src/fonts/**/*.{otf,ttf,svg,woff,eot}'
  ]).pipe(gulp.dest(outputDir));
});

gulp.task('images', function() {
  var outputDir = DIST_DIR + 'img/';
  if(argv.assets_debug) {
    outputDir = DEV_STATIC_DIR + 'img/';
  }

  gulp.src([
    './src/static/src/img/**/*.{jpg,jpeg,png,svg,ico}',
  ]).pipe(gulp.dest(outputDir));
});

gulp.task('watch', function() {
  livereload.listen(); // Start the livereload server

  gulp.watch([
    './src/static/src/js/**/*.js',
  ], ['js']);

  gulp.watch([
    './src/static/src/scss/**/*.scss',
  ], ['css']);

  gulp.watch([
    './src/static/src/img/**/*.{jpg,jpeg,png,svg,ico}',
  ], ['images']);

  // Watch for changes to the dev folder and trigger livereload if necessary
  gulp.watch([
    DEV_STATIC_DIR + '/**/*.js',
    DEV_STATIC_DIR + '/**/*.css'
  ], function(event) {
    livereload.changed(event.path);
  });

  // gulp.watch([
  //   TEMPLATES_DIR + '/**/*.html'
  // ], function(event) {
  //   livereload.changed(event.path);
  // });
});

gulp.task('default', ['build', 'watch']);
gulp.task('build', ['adminstatic', 'toolbarstatic', 'js', 'js-libs', 'css', 'fonts', 'images', 'jasmine']);
