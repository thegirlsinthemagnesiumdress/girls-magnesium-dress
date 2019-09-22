var gulp = require('gulp');
var path = require('path');

var PATHS = require(path.resolve('gulp', 'paths'));


module.exports = function(name) {
  var p = path.join(PATHS.TASKS, name);
  return require(p)(gulp);
};
