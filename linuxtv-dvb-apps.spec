# TODO: devel and static subpackages, alevt, package test apps (test/* and dst-utils/dst_test)?
Summary:	DVB apps
Summary(pl.UTF-8):	Aplikacje dla DVB
Name:		linuxtv-dvb-apps
Version:	1.1.1.20111105
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://linuxtv.org/hg/dvb-apps/archive/tip.tar.gz
# Source0-md5:	ff01d8d48f70c258ecd5a7f1485a61c2
URL:		http://linuxtv.org/
BuildRequires:	libusb-devel
BuildRequires:	linux-libc-headers >= 2.6.31
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small number of DVB test and utility programs, including szap and
dvbscan. Specifically, the utilities are geared towards the initial
setup, testing, and operation of a DVB device, whether it be of the
software decoding (a.k.a. 'budget') or hardware decoding (a.k.a.
'premium' or 'full-featured') class.

%description -l pl.UTF-8
Aplikacje dla DVB.

%package libs
Summary:	linuxtv DVB libraries
Group:		Libraries

%description libs
DVB libraries from linuxtv.

%prep
%setup -q -n dvb-apps-d4e8bf5658ce
%{__mv} lib/libesg/TODO TODO.libesg
%{__mv} test/README README.test
for i in atsc_epg av7110_loadkeys scan szap ttusb_dec_reset; do
%{__mv} util/$i/README README.$i
done

%build
%{__make} \
	CFLAGS="-g -Wall -W -Wshadow -Wpointer-arith -Wstrict-prototypes %{rpmcflags}" \
	ttusb_dec_reset=1 \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lib/libdvbcfg/zapchannel.txt util/dib3000-watch/README.dib3000-watch util/dvbnet/net_start* util/szap/channels.conf/* README* TODO.libesg
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dvb

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
