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
- `retail-master`: main branch for Retail client `retail` stream

# Installation

1. Clone the repository (you might have already done that!)
2. Run `./bin/install_deps`. If you get errors try using a virtualenv `mkvirtualenv dmb && setvirtualenv`. To use this in future run `workon dmb`.
3. Run `./manage.py runserver` to start the server and gulp

# Configuration

In order for the backend to be able to call Qualtrics APIs, a valid token needs to be configured, all information needed can be found on [DMB Wiki page](https://wiki.p.ota.to/Digital_Maturity_Benchmark).

### Generate a service account private key

1. Go [here](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=gweb-digitalmaturity-staging) and for `gweb-digitalmaturity-staging@appspot.gserviceaccount.com` select the 3 dots, click **Create key** and download the `.p12` keyfile
1. `cd` to the directory where you downloaded the file and run `cat {downloaded-file}.p12 | openssl pkcs12 -nodes -nocerts -passin pass:notasecret | openssl rsa > secret.pem` then move the generated `.pem` file to the `./keys` directory in the project.

# Troubleshooting
1. I get an authentication error when trying to run `manage.py bootstrap`:

    > googleapiclient.errors.HttpError: <HttpError 401 when requesting https://sheets.googleapis.com/v4/spreadsheets?alt=json returned "Request had invalid authentication credentials. Expected OAuth 2 access token, login cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project.">

    To fix this follow the steps under `Generate a service account private key` above.

# Add locale
Before a new locale can work correctly it needs to be explicitly called for that language. For instance, if we want to configure `it` as a new language, we should run:
  ```./manage.py makemessages -i node_modules -i third_party -i src/sitepackages -i src/sitepackages_local -l  --no-wrap --no-location```

Once the previous command has been run, all the existing locales can be maintained by running:
```./manage.py makemessages -i node_modules -i third_party -i src/sitepackages -i src/sitepackages_local --all --no-wrap --no-location```

this will update the existing locales, generating new `.po` files containing the new translations.

After the messages for the locale have been mapped with `makemessages` command, it can be sent out for translation. Once the translation is done, we need to compile the messages in order for django to be using the new translation efficiently. To compile the translations for a specific locale:
```./manage.py compilemessages -l it```

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



# Adding a New Tenant
## Back-end
### Create tenant config file
1. Copy `src/core/settings/tenants/tenant-template.py` and rename it as `<tenant>.py`, e.g. for a tenant `cloud` use `cloud.py`.
1. In the "`# DIMENSIONS`" section change the `<dimension_id>`'s to id's that match the dimension names, eg:
    ```
    DIMENSION_1 = 'strategic_direction'
    DIMENSION_2 = 'user_engagement'
    DIMENSION_3 = 'core_sales'
    DIMENSION_4 = 'emerging_monetization'
    ```
1. If the tenant levels map to scores other than the default values then change the values of the `LEVEL_(n)` variabes in the "`# LEVELS`" section. e.g. if level 3 is reached with scores greater than `5.0` then change it to this:
    ```
    LEVEL_3 = 5
    ```
    If the tenant has more than the default 4 levels, add the additional levels add them as well. e.g. to add a fifth level that is reached for scores greater than `10` add this:
    ```
    LEVEL_5 = 10
    ```
1. For weighted questions change the weights in the `WEIGHTS` object.


### Import the tenant config file

1. Import the tenant config file into `src/core/settings/tenants/__init__.py`:
    ```
    import <tenant> as <tenant>_conf
    ```
1. Add new tenant configuration settings: Add a tenant variable and set it equal to the slug in `src/core/settings/tenants/__init__.py`:
    ```
    NEWTENANT = 'tenant-slug'
    ```
    Then add that tenant variable as a property of the TENANTS object:
    ```
    TENANTS = {
        ...,
        NEWTENANT : {
            ...
        }
    }
    ```
1. Add the following **mandatory fields**:
    - `key`: represent the tenant key, that is used across the platform to uniquely identify the tenant
    - `label`: the translatable string used to describe the tenant
    - `slug`: used in the url to navigate tenant pages
    - `QUALTRICS_SURVEY_ID`: survey id used to pull results and data from the tenant survey
    - `EMAIL_TO`: email to question id in the survey, used to send an email when the result is ready
    - `EMAIL_BCC`: email bcc question id in the survey, used to send an email when the result is ready
    - `DIMENSIONS`: dictionary of dimensions for this specific tenant. Each element of the dictionary is a list of question ids belonging to that specific dimension. **Important!:** If a question ID is not added to this list the question won't be considered for the final score.
    - `CONTENT_DATA`: dictionary of data used to populate content for the tenant, this include: levels, report level descriptions, dimensions labels, headers (more details in `Content Data` section).
    - `MULTI_ANSWER_QUESTIONS`: list of question ids that where can be selected more than one value.
    - `WEIGHTS`: dictionary of question_id, weight for each question within a dimension. If there is no such concept as weighted question, this configuration need to list all the question ids with weight equal to 1.
    - `EXCLUDED_TIME_THRESHOLD`: threshold from which the surveyt result is excluded from the benchmark calculation
    - `CONTACT_EMAIL`: the contact email that is used for this specific tenant
    - `i18n`: wether the tenant is using translations or not. If set to `True` the tenant is enabled for being used multilanguage, `False` if not.
    - `GOOGLE_SHEET_EXPORT_SURVEY_FIELDS`: list of fields that needs to be exported for survey model
    - `GOOGLE_SHEET_EXPORT_RESULT_FIELDS`: list of fields that needs to be exported for survey result model
1. Add the following **optional fields** as needed:
    - `DIMENSIONS_WEIGHTS_QUESTION_ID`: If the weight for each dimension depends on a question answer, then this property needs to be set to the question id.
    - `DIMENSIONS_WEIGHTS`: If the dimesions are weighted, then this configuration is a dictionary of weights:
        ```
        DIMENSIONS_WEIGHTS = {
            DIMENSION_1: 0.4,
            DIMENSION_2: 0.18,
            DIMENSION_3: 0.3,
            DIMENSION_4: 0.12,
        }
        ```
    - `FORCED_INDUSTRY`: If the tenant is not allowed to select an industry from a list, it needs to be forced to a specific value, that can be specified through this paramenter.


## Front-end
### HTML Templates
1. Copy an existing tenant directory e.g. `src/public/templates/public/retail/` and rename it as`<tenant>`. Then update the copy accordingly.

1. Add the tenant to the `<ul>` of `<div class="dmb-footer__tenant-footer">` in `src/public/templates/public/inc/global/footer.html` as follows:
    ```
    {% if tenant|ng_mark_safe != '<tenant>' %}
        <li class="dmb-footer__tenant-footer-list-item">
        <a href="/<tenant-slug>">
            {% trans "<tenant-footer-name>" %}
        </a>
        </li>
    {% endif %}
    ```
    replacing `<tenant>`, `<tenant-slug>` & `<tenant-footer-name>` with the appropriate values.

### Images
1. Copy an exiting images directory e.g. `src/static/src/img/ads/` and rename it as `<tenant>`. 1. Replace the images with the appropriate ones.

### Partner logos
1. Add inline versions of any partner logos to `src/static/src/img/` as `<partner>-logo.png` & `<partner>-logo@2x.png`.
1. If there is a light (e.g. white) version of the logo add them as `<partner>-logo-light.png` & `
<partner>-logo-light@2x.png` otherwise make copies of the normal logos and rename them to these names.


### Add SCSS Tenant Variables
1. Add an entry for the tenant in `$tenants` in `src/static/src/scss/_tenants-variables.scss`
    ```
    $tenants: (
    ...
    cloud: (
        primary-color: $dmb-text-color,
        progress-grid-switch-bp: 800px,
        levels: (
        0: (
            color: $h-gm-yellow-600
        ),
        1: (
            color: $h-gm-yellow-700
        ),
        2: (
            color: $h-gm-yellow-800
        ),
        3: (
            color: $h-gm-yellow-900
        )
        )
    )
    ```
    where `progress-grid-switch-bp` is the breakpoint at which the progress grid in the report rotates. This is determined by the number of levels and the length of the level title strings so should be adjusted per tenant if the default value is too small.


## Qualtrics Survey

### Creating staging survey for new tenant
We have a base survey **DMB Template Survey** to be used as a template. Make a copy of it for a new tenant staging survey, change the **Splash Page** block copy and the questions then copy it to create the production survey. Detailed instructions are below:

1. From control panel click on the 3 dots of **DMB Template Survey**, then on **Copy Project**
1. Change name to `<Tenant> - Staging` and click **Copy Project**
1. Open the survey and go to **Survey Flow**
1. In **Set Embedded Data** change **tenant** & **tenant_slug** to the correct values
1. Click **Save Flow** and go back to the survey edit view
1. Change the copy for the questions in the **Splash Page** block
1. Use a new block for each dimension to force a page break
1. Make sure the first question of each subsequent block (not the first) has the following HTML to show the banner on each page (do not change the alignment or spacing, it makes it easier for translators to find the text):
    ```html
    <div class="dmb-survey-banner"><div class="dmb-survey-banner__logo"><svg width="68px" height="22px" viewBox="0 0 68 22" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><path d="M8.53 16.814C3.895 16.814 0 13.042 0 8.407 0 3.773 3.896 0 8.53 0c2.563 0 4.388 1.005 5.762 2.317l-1.62 1.62c-.984-.923-2.317-1.64-4.143-1.64-3.382 0-6.027 2.727-6.027 6.11 0 3.383 2.645 6.11 6.027 6.11 2.195 0 3.445-.881 4.245-1.681.656-.656 1.087-1.6 1.25-2.891H8.53V7.648h7.73c.083.41.124.903.124 1.435 0 1.723-.472 3.856-1.989 5.373-1.476 1.538-3.363 2.358-5.865 2.358z" fill="#4285F4"></path><path d="M26.004 11.4c0-1.947-1.39-3.28-3-3.28s-3 1.333-3 3.28c0 1.928 1.39 3.281 3 3.281s3-1.353 3-3.28m2.335 0c0 3.116-2.396 5.413-5.335 5.413s-5.335-2.297-5.335-5.413c0-3.138 2.396-5.413 5.335-5.413 2.94 0 5.335 2.275 5.335 5.413" fill="#EA4335"></path><path d="M37.964 11.4c0-1.947-1.389-3.28-3-3.28-1.61 0-3 1.333-3 3.28 0 1.928 1.39 3.281 3 3.281 1.611 0 3-1.353 3-3.28m2.335 0c0 3.116-2.396 5.413-5.335 5.413-2.94 0-5.335-2.297-5.335-5.413 0-3.138 2.395-5.413 5.335-5.413s5.335 2.275 5.335 5.413" fill="#FBBC05"></path><path d="M49.869 11.421c0-1.906-1.272-3.302-2.891-3.302-1.64 0-3.014 1.396-3.014 3.302 0 1.887 1.374 3.26 3.014 3.26 1.62 0 2.89-1.373 2.89-3.26zm2.091-5.106v9.72c0 3.998-2.358 5.639-5.146 5.639-2.625 0-4.203-1.764-4.798-3.2l2.07-.86c.37.88 1.272 1.927 2.728 1.927 1.783 0 2.891-1.107 2.891-3.178v-.78h-.083c-.533.657-1.558 1.23-2.849 1.23-2.707 0-5.187-2.357-5.187-5.392 0-3.055 2.48-5.434 5.187-5.434 1.291 0 2.316.575 2.85 1.21h.082v-.882h2.255z" fill="#4285F4"></path><path fill="#34A853" d="M53.75 16.486h2.379V.574h-2.38z"></path><path d="M59.8 11.237l4.839-2.01c-.268-.676-1.067-1.148-2.01-1.148-1.21 0-2.89 1.066-2.83 3.158m5.68 1.948l1.845 1.23c-.594.882-2.03 2.399-4.51 2.399-3.075 0-5.297-2.379-5.297-5.413 0-3.22 2.241-5.414 5.03-5.414 2.809 0 4.183 2.235 4.634 3.445l.245.615-7.238 2.994c.555 1.086 1.415 1.64 2.626 1.64 1.209 0 2.05-.594 2.665-1.496" fill="#EA4335"></path></g></svg></div><div class="dmb-survey-banner__title">${e://Field/company_name} <br>


    Data maturity assessment


    </div></div>
    ```

1. Make sure the first question of each  subsequent block (not the first) has the following JS:
    ```js
    Qualtrics.SurveyEngine.addOnload(function () {
    jQuery('#' + this.questionId).addClass('dmb-survey-banner-container');
    });

    Qualtrics.SurveyEngine.addOnReady(function () {
    jQuery('#Wrapper').addClass('dmb-survey--in-progress');
    });
    ```

1. Make sure the second question of each subsequent block (not the first) has the following HTML to show the dimension name and logo, replacing `<DIMENSION-SVG-FILENAME>` and `<QUESTION-TEXT>` with the appropritate values (do not change the alignment or spacing, it makes it easier for translators to find the text):
    ```html
    <h2 class="dmb-dimension-header h-c-headline h-c-headline--two"><img class="dmb-dimension-header__icon dmb-u-m-b-s" src="${e://Field/static_url}/img/${e://Field/tenant}/dimensions/<DIMENSION-SVG-FILENAME>">


    Strategic direction and data foundations


    </h2>

    <QUESTION-TEXT>
    ```
1. Add the remaining questions to the dimensions


## Adding/modifying questions

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

## Creating production survey for new tenant
1. From control panel click on 3 dots of the tenant's staging survey, then on **Copy Project**
1. Change the name to `<TENANT> Survey - Production` and click **Copy Project**
1. Open the survey and go to **Survey Flow**
1. Delete the Group called `Version Group`
1. Delete the **Then Branch If**: `If ver` Is Not Empty: branch with the second **Web Service**
1. In **Set Embedded Data** delete the `ver` variable


# Using SVGs

To use an SVG put the .svg file in `src/static/src/svg/` and then reference it in a template using `{% include 'core/inc/svg.html' with id='<filename>' %}`, where `id` is the filename without the '.svg' extension. This will generate an svg with classes `dmb-svg` and `dmb-svg--<filename>`, and width and height HTML attributes set to 100% (can be overridden by CSS `width` and `height` properties). You can also add additional classes to it by setting the `class` variable in the include, e.g. `{% include 'core/inc/svg.html' with id='print-button' class='dmb-addtional-class1 dmb-addtional-class2' %}`.

The `{% include %}` also accepts one of two optional arguments; `size`, which can be any valid size with units that is applied to the `width` and `height` HTML attributes, or `inline`, which is a Boolean that adds a `dmb-svg--inline` class making the size, and left and right margins proportional to font size:
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

## Content data

Since the site has been translated for a tenant, we thought it was easier to have all the tanslatable strings in the BE. This will include:
- `levels`
- `level_descriptions`
- `report_level_descriptions`
- `dimensions`
- `dimension_labels`
- `dimension_headers_descriptions`
- `dimension_level_description`
- `dimension_level_recommendations`
- `dimension_sidepanel_heading`
- `dimension_sidepanel_descriptions`
