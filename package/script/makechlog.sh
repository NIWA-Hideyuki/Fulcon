#!/bin/sh

# Fulcon
# Copyright (C) 2015 NIWA Hideyuki

# script to make the ChangeLog

PATH=$PWD:$PATH

cd ..
git set-file-times
cd lxcf
TZ=UTC gitlog2changelog.py

exit 0
