%define orgname 	korners

Summary:	korners
Name:		kde4-kdegames-korners
Version:	0.8
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.kde-apps.org/CONTENT/content-files/113113-%{orgname}.tar.gz
# Source0-md5:	83e476d52d564901d116bab3007c3367
Source1:	%{name}.desktop
URL:		http://www.kde-apps.org/content/show.php/korners?content=113113
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdegames-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Korners is simple board game. Also known as Helma.

Featuring:
- lan multiplayer
- time game with highscores

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_desktopdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/%{_desktopdir}/%{orgname}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{orgname}
%{_datadir}/apps/%{orgname}
%{_datadir}/config.kcfg/%{orgname}.kcfg
%{_iconsdir}/*/*/*/%{orgname}.png
%{_desktopdir}/%{orgname}.desktop
