# Talent Revolution

# Prerequisites

1. You need to have a local SSH key linked to a GitHub account, which is a member of the [PotatoLondon organization](https://github.com/potatolondon)

# Installation

1. Clone the repository (you might have already done that!)
2. Run `./bin/install_deps`. If you get errors try using a virtualenv `mkvirtualenv dmb && setvirtualenv`. To use this in future run `workon dmb`.
3. Run `./manage.py runserver` to start the server and gulp

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

By default the script deploy to the staging instance `gweb-digitalmaturity-staging`, it's possibile to pass
a `-p` flag to deploy to the production instance `gweb-digitalmaturity`.

Please run the script from the root of the project, as shown above.
ie.
`$ ./scripts/deploy.sh` can be used to deploy a feature that has to be tested in staging
`$ ./scripts/deploy.sh patch` can be used to launch some copy updates
`$ ./scripts/deploy.sh minor` can be used to launch some new features
`$ ./scripts/deploy.sh major` can be used to launch some a major change

When asked, you will probably want to override the existing static files, `yes`.

Authentication will most likely be your @potatolondon.com account

# Qualtrics
We have two different surveys, one for the `production` environment and the other one used for `development` and `staging`

* [Production](https://google.co1.qualtrics.com/ControlPanel/?ClientAction=EditSurvey&Section=SV_ebQG3AGFIgVzCFT&SubSection=&SubSubSection=&PageActionOptions=&TransactionID=2&Repeatable=0)
* [Staging/Development](https://google.co1.qualtrics.com/ControlPanel/?ClientAction=EditSurvey&Section=SV_beH0HTFtnk4A5rD&SubSection=&SubSubSection=&PageActionOptions=&TransactionID=4&Repeatable=0)

Unfortunately they're not linked, that means every change has to manually done in both.

## Add(modify) a question

* Create question in Qualtrics (remember that we have 2 different surveys for development and production)
* Assign a score to each question - Check the Scoring section for more detail
* Every question is assigned to a dimension (a category). Unfortunately we can't set a dimension in Qualtrics. In `src/core/settings/constants.py`, the `QuestionId` (visible in Qualtrics) needs to be added
to the `DIMENSIONS` dictionary.
**IMPORTANT**: If a questions is not added to the `DIMENSIONS` object the question won't be used to calculate the final benchmark
* If the question is supposed to have a `weight` different from 1 it needs to be added to the `WEIGHTS` constant in `src/core/settings/constants.py`
* If the question is multi answer it needs to be added to the `MULTI_ANSWER_QUESTION` constant in `src/core/settings/constants.py`


## Scoring
In order to calculate the benchmark out of the survey, we assign values to the questions answers.
This can be done through the Survey Control Panel, using the [Recode Values](https://www.qualtrics.com/support/survey-platform/survey-module/question-options/recode-values/) functionality.

Unfortunately the way qualtrics exports multiple answer data is buggy, if 2 answers have the same value some data gets losts.

We decided to assign values values to the multiple answers following the following convention:
```
--{score}-{answer_index}
```

for instance these are valid values:
```
--1--1
--1.33-2
--0.5-1
```
for the sake of the benchmark this map to:
```
score = 1.0
score = 1.33
score = 0.5
```
