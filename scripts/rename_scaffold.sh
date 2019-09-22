#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "Please supply a single argument of the new app name"
    echo "E.g. ./scripts/rename_scaffold.sh my-new-app"
    exit 1
fi

camel_case () {
  echo $1 | perl -pe "s/(-)./uc($&)/ge;s/-//g"
  return 0
}

do_rename () {
  echo "Renaming..."
  # Rename app in config files
  perl -i -pe "s/grow-gae-scaffold/$PROJECT_NAME/g" app.yaml package.json
  # Rename module in javascript files
  perl -i -pe "s/scaffold/$JS_PROJECT_NAME/g" views/base.html gulp/tasks/compile-js.js source/js/*.js
  # Clear git history
  rm -rf .git
  git init >/dev/null
  echo "Done."
  exit 0
}

do_bail() {
  echo "Exiting."
  exit 1
}


PROJECT_NAME=$1
JS_PROJECT_NAME=$(camel_case $PROJECT_NAME)

read -p "Rename project to $PROJECT_NAME? [Yn] " confirm
case $confirm in
  [Nn]*) do_bail;;
      *) do_rename;;
esac
