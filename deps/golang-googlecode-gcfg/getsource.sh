#!/bin/sh

set -x

SPEC=golang-googlecode-cfg.spec

rm *.tar.gz

wget https://gcfg.googlecode.com/archive/$1.tar.gz
mv $1.tar.gz gcfg-${1:0:12}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" ${SPEC}

#increment the version number
rpmdev-bumpspec --comment="Bump to upstream ${1}" --userstring="Eric Paris <eparis@redhat.com" ${SPEC}

sha256sum *.tar.gz *.spec > sources
