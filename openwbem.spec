Summary:	The OpenWBEM CIMOM
Summary(pl.UTF-8):	CIMOM z projektu OpenWBEM
Name:		openwbem
Version:	3.2.2
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/openwbem/%{name}-%{version}.tar.gz
# Source0-md5:	4a70352af90d4024afc9f740e8cf7b23
Patch0:		%{name}-include.patch
Patch1:		%{name}-g++.patch
Patch2:		%{name}-am.patch
URL:		http://openwbem.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libstdc++-devel >= 5:3.1
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib
# plugin using symbols from its loader
%define		skip_post_check_so	libowslpprovider\.so.*
%description
OpenWBEM is a set of software components that help facilitate the
deployment of the DMTF's (Distributed Management Task Force) CIM/WBEM
technologies (<http://www.dmtf.org/>). This software was initially
developed by Caldera International and released to the opensource
community under a BSD style license for further maturation and
additional platform support. On initial release, all of the software
components were written in C++. It's expected to change as the
project evolves and developers add more components to the suite.

%description -l pl.UTF-8
OpenWBEM to zestaw komponentów oprogramowania pomagającego przy
wdrażaniu technologii CIM/WBEM tworzonej przez DMTF (Distributed
Management Task Force: <http://www.dmtf.org/>). Oprogramowanie to
było pierwotnie tworzone przez firmę Caldera International i wydane
wraz z otwartymi źródłami na licencji typu BSD do dalszego rozwoju i
wspierania dodatkowych platform. W pierwszym wydaniu wszystkie
komponenty zostały napisane w C++; to może sie zmienić wraz z ewolucją
projektu i dodawaniem przez programistów większej liczby komponentów.

%package libs
Summary:	OpenWBEM libraries
Summary(pl.UTF-8):	Biblioteki OpenWBEM
Group:		Libraries

%description libs
OpenWBEM libraries.

%description libs -l pl.UTF-8
Biblioteki OpenWBEM.

%package devel
Summary:	Header files for OpenWBEM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OpenWBEM
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for OpenWBEM libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OpenWBEM.

%package static
Summary:	Static OpenWBEM libraries
Summary(pl.UTF-8):	Biblioteki statyczne OpenWBEM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenWBEM libraries.

%description static -l pl.UTF-8
Biblioteki statyczne OpenWBEM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# don't override
%{__sed} -i -e 's/"-O3"/""/' configure.in

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README TODO
%attr(755,root,root) %{_bindir}/ow*
%attr(755,root,root) %{_sbindir}/owcimomd
%attr(755,root,root) %{_sbindir}/owdigestgenpass
%attr(755,root,root) %{_sbindir}/owprovideragent
%attr(755,root,root) %{_sbindir}/owrepositorydump
# TODO: PLDify, move to /etc/rc.d/init.d
%attr(755,root,root) %{_sbindir}/owcimomd_init
%dir %{_sysconfdir}/openwbem
%dir %{_sysconfdir}/openwbem/openwbem.conf.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openwbem/openwbem.conf
%attr(754,root,root) %{_sysconfdir}/openwbem/owgencert
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openwbem/ssleay.cnf
%attr(755,root,root) %{_libdir}/openwbem/OW_PAMAuth
%attr(755,root,root) %{_libdir}/openwbem/owlocalhelper
%attr(755,root,root) %{_libdir}/openwbem/libowindicationreplayer.so*
%attr(755,root,root) %{_libdir}/openwbem/libowindicationserver.so*
%attr(755,root,root) %{_libdir}/openwbem/libowsimpleauthorizer.so*
%attr(755,root,root) %{_libdir}/openwbem/libowsimpleauthorizer2.so*
%attr(755,root,root) %{_libdir}/openwbem/authentication/libnonauthenticatingauthentication.so
%attr(755,root,root) %{_libdir}/openwbem/authentication/libpamauthentication.so
%attr(755,root,root) %{_libdir}/openwbem/authentication/libpamclauthentication.so
%attr(755,root,root) %{_libdir}/openwbem/authentication/libsimpleauthentication.so
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libcppindicationexportxmlhttpprovider.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovCIM_IndicationSubscription.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovindIndicationRepLayer.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstCIM_IndicationFilter.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstCIM_Namespace.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstCIM_NamespaceInManager.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstOW_NameSpace.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstOpenWBEM_ConfigSettingData.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstOpenWBEM_ObjectManager.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovinstOpenWBEM_UnitaryComputerSystem.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowprovpollUnloader.so*
%attr(755,root,root) %{_libdir}/openwbem/c++providers/libowslpprovider.so*
%attr(755,root,root) %{_libdir}/openwbem/provifcs/libcmpiprovifc.so*
%attr(755,root,root) %{_libdir}/openwbem/provifcs/libnpiprovifc.so*
%attr(755,root,root) %{_libdir}/openwbem/provifcs/libowremoteprovifc.so*
%attr(755,root,root) %{_libdir}/openwbem/requesthandlers/libowrequesthandlerbinary.so
%attr(755,root,root) %{_libdir}/openwbem/requesthandlers/libowrequesthandlercimxml.so
%attr(755,root,root) %{_libdir}/openwbem/services/libowservicehttp.so
%dir %{_localstatedir}/openwbem

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpisupport.so.4
%attr(755,root,root) %{_libdir}/libnonauthenticatingauthentication.so.4
%attr(755,root,root) %{_libdir}/libnpisupport.so.4
%attr(755,root,root) %{_libdir}/libopenwbem.so.4
%attr(755,root,root) %{_libdir}/libowcimomcommon.so.4
%attr(755,root,root) %{_libdir}/libowcimxmllistener.so.4
%attr(755,root,root) %{_libdir}/libowclient.so.4
%attr(755,root,root) %{_libdir}/libowcppprovifc.so.4
%attr(755,root,root) %{_libdir}/libowdb.so.4
%attr(755,root,root) %{_libdir}/libowembeddedcimom.so.4
%attr(755,root,root) %{_libdir}/libowhttpclient.so.4
%attr(755,root,root) %{_libdir}/libowhttpcommon.so.4
%attr(755,root,root) %{_libdir}/libowhttpxmllistener.so.4
%attr(755,root,root) %{_libdir}/libowmofc.so.4
%attr(755,root,root) %{_libdir}/libowprovider.so.4
%attr(755,root,root) %{_libdir}/libowprovideragent.so.4
%attr(755,root,root) %{_libdir}/libowrepositoryhdb.so.4
%attr(755,root,root) %{_libdir}/libowrequesthandlerbinary.so.4
%attr(755,root,root) %{_libdir}/libowrequesthandlercimxml.so.4
%attr(755,root,root) %{_libdir}/libowserver.so.4
%attr(755,root,root) %{_libdir}/libowservicehttp.so.4
%attr(755,root,root) %{_libdir}/libowwql.so.4
%attr(755,root,root) %{_libdir}/libowwqlcommon.so.4
%attr(755,root,root) %{_libdir}/libowxml.so.4
%attr(755,root,root) %{_libdir}/libpamauthentication.so.4
%attr(755,root,root) %{_libdir}/libpamclauthentication.so.4
%attr(755,root,root) %{_libdir}/libsimpleauthentication.so.4
# symlinks to libs referred as plugins (through symlinks in %{_libdir}/openwbem subdirs)
%attr(755,root,root) %{_libdir}/libnonauthenticatingauthentication.so
%attr(755,root,root) %{_libdir}/libpamauthentication.so
%attr(755,root,root) %{_libdir}/libpamclauthentication.so
%attr(755,root,root) %{_libdir}/libsimpleauthentication.so
%attr(755,root,root) %{_libdir}/libowrequesthandlerbinary.so
%attr(755,root,root) %{_libdir}/libowrequesthandlercimxml.so
%attr(755,root,root) %{_libdir}/libowservicehttp.so
%dir %{_libdir}/openwbem
%dir %{_libdir}/openwbem/authentication
%dir %{_libdir}/openwbem/c++providers
%dir %{_libdir}/openwbem/provifcs
%dir %{_libdir}/openwbem/requesthandlers
%dir %{_libdir}/openwbem/services
%{_datadir}/openwbem
%{_mandir}/man1/ow*.1*
%{_mandir}/man8/owcimomd.8*
%{_mandir}/man8/owdigestgenpass.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpisupport.so
%attr(755,root,root) %{_libdir}/libnpisupport.so
%attr(755,root,root) %{_libdir}/libopenwbem.so
%attr(755,root,root) %{_libdir}/libowcimomcommon.so
%attr(755,root,root) %{_libdir}/libowcimxmllistener.so
%attr(755,root,root) %{_libdir}/libowclient.so
%attr(755,root,root) %{_libdir}/libowcppprovifc.so
%attr(755,root,root) %{_libdir}/libowdb.so
%attr(755,root,root) %{_libdir}/libowembeddedcimom.so
%attr(755,root,root) %{_libdir}/libowhttpclient.so
%attr(755,root,root) %{_libdir}/libowhttpcommon.so
%attr(755,root,root) %{_libdir}/libowhttpxmllistener.so
%attr(755,root,root) %{_libdir}/libowmofc.so
%attr(755,root,root) %{_libdir}/libowprovider.so
%attr(755,root,root) %{_libdir}/libowprovideragent.so
%attr(755,root,root) %{_libdir}/libowrepositoryhdb.so
%attr(755,root,root) %{_libdir}/libowserver.so
%attr(755,root,root) %{_libdir}/libowwql.so
%attr(755,root,root) %{_libdir}/libowwqlcommon.so
%attr(755,root,root) %{_libdir}/libowxml.so
%{_includedir}/openwbem
%{_aclocaldir}/openwbem.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libcmpisupport.a
%{_libdir}/libnpisupport.a
%{_libdir}/libopenwbem.a
%{_libdir}/libowcimomcommon.a
%{_libdir}/libowcimxmllistener.a
%{_libdir}/libowclient.a
%{_libdir}/libowcppprovifc.a
%{_libdir}/libowdb.a
%{_libdir}/libowembeddedcimom.a
%{_libdir}/libowhttpclient.a
%{_libdir}/libowhttpcommon.a
%{_libdir}/libowhttpxmllistener.a
%{_libdir}/libowmofc.a
%{_libdir}/libowprovider.a
%{_libdir}/libowprovideragent.a
%{_libdir}/libowrepositoryhdb.a
%{_libdir}/libowserver.a
%{_libdir}/libowservicehttp.a
%{_libdir}/libowwql.a
%{_libdir}/libowwqlcommon.a
%{_libdir}/libowxml.a
