%global commit d1c4472bf2efd3826f2b5bdcc02d8416798d678c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global import_path     github.com/golang/glog

Name:           golang-github-golang-glog
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        Leveled execution logs for Go
License:        ASL 2.0
URL:            http://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/glog-%{commit}.tar.gz
BuildArch:      noarch

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        Enables Go programs to comfortably encode and decode YAML values
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package
    http://code.google.com/p/google-glog

By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control over logging at the file level.

%prep
%setup -n glog-%{commit} -q

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{gopath}:%{buildroot}%{gopath} go test %{import_path}

%files devel
%doc LICENSE README
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.gitd1c4472
- BR golang
- include check

* Tue Aug 05 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1.gitd1c4472b
- First package for Fedora
