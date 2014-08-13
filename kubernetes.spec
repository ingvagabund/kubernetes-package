#debuginfo not supported with Go
%global debug_package	%{nil}
%global gopath		%{_datadir}/gocode
%global import_path	github.com/GoogleCloudPlatform/kubernetes
%global commit		71c6e082d497696a9875d62412f22ae9d19d2491
%global shortcommit	%(c=%{commit}; echo ${c:0:8})

#binaries which should be called kube-*
%global prefixed_binaries proxy apiserver controller-manager
#binaries which should not be renamed at all
%global nonprefixed_binaries kubelet kubecfg
#all of the above
%global binaries	%{prefixed_binaries} %{nonprefixed_binaries}

Name:		kubernetes
Version:	0
Release:	0.0.16.git%{shortcommit}%{?dist}
Summary:	Kubernetes container management
License:	ASL 2.0
URL:		https://github.com/GoogleCloudPlatform/kubernetes
ExclusiveArch:	x86_64
Source0:	https://github.com/GoogleCloudPlatform/kubernetes/archive/%{commit}/kubernetes-%{shortcommit}.tar.gz
Source1:	config
Source2:	apiserver
Source3:	controller-manager
Source4:	proxy
Source5:	kubelet
Source6:	kube-apiserver.service
Source7:	kube-controller-manager.service
Source8:	kube-proxy.service
Source9:	kubelet.service
Patch1:		0001-Use-go-build-not-go-install-because-of-golang-issue.patch
Patch2:		0002-Respect-version-passed-in-via-environment-variable.patch
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	golang >= 1.2-7
BuildRequires:	systemd
Requires:	/usr/bin/docker
Requires:	etcd
Requires:	cadvisor

BuildRequires:	golang(bitbucket.org/kardianos/osext)
BuildRequires:	golang(github.com/coreos/go-log/log)
BuildRequires:	golang(github.com/coreos/go-systemd)
BuildRequires:	golang(github.com/coreos/go-etcd/etcd)
BuildRequires:	golang(code.google.com/p/go.net)
BuildRequires:	golang(code.google.com/p/goauth2)
BuildRequires:	golang(code.google.com/p/go-uuid)
BuildRequires:	golang(code.google.com/p/google-api-go-client)
BuildRequires:	golang(github.com/fsouza/go-dockerclient)
BuildRequires:	golang(github.com/golang/glog)
BuildRequires:	golang(github.com/stretchr/objx)
BuildRequires:	golang(github.com/stretchr/testify)
BuildRequires:	golang(gopkg.in/v1/yaml)
BuildRequires:	golang(github.com/google/cadvisor)

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit}

rm -r third_party/src/bitbucket.org/kardianos/osext
rmdir third_party/src/bitbucket.org/kardianos
rmdir third_party/src/bitbucket.org/

rm -r third_party/src/code.google.com/p/go.net
rm -r third_party/src/code.google.com/p/goauth2
rm -r third_party/src/code.google.com/p/go-uuid
rm -r third_party/src/code.google.com/p/google-api-go-client
rmdir third_party/src/code.google.com/p
rmdir third_party/src/code.google.com/

rm -r third_party/src/gopkg.in/v1/yaml/
rmdir third_party/src/gopkg.in/v1/
rmdir third_party/src/gopkg.in/

rm -r third_party/src/gonuts.org/v1/yaml/
rmdir third_party/src/gonuts.org/v1/
rmdir third_party/src/gonuts.org/

rm -r third_party/src/github.com/coreos/go-{log,systemd,etcd}
rmdir third_party/src/github.com/coreos/
rm -r third_party/src/github.com/fsouza/go-dockerclient
rm -r third_party/src/github.com/golang/glog
rmdir third_party/src/github.com/golang/
rm -r third_party/src/github.com/google/cadvisor/
rmdir third_party/src/github.com/google/
rm -r third_party/src/github.com/stretchr/objx
rm -r third_party/src/github.com/stretchr/testify/
rmdir third_party/src/github.com/stretchr/

# FIXME (if we can)
# Unable to remove go-dockerclient-copiedstructs because this is not really
# a third party repo, it is a copy of go-dockerclient::container.go with some
# yaml annotation which they use for testing and I think marshalling and
# unmashalling....
# rm -r third_party/src/github.com/fsouza/go-dockerclient-copiedstructs
# rmdir third_party/src/github.com/fsouza/
# rmdir third_party/src/github.com/f
# rmdir third_party/src/
# rmdir third_party/
# So instead, just explode if there is anything left other than this one...
FILES=`find third_party/src -type f`
if [[ $FILES != "third_party/src/github.com/fsouza/go-dockerclient-copiedstructs/container.go" ]]; then
	echo "UNPACKED THIRD PARTY SOFTWARE FOUND!"
	exit 1
fi

%build
export git_commit="%{shortcommit}-dirty"
export GOPATH=%{gopath}

hack/build-go.sh

%install
install -m 755 -d %{buildroot}%{_bindir}
for bin in %{prefixed_binaries}; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 output/go/bin/${bin} %{buildroot}%{_bindir}/kube-${bin}
done
for bin in %{nonprefixed_binaries}; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 output/go/bin/${bin} %{buildroot}%{_bindir}/${bin}
done

# install config files
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/kubernetes
install -m 644 -t $RPM_BUILD_ROOT%{_sysconfdir}/kubernetes %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}

# install service files
install -d -m 0755 $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 -t $RPM_BUILD_ROOT%{_unitdir} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9}

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/*
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/kubernetes/config
%config(noreplace) %{_sysconfdir}/kubernetes/apiserver
%config(noreplace) %{_sysconfdir}/kubernetes/controller-manager
%config(noreplace) %{_sysconfdir}/kubernetes/proxy
%config(noreplace) %{_sysconfdir}/kubernetes/kubelet

%post
%systemd_post %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9}

%preun
%systemd_preun %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9}

%postun
%systemd_postun

%changelog
* Mon Aug 11 2014 Adam Miller <maxamillion@redhat.com>
- update to upstream
- decouple the rest of third_party

* Thu Aug 7 2014 Eric Paris <eparis@redhat.com>
- update to head
- update package to include config files

* Wed Jul 16 2014 Colin Walters <walters@redhat.com>
- Initial package
