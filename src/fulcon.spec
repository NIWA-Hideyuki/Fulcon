# spec file for fulcon

Summary:               Generate the full container and management it
License:               Apache 2.0
Name:                  fulcon
Version:               0.3
Release:               1%{?dist}
Source:                fulcon-%{?version}.tar.gz
URL:                   https://github.com/NIWA-Hideyuki/Fulcon
Requires:              python-IPy

%description

`Fulcon` is the CLI tool for Full Container System

In Fulcon, the container can be handled like VM.
Fulcon constructs the system by generating the container, logging in
from the console, and installing the package with yum and apt, and stops
the system with shutdown command.The container can be connected directly with
the Internet by adding virtual NIC.
Fulcon can handle CentOS 7 and Ubuntu 15.04

%prep
%setup -q

%build
make %{?_smp_mflags} libdir=%{_prefix}/lib

%install
make install libdir=%{_prefix}/lib DESTDIR=$RPM_BUILD_ROOT

%files
%{_sbindir}/fulcon
%{_prefix}/lib/fulcon
%{_localstatedir}/lib/fulcon

%changelog
* Sun Feb 29 2016 NIWA Hideyuki <niwa.niwa@nifty.ne.jp>
- New release 0.2
* Thu Jan 14 2016 NIWA Hideyuki <niwa.niwa@nifty.ne.jp>
- New Build. First release 0.1

