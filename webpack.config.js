const ClosurePlugin = require('closure-webpack-plugin');
const {devFlags} = require('@google/glue/gulp'); // Get default compiler flags from Glue gulp plugin

// Dev mode
module.exports = {
  devtool: 'inline-source-map',
  entry: {
    main: './src/static/src/js/app',
    detect: './src/static/src/js/detect',
    survey: './src/static/src/js/survey',
  },
  output: {
    filename: '[name].min.js',
  },
  mode: 'none',
  plugins: [
    new ClosurePlugin.LibraryPlugin(
      {
        closureLibraryBase: require.resolve(
          'google-closure-library/closure/goog/base'
        ),
        deps: [
          require.resolve('google-closure-library/closure/goog/deps'),
          './src/static/dev/js/deps.js',
        ],
      },
      devFlags
    ),
  ],
};
