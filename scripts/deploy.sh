#!/bin/bash

appid=gweb-digitalmaturity-staging
hash=$(git rev-parse --short=5 HEAD)

./manage.py gulp build --settings=core.settings.live
python manage.py collectstatic --settings=core.settings.live
./third_party/google_appengine/appcfg.py update --no_cookies -A $appid -V 0-0-1-$hash ./src
