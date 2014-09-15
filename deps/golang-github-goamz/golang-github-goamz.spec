%global provider	github
%global provider_tld	com
%global project		mitchellh
%global repo		goamz
%global commit		9cad7da945e699385c1a3e115aa255211921c9bb

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath		%{_datadir}/gocode
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{repo}
Version:	0.0.0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	An Amazon Library for Go
License:	LGPL3+
URL:		http://%{import_path}
Source0:	https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz


%description
%{summary}.

%package devel
Requires:	golang
BuildRequires:	git
Summary:	A golang library for logging to systemd
Provides:	golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path}/autoscaling) = %{version}-%{release}
Provides:	golang(%{import_path}/aws) = %{version}-%{release}
Provides:	golang(%{import_path}/ec2) = %{version}-%{release}
Provides:	golang(%{import_path}/elb) = %{version}-%{release}
Provides:	golang(%{import_path}/exp) = %{version}-%{release}
Provides:	golang(%{import_path}/iam) = %{version}-%{release}
Provides:	golang(%{import_path}/rds) = %{version}-%{release}
Provides:	golang(%{import_path}/route53) = %{version}-%{release}
Provides:	golang(%{import_path}/s3) = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -Sgit -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in autoscaling aws ec2 elb exp iam rds route53 s3; do
	cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%doc LICENSE README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/autoscaling
%{gopath}/src/%{import_path}/autoscaling/*
%dir %{gopath}/src/%{import_path}/aws
%{gopath}/src/%{import_path}/aws/*
%dir %{gopath}/src/%{import_path}/ec2
%{gopath}/src/%{import_path}/ec2/*
%dir %{gopath}/src/%{import_path}/elb
%{gopath}/src/%{import_path}/elb/*
%dir %{gopath}/src/%{import_path}/exp
%dir %{gopath}/src/%{import_path}/exp/mturk
%{gopath}/src/%{import_path}/exp/mturk/*
%dir %{gopath}/src/%{import_path}/exp/sdb
%{gopath}/src/%{import_path}/exp/sdb/*
%dir %{gopath}/src/%{import_path}/exp/sns
%{gopath}/src/%{import_path}/exp/sns/*
%dir %{gopath}/src/%{import_path}/iam
%{gopath}/src/%{import_path}/iam/*
%dir %{gopath}/src/%{import_path}/rds
%{gopath}/src/%{import_path}/rds/*
%dir %{gopath}/src/%{import_path}/route53
%{gopath}/src/%{import_path}/route53/*
%dir %{gopath}/src/%{import_path}/s3
%{gopath}/src/%{import_path}/s3/*

%changelog
* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.git9cad7da
- Bump to upstream 9cad7da945e699385c1a3e115aa255211921c9bb

