# spec file for fulcon

Summary:               Generate the full container and management it
License:               Apache 2.0
Name:                  fulcon
Version:               0.1
Release:               1%{?dist}
Source0:               http://downloads.sourceforge.net/fulconacility/source/%{name}-%{version}.tar.gz
URL:                   https://github.com/NIWA-Hideyuki/Fulcon.git
Requires:              python-IPy

%description
fulcon efficiently makes the instance. One-instance making is a few
minutes or less.
The fulcon instance can dynamically change the resource of CPU, MEMORY,
IO and NET. Even if the instance has stopped, the change in the resource
can be changed.
fulcon can be used by installing it on Linux on VM as well as bare metal.
fulcon can be operated stabilizing the job like a past system at a long term.
Moreover, a lot of fulcon instances are generate in a short time. If a lot
of fulcon instances become unnecessary, it is possible to delete it
collectively. Such stateless instance can be operated.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS ; export CFLAGS
LDFLAGS=$RPM_OPT_FLAGS ; export LDFLAGS
make %{?_smp_mflags} libdir=%_libdir

%install
make install libdir=%_libdir DESTDIR=$RPM_BUILD_ROOT

%files
%{_sbindir}/fulcon
%{_libdir}/fulcon/
%{_mandir}/man1/fulcon.1.gz
%{_defaultdocdir}/fulcon-%{version}/
%doc README COPYING ChangeLog AUTHORS example

%changelog
* Tue Aug 23 2015 NIWA Hideyuki <niwa.niwa@nifty.ne.jp>
- New Build. First release 0.1
