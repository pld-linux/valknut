Summary:	valknut - QT Direct Connect client
Summary(pl.UTF-8):	valknut - klient Direct Connecta oparty o QT
Name:		valknut
Version:	0.4.9
%define		dclib_ver	1:0.3.23
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	c25d68c447cb9deb4262befdde9fccea
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://wxdcgui.sourceforge.net/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	dclib-devel = %{dclib_ver}
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
Requires:	dclib = %{dclib_ver}
Obsoletes:	dcgui
Obsoletes:	dcgui-qt <= 0.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QT Direct Connect client.

%description -l pl.UTF-8
Klient Direct Connecta używający biblioteki QT.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--enable-mt \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/translation/%{name}.pt_{br,BR}.qm

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/sounds
%dir %{_datadir}/%{name}/translation
%lang(bs) %{_datadir}/%{name}/translation/%{name}.bs.qm
%lang(cs) %{_datadir}/%{name}/translation/%{name}.cs.qm
%lang(da) %{_datadir}/%{name}/translation/%{name}.da.qm
%lang(de) %{_datadir}/%{name}/translation/%{name}.de.qm
%lang(en_GB) %{_datadir}/%{name}/translation/%{name}.en_GB.qm
%lang(el) %{_datadir}/%{name}/translation/%{name}.el.qm
%lang(es) %{_datadir}/%{name}/translation/%{name}.es.qm
%lang(fi) %{_datadir}/%{name}/translation/%{name}.fi.qm
%lang(fr) %{_datadir}/%{name}/translation/%{name}.fr.qm
%lang(hu) %{_datadir}/%{name}/translation/%{name}.hu.qm
%lang(is) %{_datadir}/%{name}/translation/%{name}.is.qm
%lang(it) %{_datadir}/%{name}/translation/%{name}.it.qm
%lang(nb) %{_datadir}/%{name}/translation/%{name}.nb.qm
%lang(nl) %{_datadir}/%{name}/translation/%{name}.nl.qm
%lang(pl) %{_datadir}/%{name}/translation/%{name}.pl.qm
%lang(pt_BR) %{_datadir}/%{name}/translation/%{name}.pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translation/%{name}.ro.qm
%lang(ru) %{_datadir}/%{name}/translation/%{name}.rus.qm
%lang(sv) %{_datadir}/%{name}/translation/%{name}.sv.qm
%lang(sk) %{_datadir}/%{name}/translation/%{name}.sk.qm
%lang(sr) %{_datadir}/%{name}/translation/%{name}.sr.qm
%lang(lv) %{_datadir}/%{name}/translation/%{name}.lv.qm
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/valknut.png
%{_mandir}/man1/*.1*
