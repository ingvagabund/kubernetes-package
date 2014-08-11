#debuginfo not supported with Go
%global debug_package	%{nil}
%global gopath		%{_datadir}/gocode
%global import_path	github.com/GoogleCloudPlatform/kubernetes
%global commit		71c6e082d497696a9875d62412f22ae9d19d2491
%global shortcommit	%(c=%{commit}; echo ${c:0:8})

#binaries which should be called kube-*
%global prefixed_binaries proxy integration apiserver controller-manager
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
BuildRequires:	golang(gopkg.in/v1/yaml)
BuildRequires:	golang(github.com/google/cadvisor)

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit}

rm -r third_party/src/bitbucket.org/kardianos/osext

rm -r third_party/src/code.google.com/p/go.net
rm -r third_party/src/code.google.com/p/goauth2
rm -r third_party/src/code.google.com/p/go-uuid
rm -r third_party/src/code.google.com/p/google-api-go-client
rm -r third_party/src/gopkg.in/v1/yaml/
rm -r third_party/src/gonuts.org/v1/yaml/
rm -r third_party/src/github.com/coreos/go-{log,systemd,etcd}
rm -r third_party/src/github.com/fsouza/go-dockerclient
rm -r third_party/src/github.com/golang/glog
rm -r third_party/src/github.com/google/cadvisor/

# FIXME (if we can)
# Unable to remove go-dockerclient-copiedstructs because this is not really
# a third party repo, it is a copy of go-dockerclient::container.go with some
# yaml annotation which they use for testing and I think marshalling and
# unmashalling....
# rm -r third_party/src/github.com/fsouza/go-dockerclient-copiedstructs

# Set the "version number", currently git commit id upstream 
sed "s/@@GIT_COMMIT@@/%{shortcommit}/g" \
  pkg/version/template.go.tmpl >pkg/version/autogenerated.go

%build
mkdir _build

pushd _build
    mkdir -p src/github.com/GoogleCloudPlatform
    ln -s $(dirs +1 -l) src/%{import_path}

    # FIXME - This source doesn't appear to exist at the import path so for
    #         now it must be bundled. Need to fix if we can.
    mkdir -p src/github.com/fsouza/
    ln -s \
    $(dirs +1 -l)/third_party/src/github.com/fsouza/go-dockerclient-copiedstructs \
        src/github.com/fsouza/go-dockerclient-copiedstructs
popd
export GOPATH=$(pwd)/_build:%{buildroot}%{gopath}:%{gopath}

# Default to building all of the components
for cmd in %{binaries}
do
    go build %{import_path}/cmd/${cmd}
done

%install
install -m 755 -d %{buildroot}%{_bindir}
for bin in %{prefixed_binaries}; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 ${bin} %{buildroot}%{_bindir}/kube-${bin}
done
for bin in %{nonprefixed_binaries}; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 ${bin} %{buildroot}%{_bindir}/${bin}
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
%systemd_post kubernetes-proxy.service kubernetes-integration.service kubernetes-apiserver.server kubernetes-controller-manager.service

%preun
%systemd_preun kubernetes-proxy.service kubernetes-integration.service kubernetes-apiserver.server kubernetes-controller-manager.service

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
