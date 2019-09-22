#!/bin/bash

GROW_VERSION=0.5.0
PIP_ARGS="--upgrade"


set -e  # Exit on error

do_set_user_flag () {
  PIP_ARGS="$PIP_ARGS --user"
}

do_install () {
  pip install $PIP_ARGS grow==$GROW_VERSION
  echo "Done."
  exit 0
}

do_bail () {
  echo "Exiting."
  exit 1
}

show_warning () {
  cat << EOM
Warning: Not in a virtualenv.

Installing Grow SDK in a virtualenv is preferred because it allows multiple
projects to depend on different Grow versions. You can continue without a
virtualenv but Grow will be installed for the current user.

EOM
}

if [[ -z "$VIRTUAL_ENV" ]]; then
  show_warning
  read -p "Continue without a virtualenv? [yN] " yn
  case $yn in
    # If Y or y, continue
    [Yy]*) do_set_user_flag;;
    # For all else, exit
    *) do_bail;;
  esac
fi

do_install
