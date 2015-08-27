# spec file for fulcon

Summary:               Generate the full container and management it
License:               Apache 2.0
Name:                  fulcon
Version:               0.1
Release:               1%{?dist}
Source0:               https://github.com/NIWA-Hideyuki/Fulcon.git
URL:                   https://github.com/NIWA-Hideyuki/Fulcon
Requires:              python-IPy

%description
fulcon efficiently makes the container. One container making is a second 
or less.
The fulcon container can dynamically change the resource of CPU, MEMORY,
IO and NET. 
fulcon can be used as well as VM.
fulcon can be operated stabilizing the job like a past system at a long term.
Moreover, a lot of fulcon instances are generate in a short time. If a lot
of fulcon instances become unnecessary, it is possible to delete it
collectively. 

%prep
%setup -q

%build
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
