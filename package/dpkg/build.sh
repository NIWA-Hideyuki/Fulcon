#!/bin/bash

FULCON_VER=$(grep "^VERSION" ../../Makefile | sed -e s'/VERSION=//')
PATH=`dirname $PWD`/rpm/script:$PATH

# rm old packages
rm -f fulcon_*.dsc fulcon_*_amd64.changes fulcon_*.tar.gz fulcon_*_amd64.deb
rm -rf build

# make changelog
pushd ../../src
make clean libdir=/usr/lib
cd ..
git clean -xdf
git set-file-times
( cd src ; TZ=UTC gitlog2changelog.py )
popd

# make build dir
mkdir -p build
pushd build

# link source dir
rm -f fulcon-${FULCON_VER}
ln -s ../../../src fulcon-${FULCON_VER}
cd fulcon-${FULCON_VER}

# make the package
dpkg-buildpackage -us -uc

# move pacage files
popd
mv ../../fulcon_${FULCON_VER}* .

exit 0
