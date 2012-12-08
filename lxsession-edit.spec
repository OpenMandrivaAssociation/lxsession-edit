Summary:	Manage desktop session autostarts
Name:     	lxsession-edit
Version:	0.2.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	intltool

%description
lxsession-edit is a tool used to manage desktop session autostarts,
especially for lxsession lite.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop


%changelog
* Tue Aug 02 2011 Александр Казанцев <kazancas@mandriva.org> 0.2.0-1mdv2012.0
+ Revision: 692771
- update to 0.2.0

* Fri Jul 10 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 394050
- new version 0.1.1

* Fri Dec 05 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.1
+ Revision: 310149
- import lxsession-edit


