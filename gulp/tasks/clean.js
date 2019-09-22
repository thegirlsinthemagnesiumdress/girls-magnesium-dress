var del = require('del');
var gulp = require('gulp');
var path = require('path');

var PATHS = require(path.resolve('gulp', 'paths'));


module.exports = function(gulp) {
  return function(callback) {
    del.sync(PATHS.DIST.ROOT);
    del.sync(path.resolve(PATHS.SRC.JS, 'deps.js'));
    del.sync(path.resolve(PATHS.SRC.JS, 'closure-library'));
    callback();
  };
};
