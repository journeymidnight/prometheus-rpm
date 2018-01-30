%define debug_package %{nil}

Name:		libvirt_exporter
Release:	1%{?dist}
Version:        %{version}
Summary:	Prometheus exporter for libvirt metrics, written in Go with pluggable metric collectors.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/kumina/libvirt_exporter
SOURCE:         %{name}-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
AutoReqProv:	No

%description

libvirt exporter for machine metrics, written in Go with pluggable metric collectors.

%prep
%setup -q -n libvirt_exporter-%{version}.linux-amd64

%build
echo

%install
install -D -m 755 libvirt_exporter $RPM_BUILD_ROOT/usr/bin/libvirt_exporter
install -D -m 644 contrib/libvirt_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/libvirt_exporter.service

%clean


%post

systemctl enable libvirt_exporter
systemctl start libvirt_exporter

%files
%defattr(-,root,root,-)
/usr/bin/libvirt_exporter
/usr/lib/systemd/system/libvirt_exporter.service

