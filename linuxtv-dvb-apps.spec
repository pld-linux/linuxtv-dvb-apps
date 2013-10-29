# TODO: package test apps (test/* and dst-utils/dst_test)?
Summary:	DVB apps
Summary(pl.UTF-8):	Aplikacje dla DVB
Name:		linuxtv-dvb-apps
Version:	1.1.1.20120210
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://linuxtv.org/hg/dvb-apps/archive/tip.tar.gz
# Source0-md5:	abe1e41a0bad0292e8af1740fa2c3195
Patch0:		%{name}-zlib.patch
URL:		http://linuxtv.org/
BuildRequires:	libpng-devel
BuildRequires:	libusb-compat-devel
BuildRequires:	linux-libc-headers >= 2.6.31
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zvbi-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small number of DVB test and utility programs, including szap and
dvbscan. Specifically, the utilities are geared towards the initial
setup, testing, and operation of a DVB device, whether it be of the
software decoding (a.k.a. 'budget') or hardware decoding (a.k.a.
'premium' or 'full-featured') class.

%description -l pl.UTF-8
Kilka programów testowych i narzędziowych do DVB, w tym szap i
dvbscan. Narzędzia są w szczególności przeznaczone do początkowej
konfiguracji, testowania i obsługi urządzeń DVB, zarówno tych z
dekodowaniem programowym ("niskobudżetowych"), jak i dekodowaniem
sprzętowym ("klasy premium", "w pełni funkcjonalnych").

%package libs
Summary:	linuxtv DVB libraries
Summary(pl.UTF-8):	Biblioteki DVB z projektu linuxtv
Group:		Libraries

%description libs
DVB libraries from linuxtv.

%description libs -l pl.UTF-8
Biblioteki DVB z projektu linuxtv.

%package devel
Summary:	Header files for linuxtv DVB libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek DVB z projektu linuxtv
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for linuxtv DVB libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek DVB z projektu linuxtv.

%package static
Summary:	Static linuxtv DVB libraries
Summary(pl.UTF-8):	Statyczne biblioteki DVB z projektu linuxtv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static linuxtv DVB libraries.

%description static -l pl.UTF-8
Statyczne biblioteki DVB z projektu linuxtv.

%prep
%setup -q -n dvb-apps-69fc03702a64
%patch0 -p1

# prepare %doc
%{__mv} lib/libesg/TODO TODO.libesg
%{__mv} test/README README.test
for i in atsc_epg av7110_loadkeys scan szap ttusb_dec_reset; do
%{__mv} util/$i/README README.$i
done
%{__mkdir} alevt
%{__mv} util/alevt/{ChangeLog,EXPORT.HOWTO,README,README.OLD,ReadmeGR,TODO} alevt

touch util/alevt/alevt.png

%build
export CFLAGS="-g -Wall -W -Wshadow -Wpointer-arith -Wstrict-prototypes %{rpmcflags}"
%{__make} \
	ttusb_dec_reset=1 \
	V=1

%{__make} -C util/alevt \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1}

%{__make} install \
	libdir="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C util/alevt \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc alevt lib/libdvbcfg/zapchannel.txt util/dib3000-watch/README.dib3000-watch util/dvbnet/net_start* util/szap/channels-conf README* TODO.libesg
%attr(755,root,root) %{_bindir}/alevt
%attr(755,root,root) %{_bindir}/alevt-cap
%attr(755,root,root) %{_bindir}/alevt-date
%attr(755,root,root) %{_bindir}/atsc_epg
%attr(755,root,root) %{_bindir}/av7110_loadkeys
%attr(755,root,root) %{_bindir}/azap
%attr(755,root,root) %{_bindir}/czap
%attr(755,root,root) %{_bindir}/dib3000-watch
%attr(755,root,root) %{_bindir}/dst_test
%attr(755,root,root) %{_bindir}/dvbdate
%attr(755,root,root) %{_bindir}/dvbnet
%attr(755,root,root) %{_bindir}/dvbscan
%attr(755,root,root) %{_bindir}/dvbtraffic
%attr(755,root,root) %{_bindir}/femon
%attr(755,root,root) %{_bindir}/gnutv
%attr(755,root,root) %{_bindir}/gotox
%attr(755,root,root) %{_bindir}/lsdvb
%attr(755,root,root) %{_bindir}/scan
%attr(755,root,root) %{_bindir}/szap
%attr(755,root,root) %{_bindir}/ttusb_dec_reset
%attr(755,root,root) %{_bindir}/tzap
%attr(755,root,root) %{_bindir}/zap
%{_datadir}/dvb
%{_desktopdir}/alevt.desktop
%{_pixmapsdir}/alevt.png
%{_mandir}/man1/alevt*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvbapi.so
%attr(755,root,root) %{_libdir}/libdvbcfg.so
%attr(755,root,root) %{_libdir}/libdvben50221.so
%attr(755,root,root) %{_libdir}/libdvbsec.so
%attr(755,root,root) %{_libdir}/libesg.so
%attr(755,root,root) %{_libdir}/libucsi.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/libdvbapi
%{_includedir}/libdvbcfg
%{_includedir}/libdvben50221
%{_includedir}/libdvbsec
%{_includedir}/libesg
%{_includedir}/libucsi

%files static
%defattr(644,root,root,755)
%{_libdir}/libdvbapi.a
%{_libdir}/libdvbcfg.a
%{_libdir}/libdvben50221.a
%{_libdir}/libdvbsec.a
%{_libdir}/libesg.a
%{_libdir}/libucsi.a
