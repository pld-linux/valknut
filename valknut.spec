Summary:	dcgui-qt - QT Direct Connect client
Summary(pl):	dcgui-qt - klient Direct Connecta oparty o QT
Name:		dcgui-qt
Version:	0.2.18
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	73d9ef4848340a0c870641caec966a00
Source1:	%{name}.desktop
URL:		http://dc.ketelhot.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dclib-devel = %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	qt-devel >= 3.0.5
Requires:	dclib >= %{version}
Obsoletes:	dcgui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QT Direct Connect client.

%description -l pl
Klient Direct Connecta u¿ywaj±cy biblioteki QT.

%prep
%setup -q

%build
%configure \
	CPPFLAGS="-I%{_includedir}" \
	--enable-mt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dcgui
%{_datadir}/dcgui/emoticons
%dir %{_datadir}/dcgui/translation
%lang(cs) %{_datadir}/dcgui/translation/dcgui.cs.qm
%lang(da) %{_datadir}/dcgui/translation/dcgui.da.qm
%lang(de) %{_datadir}/dcgui/translation/dcgui.de.qm
%lang(en_GB) %{_datadir}/dcgui/translation/dcgui.en_GB.qm
%lang(es) %{_datadir}/dcgui/translation/dcgui.es.qm
%lang(fi) %{_datadir}/dcgui/translation/dcgui.fi.qm
%lang(fr) %{_datadir}/dcgui/translation/dcgui.fr.qm
%lang(hu) %{_datadir}/dcgui/translation/dcgui.hu.qm
%lang(is) %{_datadir}/dcgui/translation/dcgui.is.qm
%lang(it) %{_datadir}/dcgui/translation/dcgui.it.qm
%lang(no) %{_datadir}/dcgui/translation/dcgui.nb.qm
%lang(nl) %{_datadir}/dcgui/translation/dcgui.nl.qm
%lang(pl) %{_datadir}/dcgui/translation/dcgui.pl.qm
%lang(ro) %{_datadir}/dcgui/translation/dcgui.ro.qm
%lang(sv) %{_datadir}/dcgui/translation/dcgui.sv.qm
%lang(sk) %{_datadir}/dcgui/translation/dcgui.sk.qm
%lang(lv) %{_datadir}/dcgui/translation/dcgui.lv.qm
%{_applnkdir}/Network/Communications/%{name}.desktop
