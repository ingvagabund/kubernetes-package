%global provider	github
%global provider_tld	com
%global project		vaughan0
%global repo		go-ini
%global commit		a98ad7ee00ec53921f08832bc06ecf7fd600e6a1

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath		%{_datadir}/gocode
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{repo}
Version:	0.0.0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	INI parsing library for Go (golang)
License:	BSD
URL:		http://%{import_path}
Source0:	https://github.com/%{project}/%{repo}/archive/$1/%{repo}-%{shortcommit}.tar.gz

%description
%{summary}.

%package devel
Requires:	golang
BuildRequires:	git
Summary:	A golang library for logging to systemd
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -Sgit -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -t %{buildroot}/%{gopath}/src/%{import_path}/ *.go

%files devel
%doc LICENSE README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.gita98ad7e
- Bump to upstream a98ad7ee00ec53921f08832bc06ecf7fd600e6a1
