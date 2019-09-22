var fs = require('fs');
var path = require('path');

var PATHS = require(path.resolve('gulp', 'paths'));


module.exports = function(gulp) {
  return {
    dev: function() {
      // Make a dist folder
      if (!fs.existsSync(PATHS.DIST.ROOT)) {
        fs.mkdirSync(PATHS.DIST.ROOT);
      }

    }
  };
};
