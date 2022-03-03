Summary:	Manage desktop session autostarts
Name:		lxsession-edit
Version:	0.2.0
Release:	8
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://wiki.lxde.org/en/LXSession_Edit
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXSession Edit is the standard session edit manager used by LXDE. LXSession
Lite supports the autostart freedesktop.org specs. However, autostart spec
is a term for developers and it’s meaningless for end users. Basically, it
provides a way to automatically start some applications after login. Now
this can (partially) be configured through a simple GUI - LXSession Edit.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_install

%install
%makei_nstall

# locales
%find_lang %{name}

