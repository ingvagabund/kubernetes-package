%global provider	github
%global provider_tld	com
%global project		google
%global	repo		gofuzz
%global commit		aef70dacbc78771e35beb261bb3a72986adf7906

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	0.4.git%{shortcommit}%{?dist}
Summary:	Library for populating go objects with random values
License:	ASL 2.0
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:	noarch

%description
%{summary}

%package devel
Requires:	golang >= 1.2.1-3
BuildRequires:	golang >= 1.2.1-3
Summary:	%{summary}
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use %{project}/%{repo}

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}

%check
GOPATH=%{gopath}:%{buildroot}%{gopath} go test %{import_path}

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%attr(644,-,-) %{gopath}/src/%{import_path}/*

%changelog
* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.4.gitaef70da
- don't redefine gopath
- don't own dirs owned by golang
- preserve timestamps of copied files
- use golang 1.2.1-3 or higher
- quiet setup
- add check

* Tue Aug 12 2014 Eric Paris <eparis@redhat.com> - 0.3.gitaef70da
- Move location and make a bit more generic

* Tue Aug 12 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.gitaef70da
- Fix License

* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.gitaef70da
- First package for Fedora.
