# spec file for lxcf

Summary:               Generate the full container and management it
License:               Apache 2.0
Name:                  fulcon
Version:               0.1
Release:               1%{?dist}
Source0:               http://downloads.sourceforge.net/lxcfacility/source/%{name}-%{version}.tar.gz
URL:                   https://sourceforge.net/projects/lxcfacility/
Requires:              libvirt-daemon-driver-lxc
Requires:              python-IPy

%description
LXCF efficiently makes the instance. One-instance making is a few
minutes or less.
The LXCF instance can dynamically change the resource of CPU, MEMORY,
IO and NET. Even if the instance has stopped, the change in the resource
can be changed.
LXCF can be used by installing it on Linux on VM as well as bare metal.
LXCF can be operated stabilizing the job like a past system at a long term.
Moreover, a lot of LXCF instances are generate in a short time. If a lot
of LXCF instances become unnecessary, it is possible to delete it
collectively. Such stateless instance can be operated.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS ; export CFLAGS
LDFLAGS=$RPM_OPT_FLAGS ; export LDFLAGS
make %{?_smp_mflags} libdir=%_libdir

%install
make install libdir=%_libdir DESTDIR=$RPM_BUILD_ROOT

%preun
%systemd_preun libvirtd.service
%systemd_preun lxcf.service
%systemd_preun lxcf-sched.service
%systemd_preun lxcf-api.service

%post
systemctl restart libvirtd
%{_libdir}/lxcf/lxcf-init
%systemd_post lxcf.service
%systemd_post lxcf-sched.service
%systemd_post lxcf-api.service

%postun
systemctl restart libvirtd

%files
%{_sbindir}/lxcf
%{_libdir}/lxcf/
%config(noreplace) %{_sysconfdir}/lxcf/
%{_sysconfdir}/libvirt/hooks/lxc
%{_sysconfdir}/libvirt/hooks/qemu
%config(noreplace) %{_sysconfdir}/libvirt/qemu/networks/lxcfnet1.xml
%{_sysconfdir}/libvirt/qemu/networks/autostart/lxcfnet1.xml
%{_unitdir}/lxcf.service
%{_unitdir}/lxcf-sched.service
%{_unitdir}/lxcf-api.service
%{_var}/lib/libvirt/network/lxcfnet1.xml
%{_mandir}/man1/lxcf.1.gz
%{_defaultdocdir}/lxcf-%{version}/
%doc README COPYING ChangeLog AUTHORS example

%changelog
* Fri Nov 14 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.11-1
- New Build. update to release 0.11-1

* Thu Sep 25 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.10-1
- New Build. update to release 0.10-1

* Wed Jul 30 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.9-1
- New Build. update to release 0.9-1

* Fri Jul 4 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.8-1
- New Build. update to release 0.8-1

* Fri Jun 13 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.7-1
- New Build. update to release 0.7-1

* Sat May 24 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.6-1
- New Build. update to release 0.6-1

* Fri May 02 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.5-3
- Cleanup of specfile. update to release 0.5-3

* Thu Apr 17 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.5-2
- changelog of specfile is renewed. update to release 0.5-2

* Tue Apr 15 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.5-1
- New Build. update to release 0.5-1

* Wed Apr 02 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.4-1
- New Build. update to release 0.4-1

* Wed Feb 19 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.3-1
- New Build. update to release 0.3-1

* Sat Feb 08 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.2-1
- New Build. update to release 0.2-1

* Tue Feb 04 2014 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.1-3
- New Build. update to release 0.1-3

* Tue Dec 17 2013 NIWA Hideyuki <niwa.hideyuki@jp.fujitsu.com> - 0.1
- New Build. First release 0.1
