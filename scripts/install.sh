#!/bin/bash

echo "Installing node modules"
npm i
./scripts/install_appengine.py
./scripts/install_grow.sh
