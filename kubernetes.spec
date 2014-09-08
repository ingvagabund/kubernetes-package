#debuginfo not supported with Go
%global debug_package	%{nil}
%global import_path	github.com/GoogleCloudPlatform/kubernetes
%global commit		6ebe69a8751508c11d0db4dceb8ecab0c2c7314a
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

#binaries which should be called kube-*
%global prefixed_binaries proxy apiserver controller-manager scheduler
#binaries which should not be renamed at all
%global nonprefixed_binaries kubelet kubecfg
#all of the above
%global binaries	%{prefixed_binaries} %{nonprefixed_binaries}

Name:		kubernetes
Version:	0.1
Release:	0.4.git%{shortcommit}%{?dist}
Summary:	Kubernetes container management
License:	ASL 2.0
URL:		https://github.com/GoogleCloudPlatform/kubernetes
ExclusiveArch:	x86_64
Source0:	https://github.com/GoogleCloudPlatform/kubernetes/archive/%{commit}/kubernetes-%{shortcommit}.tar.gz

#config files
Source10:	config
Source11:	apiserver
Source12:	controller-manager
Source13:	proxy
Source14:	kubelet
Source15:	scheduler
#service files
Source20:	kube-apiserver.service
Source21:	kube-controller-manager.service
Source22:	kube-proxy.service
Source23:	kubelet.service
Source24:	kube-scheduler.service

Patch1:		0001-Move-default-target-list-from-build_go-to-config_go.patch
Patch2:		0002-function-to-turn-list-of-targets-to-list-of-go-packa.patch
Patch3:		0003-more-stuff.patch
Patch4:		0004-Use-go-build-not-go-install-because-of-golang-issue.patch
Patch5:		0005-Do-not-ignore-local-GOPATH-ignore-3rd-party-deps.patch
Patch6:		0006-remove-all-third-party-software.patch

Requires:	/usr/bin/docker
Requires:	etcd
Requires:	cadvisor

Requires(pre):	shadow-utils

BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	golang >= 1.2-7
BuildRequires:	systemd
BuildRequires:	golang-cover
BuildRequires:	etcd

BuildRequires:	golang(bitbucket.org/kardianos/osext)
BuildRequires:	golang(github.com/coreos/go-log/log)
BuildRequires:	golang(github.com/coreos/go-systemd)
BuildRequires:	golang(github.com/coreos/go-etcd/etcd)
BuildRequires:	golang(github.com/google/gofuzz)
BuildRequires:	golang(code.google.com/p/go.net)
BuildRequires:	golang(code.google.com/p/goauth2)
BuildRequires:	golang(code.google.com/p/go-uuid)
BuildRequires:	golang(code.google.com/p/google-api-go-client)
BuildRequires:	golang(github.com/fsouza/go-dockerclient) > 0-0.6
BuildRequires:	golang(github.com/golang/glog)
BuildRequires:	golang(github.com/stretchr/objx)
BuildRequires:	golang(github.com/stretchr/testify)
BuildRequires:	golang(gopkg.in/v1/yaml)
BuildRequires:	golang(github.com/google/cadvisor)

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit}

%build
export KUBE_GIT_COMMIT=%{commit}
export KUBE_GIT_TREE_STATE="dirty"
export KUBE_GIT_VERSION=v%{version}

. hack/config-go.sh
version_ldflags=$(kube::version_ldflags)
export GOPATH=${KUBE_TARGET}:%{gopath}

targets=($(kube::default_build_targets))
binaries=($(kube::binaries_from_targets "${targets[@]}"))

for binary in ${binaries[@]}; do
  bin=$(basename "${binary}")
  echo "+++ Building ${bin}"
  go build -o "${KUBE_TARGET}/bin/${bin}" \
        "${goflags[@]:+${goflags[@]}}" \
        -ldflags "${version_ldflags}" \
        "${binary}"
done

%check
export GOPATH=%{gopath}
echo "******Testing the go code******"
hack/test-go.sh
echo "******Testing the commands******"
hack/test-cmd.sh

%install
install -m 755 -d %{buildroot}%{_bindir}
for bin in %{prefixed_binaries}; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 _output/go/bin/${bin} %{buildroot}%{_bindir}/kube-${bin}
done
for bin in %{nonprefixed_binaries}; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 _output/go/bin/${bin} %{buildroot}%{_bindir}/${bin}
done

# install config files
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15}

# install service files
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24}

%files
%doc README.md
%{_bindir}/*
%{_unitdir}/*.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/apiserver
%config(noreplace) %{_sysconfdir}/%{name}/controller-manager
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/scheduler

%pre
getent group kube >/dev/null || groupadd -r kube
getent passwd kube >/dev/null || useradd -r -g kube -d / -s /sbin/nologin \
        -c "Kubernetes user" kube
%post
%systemd_post %{basename:%{SOURCE20}} %{basename:%{SOURCE21}} %{basename:%{SOURCE22}} %{basename:%{SOURCE22}} %{basename:%{SOURCE24}}

%preun
%systemd_preun %{basename:%{SOURCE20}} %{basename:%{SOURCE21}} %{basename:%{SOURCE22}} %{basename:%{SOURCE23}} %{basename:%{SOURCE24}}

%postun
%systemd_postun

%changelog
* Mon Sep 08 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-0.4.git6ebe69a
- prefer autosetup instead of setup (revert setup change in 0-0.3.git)
https://fedoraproject.org/wiki/Autosetup_packaging_draft
- revert version number to 0.1

* Mon Sep 08 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.3.git6ebe69a
- gopath defined in golang package already
- package owns /etc/kubernetes
- bash dependency implicit
- keep buildroot/$RPM_BUILD_ROOT macros consistent
- replace with macros wherever possible
- set version, release and source tarball prep as per
https://fedoraproject.org/wiki/Packaging:SourceURL#Github

* Mon Sep 08 2014 Eric Paris <eparis@redhat.com>
- make services restart automatically on error

* Sat Sep 06 2014 Eric Paris <eparis@redhat.com - 0.1-0.1.0.git6ebe69a8
- Bump to upstream 6ebe69a8751508c11d0db4dceb8ecab0c2c7314a

* Wed Aug 13 2014 Eric Paris <eparis@redhat.com>
- update to upstream
- redo build to use project scripts
- use project scripts in %check
- rework deletion of third_party packages to easily detect changes
- run apiserver and controller-manager as non-root

* Mon Aug 11 2014 Adam Miller <maxamillion@redhat.com>
- update to upstream
- decouple the rest of third_party

* Thu Aug 7 2014 Eric Paris <eparis@redhat.com>
- update to head
- update package to include config files

* Wed Jul 16 2014 Colin Walters <walters@redhat.com>
- Initial package
