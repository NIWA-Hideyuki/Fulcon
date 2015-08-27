#!/bin/bash

FULCON_VERSION=$(grep "^VERSION" ../../Makefile | sed -e s'/VERSION=//')
PATH=${PWD/%package/script}:$PATH

rm -rf SOURCES/*
rm -rf RPMS/*
rm -rf SRPMS/*

cd ../../src
make clean libdir=/usr/lib`[ $(uname -m) == x86_64 ] && echo 64`
cd ..
git clean -xdf
git set-file-times
( cd FULCON ; TZ=UTC gitlog2changelog.py )
mv Fulcon Fulcon-"$FULCON_VERSION"
tar czf Fulcon-"$FULCON_VERSION".tar.gz Fulcon-"$FULCON_VERSION"
mv Fulcon-"$FULCON_VERSION" FULCON

cp Fulcon-"$FULCON_VERSION".tar.gz package/SOURCES

cd package/SOURCES
tar xzf Fulcon-"$FULCON_VERSION".tar.gz

cd ..
cp SOURCES/Fulcon-*/fulcon.spec SPECS/fulcon.spec

rpmbuild -v -ba --clean SPECS/fulcon.spec
