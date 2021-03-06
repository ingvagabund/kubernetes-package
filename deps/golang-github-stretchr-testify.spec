%global debug_package   %{nil}
%global import_path     github.com/stretchr/testify
%global commit          da775f0337260efbac0fce9764cee5bd3e8c85b8
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-stretchr-testify
Version:        0
Release:        0.3.git%{shortcommit}%{?dist}
Summary:        Tools for testifying that your code will behave as you intend
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/testify-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Thou Shalt Write Tests

Go code (golang) set of packages that provide many tools for testifying that
your code will behave as you intend.

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/stretchr/objx)
Summary:        Tools for testifying that your code will behave as you intend
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/assert) = %{version}-%{release}
Provides:       golang(%{import_path}/http) = %{version}-%{release}
Provides:       golang(%{import_path}/mock) = %{version}-%{release}
Provides:       golang(%{import_path}/require) = %{version}-%{release}
Provides:       golang(%{import_path}/suite) = %{version}-%{release}

%description devel
Thou Shalt Write Tests

Go code (golang) set of packages that provide many tools for testifying that
your code will behave as you intend.

%prep
%setup -q -n testify-%{commit}

mv LICENCE.txt LICENSE.txt

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}

for d in assert http mock require suite
do
    cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
# as long as there is circular dependency between 
# golang-github-stretchr-testify and golang-github-stretchr-objx
# there can not by test

%files devel
%doc LICENSE.txt README.md
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/assert
%dir %{gopath}/src/%{import_path}/http
%dir %{gopath}/src/%{import_path}/mock
%dir %{gopath}/src/%{import_path}/require
%dir %{gopath}/src/%{import_path}/suite
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/assert/*.go
%{gopath}/src/%{import_path}/http/*.go
%{gopath}/src/%{import_path}/mock/*.go
%{gopath}/src/%{import_path}/require/*.go
%{gopath}/src/%{import_path}/suite/*.go

%changelog
* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.3.gitda775f0
- preserve timestamps of copied files

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.2.gitda775f0
- Fix up devel package listing

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.gitda775f0
- First package for Fedora.
