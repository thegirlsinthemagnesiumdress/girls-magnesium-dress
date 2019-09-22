var path = require('path');


module.exports = PATHS = {
  TASKS: path.resolve('gulp', 'tasks'),
  NPM: path.resolve('node_modules'),
  BUILD: {
    ROOT: path.resolve('build'),
    IMG: path.resolve('build', 'static', 'images')
  },
  DIST: {
    ROOT: path.resolve('dist'),
    CSS: path.resolve('dist', 'css'),
    JS: path.resolve('dist', 'js'),
  },
  SRC: {
    ROOT: path.resolve('source'),
    SCSS: path.resolve('source', 'sass'),
    IMG: path.resolve('source', 'images'),
    JS: path.resolve('source', 'js')
  }
};

PATHS.CSS_SOURCES = [
  path.join(PATHS.SRC.SCSS, '**', '*.scss')
];

PATHS.JS_SOURCES = [
  path.join(PATHS.SRC.JS, '**', '*.js'),
  path.join('!' + PATHS.SRC.JS, 'deps.js'),
  path.join('!' + PATHS.SRC.JS, '*.spec.js'),
  path.join('!' + PATHS.SRC.JS, 'externs', '**', '*.js')
];
