%global provider_prefix code
%global provider        google
%global provider_tld    com
%global project         p
%global repo            gcfg
%global commit          c2d3050044d05357eaf6c3547249ba57c5e235cb

%global import_path     %{provider_prefix}.%{provider}.%{provider_tld}/%{project}/%{repo}
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global setupcommit     %(c=%{commit}; echo ${c:0:12})
%global debug_package   %{nil}

Name:           golang-%{provider}%{provider_prefix}-%{repo}
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        Gcfg reads INI-style configuration files into Go structs
License:        BSD
URL:            http://%{import_path}
Source0:        https://gcfg.googlecode.com/archive/%{commit}.tar.gz
BuildArch:      noarch


%description
%{summary}.

%package devel
Requires:       golang >= 1.2.1-3
BuildRequires:  golang >= 1.2.1-3
Summary:        A golang library for logging to systemd
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/scanner) = %{version}-%{release}
Provides:       golang(%{import_path}/token) = %{version}-%{release}
Provides:       golang(%{import_path}/types) = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{repo}-%{setupcommit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go  %{buildroot}/%{gopath}/src/%{import_path}/
for d in scanner token types testdata; do
        cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{buildroot}%{gopath}:%{gopath} go test %{import_path}

%files devel
%doc LICENSE README
%dir %{gopath}/src/%{import_path}
%attr(664,-,-) %{gopath}/src/%{import_path}/*.go
%dir %{gopath}/src/%{import_path}/scanner
%{gopath}/src/%{import_path}/scanner
%dir %{gopath}/src/%{import_path}/token
%attr(664,-,-) %{gopath}/src/%{import_path}/token/*.go
%dir %{gopath}/src/%{import_path}/types
%attr(664,-,-) %{gopath}/src/%{import_path}/types/*.go
%dir %{gopath}/src/%{import_path}/testdata
%attr(664,-,-) %{gopath}/src/%{import_path}/testdata/*.gcfg

%changelog
* Fri Sep 12 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2gitc2d3050
- don't own dirs owned by golang
- preserve timestamps
- noarch

* Fri Sep 12 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.gitc2d30500
- Bump to upstream c2d3050044d05357eaf6c3547249ba57c5e235cb

