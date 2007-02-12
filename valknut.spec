%define _snap   040521
Summary:	dcgui-qt - QT Direct Connect client
Summary(pl.UTF-8):   dcgui-qt - klient Direct Connecta oparty o QT
Name:		dcgui-qt
Version:	0.3
Release:	3
License:	GPL v2
Group:		X11/Applications/Networking
Source0:        http://dcgui.berlios.de/files/dcgui/snapshot/dc-source-alpha-snapshot.tar.gz
#Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	f2fd65496a2cc6149038e7b87a398beb
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://dcgui.berlios.de/	
BuildRequires:	automake
BuildRequires:	dclib-devel = %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	bzip2-devel
BuildRequires:	qt-devel >= 3.0.5
Requires:	dclib = %{version}
Provides:	dcgui
Obsoletes:	dcgui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QT Direct Connect client.

%description -l pl.UTF-8
Klient Direct Connecta używający biblioteki QT.

%prep
##%setup -q
if [ -d %{name}-%{version} ]; then
rm -rf %{name}-%{version}
fi
mkdir %{name}-%{version}
cd %{name}-%{version}
tar xfz %{SOURCE0} -C ./

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/dcgui
%{__make} -f Makefile.dist
cp -f /usr/share/automake/config.* admin
%configure \
	--enable-mt \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/%{name}-%{version}/dcgui

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
##%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dcgui
%{_datadir}/dcgui/emoticons
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
