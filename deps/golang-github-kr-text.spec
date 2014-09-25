%global debug_package   %{nil}
%global import_path     github.com/kr/text
%global commit          6807e777504f54ad073ecef66747de158294b639
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-kr-text
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        Go package for manipulating paragraphs of text
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/text-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
%{summary}

%package devel
BuildRequires:  golang
BuildRequires:  golang(github.com/kr/pty)
Requires:       golang
Summary:        Go package for manipulating paragraphs of text
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/colwriter) = %{version}-%{release}
Provides:       golang(%{import_path}/mc) = %{version}-%{release}

%description devel
%{summary}

This package contains the library source intended for building other packages
which use kr/text.

%prep
%setup -n text-%{commit}

%build

%install
chmod 664 wrap.go
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}

for d in colwriter mc
do
    mv $d/Readme Readme-$d
    cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{gopath}:%{buildroot}%{gopath} go test %{import_path}
GOPATH=%{gopath}:%{buildroot}%{gopath} go test %{import_path}/colwriter
GOPATH=%{gopath}:%{buildroot}%{gopath} go test %{import_path}/mc

%files devel
%doc License Readme Readme-colwriter Readme-mc
%dir %{gopath}/src/github.com/kr
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/colwriter
%dir %{gopath}/src/%{import_path}/mc
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/colwriter/*.go
%{gopath}/src/%{import_path}/mc/*.go

%changelog
* Thu Sep 11 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.git6807e77
- gopath defined in golang package
- preserve timestamps while copying source files
- attrs not needed
- devel description update
- include check section
- get rid of files listed twice warning for doc files
- noarch
- needs kr/pty as BR
- chmod wrap.go to 644 (needs to be upstreamed)

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.git6807e77
- First package for Fedora.
