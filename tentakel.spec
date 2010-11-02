%define name tentakel
%define version 2.2
%define release %mkrel 8

Summary: Program that executes the same command on many hosts in parallel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: tentakel-setup.py.patch
License: GPL
Group: Networking/Remote access
Url: http://tentakel.biskalar.de/
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
