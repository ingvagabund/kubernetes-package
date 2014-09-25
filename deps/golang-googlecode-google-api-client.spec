%global debug_package   %{nil}
%global import_path     code.google.com/p/google-api-go-client
%global rev             e1c259484b495133836706f46319f5897f1e9bf6
%global shortrev        %(r=%{rev}; echo ${r:0:12})

Name:           golang-googlecode-google-api-client
Version:        0
Release:        0.2.alpha.hg%{shortrev}%{?dist}
Summary:        Go libraries for "new style" Google APIs
License:        BSD
URL:            http://%{import_path}

Source0:        https://google-api-go-client.googlecode.com/archive/%{rev}.tar.gz
BuildArch:      noarch

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
BuildRequires:  golang(code.google.com/p/goauth2/oauth)
Requires:       golang >= 1.2.1-3
Requires:       golang(code.google.com/p/goauth2/oauth)
Summary:        Go libraries for "new style" Google APIs
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/admin) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/directory_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/email_migration_v2) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/reports_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/adsensehost) = %{version}-%{release}
Provides:       golang(%{import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v2.4) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/appsactivity) = %{version}-%{release}
Provides:       golang(%{import_path}/appsactivity/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/appstate) = %{version}-%{release}
Provides:       golang(%{import_path}/appstate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/audit) = %{version}-%{release}
Provides:       golang(%{import_path}/audit/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/autoscaler) = %{version}-%{release}
Provides:       golang(%{import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/bigquery) = %{version}-%{release}
Provides:       golang(%{import_path}/bigquery/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/books) = %{version}-%{release}
Provides:       golang(%{import_path}/books/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/us_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudmonitoring) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudmonitoring/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/compute) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/content) = %{version}-%{release}
Provides:       golang(%{import_path}/content/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/coordinate) = %{version}-%{release}
Provides:       golang(%{import_path}/coordinate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/customsearch) = %{version}-%{release}
Provides:       golang(%{import_path}/customsearch/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/discovery) = %{version}-%{release}
Provides:       golang(%{import_path}/discovery/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclickbidmanager) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclicksearch) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/drive) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1-sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/games) = %{version}-%{release}
Provides:       golang(%{import_path}/games/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesmanagement) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides:       golang(%{import_path}/gan) = %{version}-%{release}
Provides:       golang(%{import_path}/gan/v1beta) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1beta) = %{version}-%{release}
Provides:       golang(%{import_path}/gmail) = %{version}-%{release}
Provides:       golang(%{import_path}/gmail/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi/internal/uritemplates) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi/transport) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-generator) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-generator/testdata) = %{version}-%{release}
Provides:       golang(%{import_path}/groupsmigration) = %{version}-%{release}
Provides:       golang(%{import_path}/groupsmigration/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/identitytoolkit) = %{version}-%{release}
Provides:       golang(%{import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/licensing) = %{version}-%{release}
Provides:       golang(%{import_path}/licensing/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/manager) = %{version}-%{release}
Provides:       golang(%{import_path}/manager/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/mirror) = %{version}-%{release}
Provides:       golang(%{import_path}/mirror/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/orkut) = %{version}-%{release}
Provides:       golang(%{import_path}/orkut/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plus) = %{version}-%{release}
Provides:       golang(%{import_path}/plus/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plusdomains) = %{version}-%{release}
Provides:       golang(%{import_path}/plusdomains/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.5) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.6) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/qpexpress) = %{version}-%{release}
Provides:       golang(%{import_path}/qpexpress/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/siteverification) = %{version}-%{release}
Provides:       golang(%{import_path}/siteverification/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/spectrum) = %{version}-%{release}
Provides:       golang(%{import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/storage) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/tasks) = %{version}-%{release}
Provides:       golang(%{import_path}/tasks/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/translate) = %{version}-%{release}
Provides:       golang(%{import_path}/translate/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/urlshortener) = %{version}-%{release}
Provides:       golang(%{import_path}/urlshortener/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webfonts) = %{version}-%{release}
Provides:       golang(%{import_path}/webfonts/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtube) = %{version}-%{release}
Provides:       golang(%{import_path}/youtube/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}

%description devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%prep

%setup -n google-api-go-client-%{shortrev} -q

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
mv googleapi/internal/uritemplates/LICENSE LICENSE-googleapi-internal-uritemplates
for d in ./*; do
    if [[ -d $d ]]; then
        cp -pav $d %{buildroot}/%{gopath}/src/%{import_path}/
    fi
done

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/googleapi
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/google-api-go-generator

%files devel
%doc AUTHORS CONTRIBUTORS LICENSE Makefile NOTES README TODO
%doc LICENSE-googleapi-internal-uritemplates
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/examples/gopher.png
%{gopath}/src/%{import_path}/lib/codereview/codereview.cfg
%{gopath}/src/%{import_path}/*/*.go
%{gopath}/src/%{import_path}/*/*/*.go
%{gopath}/src/%{import_path}/*/*/*/*.go
%{gopath}/src/%{import_path}/*/*/*.json
%{gopath}/src/%{import_path}/*/*/*.want

%changelog
* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.alpha.hge1c259484b49
- update to e1c259484b495133836706f46319f5897f1e9bf6
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.alpha.hg0923cdda5b82
- First package for Fedora.
