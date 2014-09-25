%global provider	github
%global provider_tld	com
%global project		vaughan0
%global repo		go-ini
%global commit		a98ad7ee00ec53921f08832bc06ecf7fd600e6a1

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	0.2.git%{shortcommit}%{?dist}
Summary:	INI parsing library for Go
License:	BSD
URL:		http://%{import_path}
Source0:	https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:	noarch

%description
%{summary}.

%package devel
BuildRequires:	golang >= 1.2.1-3
Requires:	golang >= 1.2.1-3
Summary:	INI parsing library for Go (golang)
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav test.ini %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}

%files devel
%doc LICENSE README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%attr(644,-,-) %{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/test.ini

%changelog
* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.gita98ad7e
- noarch devel package
- don't redefine gopath
- don't own dirs owned by golang
- preserve timestamps of copied files
- devel package buildrequires golang 1.2.1-3 or higher
- correct version and package name

* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.gita98ad7e
- Bump to upstream a98ad7ee00ec53921f08832bc06ecf7fd600e6a1
