Summary:	Manage desktop session autostarts
Name:		lxsession-edit
Version:	0.2.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description
lxsession-edit is a tool used to manage desktop session autostarts,
especially for lxsession lite.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop

