# Talent Revolution

# Prerequisites

1. You need to have a local SSH key linked to a GitHub account, which is a member of the [PotatoLondon organization](https://github.com/potatolondon)

# Branches

As good practice rule for the project, it has been decided to organize the work using the kind of branches:
- features:
    - be in the form of `feature/<ticket_id>-<short_description_of_the_feature>`
    - should contain `[touch:<ticket_id>]` inside the commit messages, to update tickets using *hermes hooks*
- hotfixes:
    - be in the form of `hotfix/<ticket_id>-<short_description_of_the_fix>`
    - should contain `[touch:<ticket_id>]` inside the commit messages, to update tickets using *hermes hooks*

Working branches are organized as follows:

- `master`: contains production code
- `news-master`: main branch for Publishers client `news` workflow

# Installation

1. Clone the repository (you might have already done that!)
2. Run `./bin/install_deps`. If you get errors try using a virtualenv `mkvirtualenv dmb && setvirtualenv`. To use this in future run `workon dmb`.
3. Run `./manage.py runserver` to start the server and gulp

# Configuration

In order for the backend to be able to call Qualtrics APIs, a valid token needs to be configured, all information needed can be found on [DMB Wiki page](https://wiki.p.ota.to/Digital_Maturity_Benchmark).

# Add locale
Before a new locale can work correctly it needs to be explicitly called for that language. For instance, if we want to configure a `it` as  new language, we should run:
  ```./manage.py makemessages -i node_modules -i third_party -i src/sitepackages -i src/sitepackages_local -l it```

Once the previous command has been run, all the existing locales can be maintaned running:
```./manage.py makemessages -i node_modules -i third_party -i src/sitepackages -i src/sitepackages_local --all```

this will update the existing locales, generating new `.po` files containing the new translations.

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

We're versioning js and css files, that's automatically handled by static_rev template tag. However we're generaring survey-{hash-of-content}.min.js and survey-{hash-of-content}.min.css that are fed to the Qualtrics Survey page. Please make sure to update the references there if there are any changes to those files ( through Qualtrics Look&Feel panel).

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

We decided to assign values to the multiple answers following the following convention:
```
--{score*100}.{choice_index}
```
The score * 100 has to be a 3 digit number.

for instance these are valid values:
```
100.1
133.2
050.3
```
for the sake of the benchmark this map to:
```
score = 1.0
score = 1.33
score = 0.5
```

# Using SVGs

To use an SVG put the .svg file in `src/static/src/svg/` and then reference it in a template using `{% include 'core/inc/svg.html' with id='<filename>' %}`, where `id` is the filename without the '.svg' extension. This will generate an svg with classes `dmb-svg` and `dmb-svg--<filename>`, and width and height HTML attributes set to 100% (can be overridden by CSS `width` and `height` properties). You can also add additional classes to it by setting the `class` variable in the include, e.g. `{% include 'core/inc/svg.html' with id='print-button' class='dmb-addtional-class' %}`.

The `{% include %}` also accepts one of two optional arguments; `size`, which accepts any valid size with units and sets the `width` and `height` attributes, or `inline`, which is a Boolean that adds a `dmb-svg--inline` class making the size, and left and right margins proportional to font size:
```scss
.dmb-svg--inline {
  height: .75em;
  margin-left: .3125em;
  margin-right: .3125em;
  width: .75em;
}
```

For example, SVG file `src/static/src/svg/print-button.svg` can be used in the following ways:

- `{% include 'core/inc/svg.html' with id='print-button' only %}` will generate:
    ```html
    <svg role="img" class="dmb-svg dmb-svg--print-button" width="100%" height="100%">
    ...
    </svg>
    ```

- `{% include 'core/inc/svg.html' with id='print-button' size='30px' only %}` will generate:
    ```html
    <svg role="img" class="dmb-svg dmb-svg--print-button" width="30px" height="30px">
    ...
    </svg>
    ```

- `{% include 'core/inc/svg.html' with id='print-button' inline=True only %}` will generate:
    ```html
    <svg role="img" class="dmb-svg dmb-svg--print-button dmb-svg--inline">
    ...
    </svg>
    ```
