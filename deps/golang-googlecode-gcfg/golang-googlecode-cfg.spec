%global provider_prefix	code
%global provider        google
%global provider_tld    com
%global project         p
%global repo            gcfg
%global commit          c2d3050044d05357eaf6c3547249ba57c5e235cb

%global import_path     %{provider_prefix}.%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath          %{_datadir}/gocode
%global shortcommit     %(c=%{commit}; echo ${c:0:12})
%global debug_package   %{nil}

Name:           golang-%{provider}-%{repo}
Version:        0.0.0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        Gcfg reads INI-style configuration files into Go structs
License:        BSD
URL:            http://%{import_path}
Source0:	https://gcfg.googlecode.com/archive/gcfg-%{shortcommit}.tar.gz


%description
%{summary}.

%package devel
Requires:       golang
BuildRequires:	git
Summary:        A golang library for logging to systemd
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/scanner) = %{version}-%{release}
Provides:       golang(%{import_path}/token) = %{version}-%{release}
Provides:       golang(%{import_path}/types) = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -Sgit -n %{repo}-%{shortcommit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d %{buildroot}/%{gopath}/src/%{import_path}
install -t %{buildroot}/%{gopath}/src/%{import_path}/ *.go
for d in scanner token types; do
	cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%doc LICENSE README
%dir %{gopath}/src/%{provider_prefix}.%{provider}.%{provider_tld}
%dir %{gopath}/src/%{provider_prefix}.%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go
%dir %{gopath}/src/%{import_path}/scanner
%{gopath}/src/%{import_path}/scanner
%dir %{gopath}/src/%{import_path}/token
%{gopath}/src/%{import_path}/token/*.go
%dir %{gopath}/src/%{import_path}/types
%{gopath}/src/%{import_path}/types/*.go

%changelog
* Fri Sep 12 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.gitc2d30500
- Bump to upstream c2d3050044d05357eaf6c3547249ba57c5e235cb

