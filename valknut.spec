Summary:	dcgui-qt - QT Direct Connect client
Summary(pl):	dcgui-qt - klient Direct Connecta oparty o QT
Name:		dcgui-qt
Version:	0.2.13
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/dcgui/%{name}-%{version}.tar.bz2
# Source0-md5:	13e7d2d740b8ac6120ea004329b8ab91
Source1:	%{name}.desktop
URL:		http://dc.ketelhot.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dclib-devel = %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-devel > 2.0.0
BuildRequires:	qt-devel >= 3.0.5
Requires:	dclib >= %{version}
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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dcgui
%dir %{_datadir}/dcgui/emoticons
%dir %{_datadir}/dcgui/translation
%attr(644,root,root) %{_datadir}/dcgui/translation/*.qm
%attr(644,root,root) %{_datadir}/dcgui/emoticons/*
%{_applnkdir}/Network/Communications/%{name}.desktop
