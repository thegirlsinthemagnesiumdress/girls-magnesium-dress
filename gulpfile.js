var gulp = require('gulp');
var path = require('path');

var getTask = require(path.resolve('gulp', 'utils', 'get-task'));


// Initialise gulp tasks.
gulp.task('clean', getTask('clean'));
gulp.task('closure-deps', getTask('closure-deps'));
gulp.task('compile-js', getTask('compile-js'));
gulp.task('imagemin:dev', getTask('imagemin').dev);
gulp.task('imagemin:build', getTask('imagemin').build);
gulp.task('karma', getTask('karma'));
gulp.task('lint-js', getTask('lint-js'));
gulp.task('lint-sass', getTask('lint-sass'));
gulp.task('sass', getTask('sass'));
gulp.task('symlink:dev', getTask('symlink').dev);
gulp.task('watch', getTask('watch'));

// Main tasks.
gulp.task('build', getTask('build'));
gulp.task('default', getTask('default'));
gulp.task('predeploy', getTask('predeploy'));
gulp.task('test', getTask('test'));
