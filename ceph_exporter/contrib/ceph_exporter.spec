%define debug_package %{nil}

Name:		ceph_exporter
Release:	1%{?dist}
Version:        %{version}
Summary:	Prometheus exporter for ceph metrics, written in Go with pluggable metric collectors.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/digitalocean/ceph_exporter
SOURCE:         %{name}-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
AutoReqProv:	No

%description

ceph exporter for machine metrics, written in Go with pluggable metric collectors.

%prep
%setup -q -n ceph_exporter-%{version}.linux-amd64

%build
echo

%install
install -D -m 755 ceph_exporter $RPM_BUILD_ROOT/usr/bin/ceph_exporter
install -D -m 644 contrib/ceph_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/ceph_exporter.service

%clean


%post

sudo systemctl start ceph_exporter
sudo systemctl enable ceph_exporter

%files
%defattr(-,root,root,-)
/usr/bin/ceph_exporter
/usr/lib/systemd/system/ceph_exporter.service

