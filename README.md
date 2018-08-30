# Talent Revolution

# Prerequisites

1. You need to have a local SSH key linked to a GitHub account, which is a member of the [PotatoLondon organization](https://github.com/potatolondon)

# Installation

1. Clone the repository (you might have already done that!)
1. Run `./bin/install_deps --with-appengine`. If you get errors try using a virtualenv `mkvirtualenv dmb && setvirtualenv`. To use this in future run `workon dmb`.
1. Run `./manage.py runserver` to start the server and gulp

# Frontend Setup

The frontend uses gulp for building assets, however it is linked to Django via management commands which pass additional information (e.g. STATIC_ROOT, DEBUG) down to Gulp.

We have the following gulp tasks:

- 'js' - builds the Javascript files
- 'css' - builds the CSS files (from scss)
- 'build' - Builds both JS and CSS
- 'watch' - Does what it says

You can trigger them by running (for example):

    ./manage.py assets build

If you want to build production assets:

    ./manage.py gulp build --settings=core.settings.live

You can generate some test data for developing

    python manage.py testdata

# Folder structure

Source static files live in the Django apps, so currently there is:
This is going to change.
 - 'src/core/static' - Shared assets needed for multiple apps
 - 'src/public/static' - Assets only required for the public app

When building these files are build (as per gulpfile.js) and then output to:

 - 'src/static/dev' - When in development mode
 - 'src/static/dist' - When in production mode (this is what's deployed)

 # Deploy
 The deployment script is inside `scripts` folder and it can be called with or without parameters. Calling the script without parameters will deploy a version based on the last tagged version where the current hash commit is appended. Alternatively, the deploy script can be called with the following paramenters:
 - `major`: it will generate a new major version number and deploy it;
 - `minor`: it will generate a new minor version number and deploy it;
 - `patch`: it will generate a new patch version number and deploy it.

Please run the script from the root of the project, as shown above.
ie.
`$ ./scripts/deploy.sh` can be used to deploy a feature that has to be tested in staging
`$ ./scripts/deploy.sh patch` can be used to launch some copy updates
`$ ./scripts/deploy.sh minor` can be used to launch some new features
`$ ./scripts/deploy.sh major` can be used to launch some a major change

When asked, you will probably want to override the existing static files, `yes`.

Authentication will most likely be your @potatolondon.com account
