## General

#### Look & Feel > Theme

Use **Blank** theme



#### Look & Feel > Layout

Flat



#### Look & Feel > General > Header

Add one of the following script tags:

Staging: `script src="https://news-dot-gweb-digitalmaturity-staging.appspot.com/static/js/qualtrics-survey.min.js"></script>`
Production: `<script src="https://digitalmaturitybenchmark.withgoogle.com/static/js/qualtrics-survey.min.js"></script`



#### Look & Feel > General > Footer

Use `./footer.html`



#### Look & Feel > Style

**Primary Color**: `#1a73e8`

**Question spacing:** Comfortable

**Question Text** and **Answer Text**: 16px

**External CSS**:

Development: `http://localhost:8000/devstatic/css/qualtrics-<tenant>.css`
Staging: `https://news-dot-gweb-digitalmaturity-staging.appspot.com/static/css/qualtrics-<tenant>.css`
Production: `https://digitalmaturitybenchmark.withgoogle.com/static/css/qualtrics-<tenant>.css`


#### Survey Options > Survey Termination

**Redirect**:
Development: `http://localhost:8000/<tenant>/thankyou`
Staging: `https://news-dot-gweb-digitalmaturity-staging.appspot.com/<tenant>/thankyou`
Production: `https://digitalmaturitybenchmark.withgoogle.com/<tenant>/thankyou`


## Question Components

### Hero

1. Use `./hero.html` as question HTML
2. Replace `http://localhost:8000/devstatic` with `https://news-dot-gweb-digitalmaturity-staging.appspot.com/static` for staging, and `https://digitalmaturitybenchmark.withgoogle.com/static` for production
3. Edit Question JavaScript and add `./hero.js`



### User Details

Edit Question JavaScript and add `./user-details.js`



### Privacy Policy

1. Use `./privacy-policy.html` as question HTML
2. Edit Question JavaScript and add `./privacy-policy.js`



### Banner

1. Use `./banner.html` as question HTML
2. Edit Question JavaScript and add `./banner.js`
3. Copy question to start of each subsequent block



### Dimension heading

1. Use `./dimension-heading.html` as question HTML
2. Add dimension name below `<!-- DIMENSION NAME GOES HERE -->`
3. Add question text below `<!-- QUESTION TEXT GOES HERE  -->`
4. Replace `<svg-filename>`with appropriate svg.
5. Replace `http://localhost:8000/devstatic/` with `https://news-dot-gweb-digitalmaturity-staging.appspot.com/static` for staging, and `https://digitalmaturitybenchmark.withgoogle.com/static` for production



















