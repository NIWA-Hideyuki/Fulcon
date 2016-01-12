#!/bin/bash

FULCON_VERSION=$(grep "^VERSION" ../../Makefile | sed -e s'/VERSION=//')
PATH=${PWD/%package/script}/script:$PATH

rm -rf SOURCES/*
rm -rf RPMS/*
rm -rf SRPMS/*

cd ../../src
make clean libdir=/usr/lib
cd ..
git clean -xdf
git set-file-times
( cd src ; TZ=UTC gitlog2changelog.py )
mv src fulcon-"$FULCON_VERSION"
tar czf package/rpm/SOURCES/fulcon-"$FULCON_VERSION".tar.gz fulcon-"$FULCON_VERSION"
mv fulcon-"$FULCON_VERSION" src

cd package/rpm/SOURCES
tar xzf fulcon-"$FULCON_VERSION".tar.gz

cd ..
cp SOURCES/fulcon-*/fulcon.spec SPECS/fulcon.spec

rpmbuild -v -ba --clean SPECS/fulcon.spec
