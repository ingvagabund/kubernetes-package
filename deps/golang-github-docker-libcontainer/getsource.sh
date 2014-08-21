#!/bin/sh

SPEC=golang-github-docker-libcontainer.spec

rm *.tar.gz

wget https://github.com/docker/libcontainer/archive/$1/libcontainer-${1:0:8}.tar.gz

#put the git hash in there
sed -i -e "s/%global commit\([[:space:]]\+\)[[:xdigit:]]\{40\}/%global commit\1$1/" ${SPEC}

#increment the version number
rpmdev-bumpspec --comment="Bump to upstream ${1}" --userstring="Eric Paris <eparis@redhat.com" ${SPEC}

sha256sum *.tar.gz *.spec > sources
