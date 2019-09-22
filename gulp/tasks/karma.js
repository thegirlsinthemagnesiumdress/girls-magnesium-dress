var path = require('path');
var Server = require('karma').Server;


module.exports = function(gulp) {
  return function(done) {
    new Server({
      configFile: path.resolve('karma.conf.js'),
      singleRun: true
    }, done).start();
  };
};
