%global provider        github
%global provider_tld    com
%global project         coreos
%global repo            go-etcd
%global commit          23142f6773a676cc2cae8dd0cb90b2ea761c853f

%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath          %{_datadir}/gocode
%global shortcommit     %(c=%{commit}; echo ${c:0:8})
%global debug_package   %{nil}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.2.rc1
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        The official etcd v0.2 client library for Go
License:        ASL 2.0
URL:            http://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

%description
%{summary}

%package devel
Requires:       golang
BuildRequires:	git
Summary:        A golang library for logging to systemd
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/etcd) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use coreos/go-etcd.

%prep
%autosetup -Sgit -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/etcd
install -t %{buildroot}/%{gopath}/src/%{import_path}/etcd etcd/*.go

%files devel
%doc LICENSE README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/etcd
%{gopath}/src/%{import_path}/etcd/*.go

%changelog
* Sat Sep 06 2014 Eric Paris <eparis@redhat.com - 0.2.rc1-0.1.git23142f67.2
- Bump to upstream 23142f6773a676cc2cae8dd0cb90b2ea761c853f

* Wed Aug 20 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-0.1-rc1
- Initial fedora package
