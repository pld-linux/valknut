Summary:	dcgui-qt - QT Direct Connect client
Summary(pl):	dcgui-qt - klient Direct Connecta oparty o QT
Name:		dcgui-qt
Version:	0.3.2
Release:	4
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	079492b0ecf7cb680661a0009d5b15b3
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://dcgui.berlios.de/	
BuildRequires:	automake
BuildRequires:	dclib-devel = %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	bzip2-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	qt-linguist
Requires:	dclib = %{version}
Provides:	dcgui
Obsoletes:	dcgui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_desktopdir	%{_applnkdir}/Network/Communications

%description
QT Direct Connect client.

%description -l pl
Klient Direct Connecta u¿ywaj±cy biblioteki QT.

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

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dcgui
%{_datadir}/dcgui/icons
%{_datadir}/dcgui/sounds
%dir %{_datadir}/dcgui/translation
%lang(bs) %{_datadir}/dcgui/translation/dcgui.bs.qm
%lang(cs) %{_datadir}/dcgui/translation/dcgui.cs.qm
%lang(da) %{_datadir}/dcgui/translation/dcgui.da.qm
%lang(de) %{_datadir}/dcgui/translation/dcgui.de.qm
%lang(en_GB) %{_datadir}/dcgui/translation/dcgui.en_GB.qm
%lang(el) %{_datadir}/dcgui/translation/dcgui.el.qm
%lang(es) %{_datadir}/dcgui/translation/dcgui.es.qm
%lang(fi) %{_datadir}/dcgui/translation/dcgui.fi.qm
%lang(fr) %{_datadir}/dcgui/translation/dcgui.fr.qm
%lang(hu) %{_datadir}/dcgui/translation/dcgui.hu.qm
%lang(is) %{_datadir}/dcgui/translation/dcgui.is.qm
%lang(it) %{_datadir}/dcgui/translation/dcgui.it.qm
%lang(nb) %{_datadir}/dcgui/translation/dcgui.nb.qm
%lang(nl) %{_datadir}/dcgui/translation/dcgui.nl.qm
%lang(pl) %{_datadir}/dcgui/translation/dcgui.pl.qm
%lang(ro) %{_datadir}/dcgui/translation/dcgui.ro.qm
%lang(ru) %{_datadir}/dcgui/translation/dcgui.rus.qm
%lang(sv) %{_datadir}/dcgui/translation/dcgui.sv.qm
%lang(sk) %{_datadir}/dcgui/translation/dcgui.sk.qm
%lang(lv) %{_datadir}/dcgui/translation/dcgui.lv.qm
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
