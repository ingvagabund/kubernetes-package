%global provider_prefix	code
%global provider        google
%global provider_tld    com
%global project         p
%global repo            go.exp
%global commit          bd8df7009305d6ada223ea3c95b94c0f38bfa119

%global import_path     %{provider_prefix}.%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath          %{_datadir}/gocode
%global shortcommit     %(c=%{commit}; echo ${c:0:12})
%global debug_package   %{nil}

%global go_arch %(go env GOHOSTARCH)
%global go_root %(go env GOROOT)

Name:           golang-googlecode-go-exp
Version:        0
Release:        1.0.hg%{shortcommit}%{?dist}
Summary:        Experimental tools and packages for Go
License:        BSD
URL:            http://%{import_path}
Source0:        https://there/is/not/one/go-exp-%{shortcommit}.tar.gz
BuildRequires:  golang


%description
%{summary}.

%package devel
Requires:	golang
BuildRequires:	git
Summary:	%{summary}
Provides:	golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path}/ebnf) = %{version}-%{release}
Provides:	golang(%{import_path}/ebnflint) = %{version}-%{release}
Provides:	golang(%{import_path}/fsnotify) = %{version}-%{release}
Provides:	golang(%{import_path}/inotify) = %{version}-%{release}
Provides:	golang(%{import_path}/locale/search) = %{version}-%{release}
Provides:	golang(%{import_path}/old/netchan) = %{version}-%{release}
Provides:	golang(%{import_path}/utf8string) = %{version}-%{release}
Provides:	golang(%{import_path}/winfsnotify) = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -Sgit -n %{repo}-%{shortcommit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
for d in ebnf ebnflint fsnotify inotify locale/search old/netchan utf8string winfsnotify; do
	cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%doc LICENSE PATENTS README 
%dir %{gopath}/src/%{provider_prefix}.%{provider}.%{provider_tld}
%dir %{gopath}/src/%{provider_prefix}.%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*

%changelog
* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.hgbd8df7009305
- Bump to upstream bd8df7009305d6ada223ea3c95b94c0f38bfa119

