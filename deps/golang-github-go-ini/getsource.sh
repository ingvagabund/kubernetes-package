#!/bin/sh

set -x
set -e

SPEC=golang-github-go-ini.spec

rm *.tar.gz

wget https://github.com/vaughan0/go-ini/archive/$1/go-ini-${1:0:7}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" ${SPEC}

#increment the version number
rpmdev-bumpspec --comment="Bump to upstream ${1}" --userstring="Eric Paris <eparis@redhat.com" ${SPEC}

sha256sum *.tar.gz *.spec > sources
