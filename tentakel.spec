%define name tentakel
%define version 2.2
%define release 9

Summary: Program that executes the same command on many hosts in parallel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: tentakel-setup.py.patch
License: GPL
Group: Networking/Remote access
Url: https://tentakel.biskalar.de/
Buildarch: noarch
requires: python
Buildrequires: python-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Tentakel is a program that executes the same command on many hosts in parallel 
using SSH. It is designed to be easily extendable. The output of the remote 
command can be controlled by means of format strings.

%prep
%setup -q
%patch0 -p0

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%make PREFIX=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%name
%dir %py_puresitedir/lekatnet
%py_puresitedir/lekatnet/*.py*
%dir %py_puresitedir/lekatnet/plugins
%py_puresitedir/lekatnet/plugins/*
%py_puresitedir/tentakel-*.egg-info
%{_mandir}/man1/tentakel.*
%{_defaultdocdir}/%name/*


%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 2.2-8mdv2011.0
+ Revision: 592185
- rebuild for python 2.7

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 2.2-7mdv2010.1
+ Revision: 497257
- fix to be able to rebuild on 2010.1
- use macro for doc

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Tue Mar 11 2008 Antoine Ginies <aginies@mandriva.com> 2.2-4mdv2008.1
+ Revision: 185610
- fix missing doc
- re-add buildroot
- remove buildroot

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request
    - fix man pages extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Mar 02 2007 Antoine Ginies <aginies@mandriva.com> 2.2-3mdv2007.0
+ Revision: 130992
- use %%py_puresitedir instead of %%py_platsitedir (thx misc help)
- add .egg-info

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild against new python
    - Import tentakel

* Mon Feb 27 2006 Antoine Ginies <aginies@mandriva.com> 2.2-2mdk
- add Buildrequires on python-devel

* Tue Mar 22 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 2.2-1mdk
- release 2.2

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 2.1.2-3mdk
- Rebuild for new python

* Sat May 29 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 2.1.2-1mdk
- first Mandrakesoft release

