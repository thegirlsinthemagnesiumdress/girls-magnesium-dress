#!/bin/bash

gulp build
grow build
gulp predeploy
dev_appserver.py app.yaml
