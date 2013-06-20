Summary:	Manage desktop session autostarts
Name:     	lxsession-edit
Version:	0.2.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRequires:	pkgconfig(gtk+-x11-2.0)
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

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
