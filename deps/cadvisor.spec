%global commit ba041ddf654c5bea988d478e2224352748f80404
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global import_path     github.com/google/cadvisor
%global gopath          %{_datadir}/gocode

Name:           cadvisor
Version:        0.2.0
Release:        2%{?dist}
Summary:        Analyzes resource usage and performance characteristics of running containers.
License:        ASL2.0
URL:            http://%{import_path}
Source0:        https://github.com/google/cadvisor/archive/%{commit}/cadvisor-%{shortcommit}.tar.gz
Patch0:         0001-add-systemd-unit-file-sysconfig.patch
BuildRequires:  docker-io-pkg-devel
BuildRequires:  systemd
BuildRequires:  golang
BuildRequires:  golang(github.com/docker/libcontainer)
BuildRequires:  golang(github.com/fsouza/go-dockerclient)
BuildRequires:  golang(github.com/coreos/go-systemd)
BuildRequires:  golang(github.com/godbus/dbus)
BuildRequires:  golang(github.com/kr/text)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/influxdb/influxdb/client)
BuildRequires:  golang(github.com/stretchr/testify)
BuildRequires:  golang(github.com/stretchr/objx)
ExclusiveArch:  x86_64 

%description
%{summary}

cAdvisor (Container Advisor) provides container users an understanding of the
resource usage and performance characteristics of their running containers.
It is a running daemon that collects, aggregates, processes, and exports
information about running containers. Specifically, for each container it keeps
resource isolation parameters, historical resource usage, histograms of
complete historical resource usage and network statistics. This data is
exported by container and machine-wide.

cAdvisor currently supports lmctfy containers as well as Docker containers (those
that use the default libcontainer execdriver). Other container backends can also
be added. cAdvisor's container abstraction is based on lmctfy's so containers are
inherently nested hierarchically.

%package devel
Requires:       golang
Summary:        enables Go programs to comfortably encode and decode YAML values
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/advice) = %{version}-%{release}
Provides:       golang(%{import_path}/advice/interface) = %{version}-%{release}
Provides:       golang(%{import_path}/api) = %{version}-%{release}
Provides:       golang(%{import_path}/client) = %{version}-%{release}
Provides:       golang(%{import_path}/container) = %{version}-%{release}
Provides:       golang(%{import_path}/container/docker) = %{version}-%{release}
Provides:       golang(%{import_path}/container/libcontainer) = %{version}-%{release}
Provides:       golang(%{import_path}/container/raw) = %{version}-%{release}
Provides:       golang(%{import_path}/deploy) = %{version}-%{release}
Provides:       golang(%{import_path}/info) = %{version}-%{release}
Provides:       golang(%{import_path}/manager) = %{version}-%{release}
Provides:       golang(%{import_path}/pages) = %{version}-%{release}
Provides:       golang(%{import_path}/pages/static) = %{version}-%{release}
Provides:       golang(%{import_path}/sampling) = %{version}-%{release}
Provides:       golang(%{import_path}/storage) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/cache) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/influxdb) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/memory) = %{version}-%{release}
Provides:       golang(%{import_path}/utils) = %{version}-%{release}
BuildRequires:  docker-io-pkg-devel
BuildRequires:  golang
BuildRequires:  golang(github.com/docker/libcontainer)
BuildRequires:  golang(github.com/fsouza/go-dockerclient)
BuildRequires:  golang(github.com/coreos/go-systemd)
BuildRequires:  golang(github.com/godbus/dbus)
BuildRequires:  golang(github.com/kr/text)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/influxdb/influxdb/client)
BuildRequires:  golang(github.com/stretchr/testify)
BuildRequires:  golang(github.com/stretchr/objx)

%description devel
%{summary}

cAdvisor (Container Advisor) provides container users an understanding of the
resource usage and performance characteristics of their running containers.
It is a running daemon that collects, aggregates, processes, and exports
information about running containers. Specifically, for each container it keeps
resource isolation parameters, historical resource usage, histograms of
complete historical resource usage and network statistics. This data is
exported by container and machine-wide.

cAdvisor currently supports lmctfy containers as well as Docker containers (those
that use the default libcontainer execdriver). Other container backends can also
be added. cAdvisor's container abstraction is based on lmctfy's so containers are
inherently nested hierarchically.

%prep
%setup -n %{name}-%{commit} -q

%patch0 -p1

%build
mkdir _build

pushd _build
  mkdir -p src/github.com/google
  ln -s $(dirs +1 -l) src/github.com/google/cadvisor
popd
export GOPATH=$(pwd)/_build:%{buildroot}%{gopath}:%{gopath}

### FIXME
### Upstream uses this invocation of go build but it fails with the following:
# go build --ldflags '-extldflags "-static"' github.com/google/cadvisor
#   # github.com/google/cadvisor
#   /usr/bin/ld: cannot find -lpthread
#   /usr/bin/ld: cannot find -lc
#   collect2: error: ld returned 1 exit status
#   /usr/lib/golang/pkg/tool/linux_amd64/6l: running gcc failed: unsuccessful exit status 0x100
#
# It *seems* fine without it, but I assume upstream has a reason for doing
# this, however I've yet to get a response on why and if it's necessary.

go build github.com/google/cadvisor

%install
# main package binary
install -d -p %{buildroot}%{_bindir}
install -p -m0755 cadvisor %{buildroot}%{_bindir}

# install systemd/sysconfig 
install -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m0660 sysconfig/%{name} %{buildroot}%{_sysconfdir}/sysconfig/%{name} 
install -d -m0755 %{buildroot}%{_prefix}/lib/systemd/system
install -p -m0644 init/%{name}.service %{buildroot}%{_prefix}/lib/systemd/system/%{name}.service

# devel package golang libs
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}/

for d in advice api client container deploy info manager pages sampling storage \
          utils
do
    cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%post
%systemd_post cadvisor.service

%preun
%systemd_preun cadvisor.service

%postun
%systemd_postun

%files
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS LICENSE README.md 
%{_bindir}/cadvisor
%{_prefix}/lib/systemd/system/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%files devel
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS LICENSE README.md 
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/api
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/client
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/container
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/deploy
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/info
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/manager
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/pages
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/sampling
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/storage
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/utils
%{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/api/*
%{gopath}/src/%{import_path}/client/*
%{gopath}/src/%{import_path}/container/*
%{gopath}/src/%{import_path}/deploy/*
%{gopath}/src/%{import_path}/info/*
%{gopath}/src/%{import_path}/manager/*
%{gopath}/src/%{import_path}/pages/*
%{gopath}/src/%{import_path}/sampling/*
%{gopath}/src/%{import_path}/storage/*
%{gopath}/src/%{import_path}/utils/*

%changelog
* Thu Aug 07 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-1
- First package for Fedora
