#!/bin/bash
FULCON_VER=0.1

# rm old packages
rm -f fulcon_*.dsc fulcon_*_amd64.changes fulcon_*.tar.gz fulcon_*_amd64.deb
rm -rf build

# make build dir
mkdir -p build
pushd build

# link source dir
rm -f fulcon-${FULCON_VER}
ln -s ../../src fulcon-${LXCF_VER}

cd fulcon-${FULCON_VER}

# make the package
dpkg-buildpackage -us -uc

# move pacage files
popd
mv ../fulcon_${FULCON_VER}* .

