%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}
%bcond_with sysvinit
%bcond_without systemd

Name:		prometheus
Version:	%{version}
%if %{with sysvinit}
Release:	1.sysvinit%{?dist}
%endif
%if %{with systemd}
Release:	1%{?dist}
%endif
Summary:	Prometheus is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/prometheus
Source0:	https://github.com/prometheus/prometheus/releases/download/%{version}/prometheus-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
%if %{with sysvinit}
Requires:       daemonize
%endif
%if %{with systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif
AutoReqProv:	No

%description

Prometheus is a systems and service monitoring system.
It collects metrics from configured targets at given intervals, evaluates
rule expressions, displays the results, and can trigger alerts if
some condition is observed to be true.

%prep
%setup -q -n prometheus-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/consoles
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/console_libraries
%if %{with sysvinit}
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
%endif
%if %{with systemd}
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
%endif


install -m 644 contrib/prometheus.rules $RPM_BUILD_ROOT/etc/prometheus/prometheus.rules
install -m 644 contrib/prometheus.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/prometheus
install -m 644 contrib/prometheus.yaml $RPM_BUILD_ROOT/etc/prometheus/prometheus.yaml
install -m 755 prometheus $RPM_BUILD_ROOT/usr/bin/prometheus
install -m 755 promtool $RPM_BUILD_ROOT/usr/bin/promtool
%if %{with sysvinit}
install -m 755 contrib/prometheus.init $RPM_BUILD_ROOT/etc/init.d/prometheus
%endif
%if %{with systemd}
install -m 755 contrib/prometheus.service $RPM_BUILD_ROOT/usr/lib/systemd/system/prometheus.service
%endif


%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0

%post
chgrp prometheus /var/run/prometheus
chmod 774 /var/run/prometheus
chown prometheus:prometheus /var/log/prometheus
chmod 744 /var/log/prometheus
%if %{with systemd}
/usr/lib/systemd/system/prometheus.service
%endif
chown prometheus:prometheus -R /etc/prometheus

%files
%defattr(-,root,root,-)
%if %{with sysvinit}
/etc/init.d/prometheus
%endif
%if %{with systemd}
/usr/lib/systemd/system/prometheus.service
%endif
/usr/bin/prometheus
/usr/bin/promtool
%config(noreplace) /etc/prometheus/prometheus.yaml
%config(noreplace) /etc/prometheus/prometheus.rules
%config(noreplace) /etc/sysconfig/prometheus
%attr(755, prometheus, prometheus)/var/lib/prometheus
/var/run/prometheus
/var/log/prometheus
