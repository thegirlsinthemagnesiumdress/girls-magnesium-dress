## Survey Flow
**Set Embedded Data**:

`base_url`:
Dev: `http://localhost:8000`
Staging: `https://gweb-digitalmaturity-staging.appspot.com`
Production: `https://digitalmaturitybenchmark.withgoogle.com`

`static_url`:
Dev: `http://localhost:8000/devstatic`
Staging: `https://gweb-digitalmaturity-staging.appspot.com/static`
Production: `https://digitalmaturitybenchmark.withgoogle.com/static`


## Look & Feel
### Theme
**Dynamic Themes**: Select *Google* from dropdown list then select *Blank* theme

### Layout
**Layout**: *Flat*

### General
**Header**: Add the following script tag:
`<script src="${e://Field/base_url}/static/js/qualtrics-survey.min.js"></script>`

**Footer**: Use `./footer.html`


### Style
**Primary Color**: *#1a73e8*
**Secondary Color**: *#1a73e8*
**Question Spacing:** *Comfortable*
**Question Text**: *16px*
**Answer Text**: *16px*

**External CSS**
Cannot use embedded data here so these must be set manually. Use one of the following:
Dev: `http://localhost:8000/devstatic/css/qualtrics-survey.css`
Staging: `https://gweb-digitalmaturity-staging.appspot.com/static/css/qualtrics-survey.css`
Production: `https://digitalmaturitybenchmark.withgoogle.com/static/css/qualtrics-survey.css`


## Survey Options
### Survey Termination

**Redirects to full URL**:
Cannot use embedded data here so these must be set manually. Use one of the following, changing `<TENANT>` to the correct tenant:
Dev: `http://localhost:8000/<TENANT>/thankyou`
Staging: `https://gweb-digitalmaturity-staging.appspot.com/<TENANT>/thankyou`
Production: `https://digitalmaturitybenchmark.withgoogle.com/<TENANT>/thankyou`


## Question Components
### Hero
1. Use `./hero.html` as question HTML
1. Use `./hero.js` as the question JS

### User Details
Edit Question JavaScript and add `./user-details.js`


### Privacy Policy
1. Use `./privacy-policy.html` as question HTML
1. Use `./privacy-policy.js` as the question JS


### Banner
1. Use `./banner.html` as question HTML
1. Use `./banner.js` as the question JS
1. Copy question to start of each subsequent block

### Dimension heading
1. Use `./dimension-heading.html` as question HTML
1. Replace `<!-- DIMENSION NAME GOES HERE -->` with dimension name
1. Replace `<!-- QUESTION TEXT GOES HERE  -->` with question text
1. Replace `<SVG-FILENAME>`with appropriate svg.
