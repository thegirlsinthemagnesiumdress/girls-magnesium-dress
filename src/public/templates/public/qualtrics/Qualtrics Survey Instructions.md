# Survey settings
## Look & Feel
### Theme
**Blank**

### Layout
**Flat**

### General
**Header**: Add the following HTML:
```html
<link rel="stylesheet" href="${e://Field/static_url}/css/qualtrics-survey.css" />
<script src="${e://Field/base_url}/static/js/qualtrics-survey.min.js"></script>`
```

**Footer**: Use `footer.html`

### Style
**Primary Color**: *#1a73e8*
**Secondary Color**: *#1a73e8*
**Question Spacing:** *Comfortable*
**Question Text**: *16px*
**Answer Text**: *16px*


## Survey Options
### Survey Termination

**Redirects to full URL**:

Cannot use embedded data here so these must be set manually. Use one of the following, changing `<TENANT>` to the correct tenant:
Dev: `http://localhost:8000/<tenant>/thank-you`
Staging: `https://gweb-digitalmaturity-staging.appspot.com/<tenant>/thank-you`
Production: `https://digitalmaturitybenchmark.withgoogle.com/<tenant>/thank-you`



## Question Components
### Hero
1. Use `hero.html` as question HTML
1. Edit question JavaScript and add `hero.js`


### User Details
Edit question JavaScript and add `user-details.js`


### Privacy Policy
1. Use `privacy-policy.html` as question HTML
1. Edit question JavaScript and add `privacy-policy.js`


### Banner
1. Use `banner.html` as question HTML
1. Edit Question JavaScript and add `banner.js`
1. Copy question to start of each subsequent block


### Dimension heading
1. Use `dimension-heading.html` as question HTML
1. Replace `<!-- DIMENSION NAME GOES HERE -->` with dimension name
1. Replace `<!-- QUESTION TEXT GOES HERE  -->` with question text
1. Replace `<SVG-FILENAME>`with appropriate svg file name.




# Copying survey between *Staging* and *Production*

1. From control panel click on the survey's 3 dots and then on **Copy Project**, edit the name and click **Copy Project**
1. Open the survey and go to **Survey Flow**
1. In the first **Set Embedded Data** block change value of `base_url` to `https://digitalmaturitybenchmark.withgoogle.com`
1. Delete the Group called `Version Group
1. Under **Web Service** change:
    * `URL` value to `https://digitalmaturitybenchmark.withgoogle.com/api/company-name`
    * `Authorisation` value to the appropriate auth token used by Django REST framework, which can be obtained from the Google Cloud Platform `authtoken_token` from [here](https://console.cloud.google.com/datastore/entities;kind=authtoken_token;ns=__$DEFAULT$__/query/kind?project=gweb-digitalmaturity)
