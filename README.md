# Grow + GAE Scaffold

Scaffold for building static sites using [Grow](https://grow.io) and deploying to [Google App Engine](https://cloud.google.com/appengine/).

We provide a foundation for HTML, [Google Closure](https://developers.google.com/closure/library/)-style JS, [Sass](http://sass-lang.com/)-driven CSS and testing stubs through [Karma](http://karma-runner.github.io/) with Google-approved linters and style configuration all automated using [Gulp](http://gulpjs.com/). We also bundle a ready-made `app.yaml` config file for easy deployment to [Google App Engine](https://cloud.google.com/appengine/).

This scaffold is self-contained within a virtual environment allowing you to maintain multiple, concurrent projects with differing versions/dependencies.

## Getting started

### Assumptions

 - [Node.js](https://nodejs.org/en/) is installed.
 - [Gulp](http://gulpjs.com/) is installed.
 - [Karma](https://karma-runner.github.io/) is installed (to run tests).
 - [Java JRE](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) is installed (required for Closure Linter).

### Setup

Shallow clone the git repository:
```
git clone --depth 1 git@github.com:potatolondon/grow-gae-scaffold.git
```

Create a new virtualenv

```
mkvirtualenv [your-project-name]
```

Install the required dependencies:

```
./scripts/install.sh
```

Start a new git history and rename instances of `grow-gae-scaffold` and `scaffold` in the project:

```
./scripts/rename_scaffold.sh [your-project-name]
```

Stage changes and update the git repository remote then push:

```
git add .
git remote set-url origin [URL]
git push origin master
```

## Development

Run Gulp and Grow:

```
gulp
grow run
```

Preview the site by navigating to http://localhost:8080/ in your browser to get started.

## Tests

Tests are run on Karma using the Jasmine framework. Run the test suite with:

```
gulp test
```

Each JS component file should be paired with a test spec. Tests files should end with `.spec.js` and sit alongside their relevant source file in the directory structure.

## Preview

Run the following to build and preview the site:

```
source ./scripts/preview.sh
```

This will run the relevant `gulp` tasks to build the static files as well as `grow build` to build the site and then run the GAE dev server so you can preview the built site from the `build/` directory.

## Deploying

Run this command to deploy the site:

On dev brach
```
gulp build
grow deploy
```

than merge to master and push.


## Updating Grow and other dependencies

Once you have kicked your project off, customised it to your needs and severed ties to the scaffoled repository, you must take responsibility of updating Grow and other dependencies. Keep an eye on the [Grow GAE Scaffold](https://github.com/potatolondon/grow-gae-scaffold) repo for any changes to the core scaffold that you may find useful.

## Linting

The scaffold comes with tasks for linting both JS and the Sass files. These are:

```
gulp lint-js
gulp lint-sass
```

They are both run automatically when you edit any files in `source/js/` or `source/sass/` files respectively.

JS linting is handled by the [Closure Linter](https://developers.google.com/closure/utilities/) (`gjslint`) and [`gulp-gjslint`](https://www.npmjs.com/package/gulp-gjslint) to conform to Google Closure Library's style rules. There is a config file in the root of the project to set these rules to `--strict`.

Sass linting is handled by [Sass Lint](https://github.com/sasstools/sass-lint) and [`gulp-sass-lint`](https://www.npmjs.com/package/gulp-sass-lint). Linting rules are defined in the `.sass-lint.yml` file in the root of the project according to [Google's CSS style guidelines](https://google.github.io/styleguide/htmlcssguide.xml).


## CSP

The routes in app.yaml have strictly-defined [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/Security/CSP) headers that allow for Google Analytics and Google Fonts integration. These can be modified to open up further integrations.

Inline scripts are disabled by default and require you to add a SHA256 representation of the script to the CSP configuration.
