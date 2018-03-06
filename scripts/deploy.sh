#!/bin/bash

./manage.py gulp build --settings=core.settings.live
python manage.py collectstatic --settings=core.settings.live
./third_party/google_appengine/appcfg.py update --no_cookies -A potato-trev-test -V [version] ./src
