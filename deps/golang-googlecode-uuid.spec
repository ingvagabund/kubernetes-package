%global debug_package   %{nil}
%global import_path     code.google.com/p/go-uuid
%global rev             7dda39b2e7d5e265014674c5af696ba4186679e9
%global shortrev        %(r=%{rev}; echo ${r:0:12})

Name:           golang-googlecode-uuid
Version:        0
Release:        0.2.hg%{shortrev}%{?dist}
Summary:        Generates and inspects UUIDs based on RFC 4122 and DCE 1.1
License:        BSD
URL:            http://%{import_path}
Source0:        https://go-uuid.googlecode.com/archive/%{rev}.tar.gz
BuildArch:      noarch

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        Generates and inspects UUIDs based on RFC 4122 and DCE 1.1
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/go-uuid) = %{version}-%{release}

%description devel
%{summary}

Generates and inspects UUIDs based on RFC 4122 and DCE 1.1: 
Authentication and Security Services. 

%prep

%setup -n go-uuid-%{shortrev} -q
mv uuid/LICENSE ./

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in uuid; do
   cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/uuid

%files devel
%doc CONTRIBUTORS LICENSE
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/uuid
%attr(644,-,-) %{gopath}/src/%{import_path}/uuid/*.go

%changelog
* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hg7dda39b2e7d5
- preserve timestamps
- do not own dirs owned by golang

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg7dda39b2e7d5
- First package for Fedora.
