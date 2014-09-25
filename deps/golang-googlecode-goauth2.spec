%global provider        google
%global provider_sub    code
%global provider_tld    com
%global repo            goauth2
%global import_path     %{provider_sub}.%{provider}.%{provider_tld}/p/%{repo}
%global rev             afe77d958c701557ec5dc56f6936fcc194d15520
%global shortrev        %(r=%{rev}; echo ${r:0:12})

Name:           golang-%{provider}%{provider_sub}-%{repo}
Version:        0
Release:        0.2.hg%{shortrev}%{?dist}
Summary:        OAuth 2.0 for Go clients
License:        BSD
URL:            http://%{import_path}
Source0:        https://%{repo}.%{provider}%{provider_sub}.%{provider_tld}/archive/%{rev}.tar.gz
BuildArch:      noarch

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        OAuth 2.0 for Go clients
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/serviceaccount) = %{version}-%{release}
Provides:       golang(%{import_path}/compute) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/serviceaccount) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the OAuth 2.0 for Go clients library.


%prep
%setup -n %{repo}-%{shortrev} -q

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in oauth appengine compute; do
   cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{gopath}:%{buildroot}/%{gopath} go test %{import_path}/oauth

%files devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/oauth
%dir %{gopath}/src/%{import_path}/oauth/example
%dir %{gopath}/src/%{import_path}/oauth/jwt
%dir %{gopath}/src/%{import_path}/oauth/jwt/example
%dir %{gopath}/src/%{import_path}/appengine
%dir %{gopath}/src/%{import_path}/appengine/serviceaccount
%dir %{gopath}/src/%{import_path}/compute
%dir %{gopath}/src/%{import_path}/compute/serviceaccount
%{gopath}/src/%{import_path}/oauth/*.go
# oauth/example/oauthreq.go is executable in the tarball, undo it
%attr(644,-,-) %{gopath}/src/%{import_path}/oauth/example/*.go
%{gopath}/src/%{import_path}/oauth/jwt/*.go
%{gopath}/src/%{import_path}/oauth/jwt/example/*.go
%{gopath}/src/%{import_path}/oauth/jwt/example/*.json
%{gopath}/src/%{import_path}/oauth/jwt/example/*.pem
%{gopath}/src/%{import_path}/appengine/serviceaccount/*.go
%{gopath}/src/%{import_path}/compute/serviceaccount/*.go

%changelog
* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hgafe77d958c70
- update to afe77d958c70
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg6a3615e294b5
- First package for Fedora.
