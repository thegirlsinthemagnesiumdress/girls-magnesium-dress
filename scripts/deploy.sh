#!/bin/bash

# function cleanVersionString() {
#     local res=`echo $1 | sed 's/[. ]/-/g'`
#     echo $res
# }

TAG_NAME=`git describe --always --tags --dirty`

DEFAULT_VERSION=$(cleanVersionString "$TAG_NAME")

# DEFAULT_APP_ID=`cat app.yaml | grep "application:" | sed 's/application: //g'`

if [ "$1" != "--no-input" ]; then
  read -p "APP ID (blank for $DEFAULT_APP_ID): " USER_APP_ID
fi

# APP_ID=${USER_APP_ID:-$DEFAULT_APP_ID}
# VERSION=${USER_VERSION:-$DEFAULT_VERSION}
# VERSION=$(cleanVersionString "$VERSION")

# Deploying
# gulp test
rm -rf ./build
gulp build
grow build
gulp predeploy
# ./sitepackages/google_appengine/appcfg.py update --no_cookies -A $APP_ID -V $VERSION ./
git add build -f
git commit -m "Deploy version " + $VERSION
git subtree push --prefix build origin gh-pages
