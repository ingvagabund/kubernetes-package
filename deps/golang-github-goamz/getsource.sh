#!/bin/sh

set -x
set -e

SPEC=golang-github-goamz.spec

rm *.tar.gz

wget https://github.com/mitchellh/goamz/archive/$1/goamz-${1:0:7}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" ${SPEC}

#increment the version number
rpmdev-bumpspec --comment="Bump to upstream ${1}" --userstring="Eric Paris <eparis@redhat.com" ${SPEC}

sha256sum *.tar.gz *.spec > sources
