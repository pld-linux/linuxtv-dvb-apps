# TODO: optflags
Summary:	DVB apps
Summary(pl.UTF-8):	Aplikacje dla DVB
Name:		linuxtv-dvb-apps
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.linuxtv.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	de958cdb8d00e74792dd69f3c945b037
URL:		http://linuxtv.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_utils	av7110_loadkeys dvbdate dvbnet dvbtraffic lib scan szap

%description
DVB apps.

%description -l pl.UTF-8
Aplikacje dla DVB.

%prep
%setup -q

%build
cd util
for i in %{_utils}; do
	%{__make} -C $i
done
cd ..
mv util/av7110_loadkeys/README README.av7110_loadkeys
mv util/scan/README README.scan
mv util/szap/README README.szap

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install util/av7110_loadkeys/av7110_loadkeys $RPM_BUILD_ROOT%{_bindir}
install util/av7110_loadkeys/evtest $RPM_BUILD_ROOT%{_bindir}
install util/dvbdate/dvbdate $RPM_BUILD_ROOT%{_bindir}
install util/dvbnet/dvbnet $RPM_BUILD_ROOT%{_bindir}
install util/dvbtraffic/dvbtraffic $RPM_BUILD_ROOT%{_bindir}
install util/lib/lnb.o $RPM_BUILD_ROOT%{_libdir}
install util/scan/scan $RPM_BUILD_ROOT%{_bindir}
install util/szap/azap $RPM_BUILD_ROOT%{_bindir}
install util/szap/czap $RPM_BUILD_ROOT%{_bindir}
install util/szap/femon $RPM_BUILD_ROOT%{_bindir}
install util/szap/szap $RPM_BUILD_ROOT%{_bindir}
install util/szap/tzap $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc util/av7110_loadkeys/*rc5 util/dvbnet/net_start* util/scan/dvb-*/ util/scan/atsc/ util/szap/channels.conf* README* TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lnb.o
