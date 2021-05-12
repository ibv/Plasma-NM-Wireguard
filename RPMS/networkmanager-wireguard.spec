%define nmversion	%(echo %{version} | cut -d "." -f -2)
%define url_ver		%(echo %{version}|cut -d. -f1,2)

# filter out plugin .so provides
%global __provides_exclude_from	%{_libdir}/NetworkManager/.*\\.so

Summary:	NetworkManager VPN integration for Wireguard
Name:		networkmanager-wireguard
Epoch:		1
Version:	1.2.6
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Base
URL:		https://wiki.gnome.org/Projects/NetworkManager
Source:		https://download.gnome.org/sources/NetworkManager-openvpn/%{url_ver}/NetworkManager-wireguard-%{version}.tar.xz

BuildRequires:	pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) > 2.91.4
BuildRequires:	pkgconfig(libnma) >= %{nmversion}
BuildRequires:	pkgconfig(libxml-2.0)
#BuildRequires:	pkgconfig(openconnect)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	intltool
BuildRequires:	gettext
#Requires:	openvpn >= 2.1

%description
This package contains software for integrating the Wireguard VPN software
with NetworkManager.

%prep
%autosetup -p1 -n NetworkManager-wireguard-%{version}

%build
./autogen.sh
%configure \
    --disable-static \
    --with-dist-version="%product_distribution %product_version" \
    --without-libnm-glib
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%find_lang NetworkManager-wireguard

%pre
%_pre_useradd nm-wireguard %{_localstatedir}/lib/wireguard /bin/false

%files -f NetworkManager-wireguard.lang
%doc AUTHORS COPYING README.md
%{_libdir}/NetworkManager/libnm-vpn-plugin-wireguard.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-wireguard-editor.so
%{_usr}/lib/NetworkManager/VPN/nm-wireguard-service.name
%{_libexecdir}/nm-wireguard-auth-dialog
%{_libexecdir}/nm-wireguard-service
#%{_libexecdir}/nm-wireguard-service-wireguard-helper
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-wireguard-service.conf
%{_datadir}/appdata/network-manager-wireguard.metainfo.xml
# For now disabled in upstream
#{_datadir}/applications/nm-openvpn.desktop
#{_datadir}/icons/hicolor/*/apps/*


%changelog
* Fri Mar 06 2020 ovitters <ovitters> 1:1.8.12-1.mga8
+ Revision: 1554467
- new version 1.8.12

* Sat Feb 15 2020 umeabot <umeabot> 1:1.8.10-3.mga8
+ Revision: 1527990
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x

* Fri Aug 02 2019 wally <wally> 1:1.8.10-2.mga8
+ Revision: 1426924
- build without legacy libnm-glib

* Fri Feb 08 2019 ovitters <ovitters> 1:1.8.10-1.mga7
+ Revision: 1364283
- new version 1.8.10

* Wed Oct 17 2018 ovitters <ovitters> 1:1.8.8-1.mga7
+ Revision: 1321495
- new version 1.8.8

* Tue Oct 02 2018 ovitters <ovitters> 1:1.8.6-1.mga7
+ Revision: 1314594
- new version 1.8.6

* Sun Sep 23 2018 umeabot <umeabot> 1:1.8.4-2.mga7
+ Revision: 1299726
- Mageia 7 Mass Rebuild

* Sun Jul 01 2018 guillomovitch <guillomovitch> 1:1.8.4-1.mga7
+ Revision: 1241034
- new version 1.8.4

* Tue Mar 13 2018 tv <tv> 1:1.8.2-1.mga7
+ Revision: 1209031
- fix filelist
+ ovitters <ovitters>
- new version 1.8.2

* Wed May 17 2017 ovitters <ovitters> 1:1.2.10-1.mga6
+ Revision: 1102476
- new version 1.2.10

* Wed Mar 22 2017 ovitters <ovitters> 1:1.2.8-1.mga6
+ Revision: 1094319
- new version 1.2.8

* Sun Feb 19 2017 ovitters <ovitters> 1:1.2.6-1.mga6
+ Revision: 1086915
- new version 1.2.6
- drop upstream patch 0002-build-use-DL_LIBS-name-for-ldl.patch
- drop upstream patch 0001-build-fix-linking-libnm-vpn-plugin-openvpn.la-for-dlopen.patch

* Sat Oct 08 2016 daviddavid <daviddavid> 1:1.2.4-1.mga6
+ Revision: 1059700
- actually apply patches
- filter out 'plugin' .so provides
+ ovitters <ovitters>
- add patches to fix linking
- new version 1.2.4

* Wed Jun 15 2016 guillomovitch <guillomovitch> 1:1.2.2-2.mga6
+ Revision: 1021508
- create system account at installation

* Thu May 26 2016 ovitters <ovitters> 1:1.2.2-1.mga6
+ Revision: 1018686
- new version 1.2.2

* Thu Apr 21 2016 ovitters <ovitters> 1:1.2.0-1.mga6
+ Revision: 1003913
- new version 1.2.0

* Tue Apr 05 2016 ovitters <ovitters> 1:1.1.93-1.mga6
+ Revision: 998799
- new version 1.1.93

* Tue Mar 29 2016 ovitters <ovitters> 1:1.1.92-1.mga6
+ Revision: 996332
- new version 1.1.92
- update description

* Tue Mar 01 2016 ovitters <ovitters> 1:1.1.91-1.mga6
+ Revision: 981545
- new version 1.1.91

* Thu Feb 11 2016 ovitters <ovitters> 1:1.1.90-1.mga6
+ Revision: 955857
- new version 1.1.90

* Fri Nov 20 2015 ovitters <ovitters> 1:1.0.8-1.mga6
+ Revision: 904519
- new version 1.0.8

* Thu Aug 27 2015 ovitters <ovitters> 1:1.0.6-1.mga6
+ Revision: 870232
- new version 1.0.6

* Mon May 11 2015 tmb <tmb> 1:1.0.2-2.mga5
+ Revision: 821743
- submit to release

* Fri May 08 2015 tmb <tmb> 1:1.0.2-1.mga5
+ Revision: 821481
- update to 1.0.2

* Thu Feb 05 2015 ovitters <ovitters> 1:1.0.0-1.mga5
+ Revision: 813583
- new version 1.0.0
- fix source url

* Wed Oct 15 2014 umeabot <umeabot> 1:0.9.10.0-3.mga5
+ Revision: 739795
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 1:0.9.10.0-2.mga5
+ Revision: 682870
- Mageia 5 Mass Rebuild

* Wed Jul 09 2014 ovitters <ovitters> 1:0.9.10.0-1.mga5
+ Revision: 650809
- new version 0.9.10.0

* Fri Jul 04 2014 ovitters <ovitters> 1:0.9.8.4-3.mga5
+ Revision: 643126
- update url

* Sat Oct 19 2013 umeabot <umeabot> 1:0.9.8.4-2.mga4
+ Revision: 534674
- Mageia 4 Mass Rebuild

* Fri Sep 13 2013 ovitters <ovitters> 1:0.9.8.4-1.mga4
+ Revision: 478586
- new version 0.9.8.4

* Fri Jun 07 2013 ovitters <ovitters> 1:0.9.8.2-1.mga4
+ Revision: 440342
- new version 0.9.8.2

* Wed Feb 20 2013 ovitters <ovitters> 1:0.9.8.0-1.mga3
+ Revision: 399585
- new version 0.9.8.0
- new version 0.9.6.0
+ umeabot <umeabot>
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Fri Jun 29 2012 ovitters <ovitters> 1:0.9.5.95-1.mga3
+ Revision: 264823
- new version 0.9.5.95

* Sat Mar 24 2012 ovitters <ovitters> 1:0.9.4.0-1.mga2
+ Revision: 225994
- new version 0.9.4.0

* Fri Mar 02 2012 ovitters <ovitters> 1:0.9.3.995-1.mga2
+ Revision: 216881
- new version 0.9.3.995
+ guillomovitch <guillomovitch>
- spec cleanup

* Sat Nov 12 2011 fwang <fwang> 1:0.9.2.0-1.mga2
+ Revision: 166902
- disable warnings
- new version 0.9.2.0
+ mikala <mikala>
- Update tarball to 0.9.0
- use xz tarball

* Tue Jun 14 2011 mikala <mikala> 1:0.8.999-1.mga2
+ Revision: 106272
- Update tarball to 0.8.999
- Fix BuildRequires

* Thu Apr 21 2011 mikala <mikala> 1:0.8.4-1.mga1
+ Revision: 89451
- Update tarball to 0.8.4

* Thu Apr 14 2011 mikala <mikala> 1:0.8.3.995-2.mga1
+ Revision: 85421
- Rebuild for missing i586 binaries

* Thu Apr 14 2011 mikala <mikala> 1:0.8.3.995-1.mga1
+ Revision: 85254
- Update tarball

* Tue Mar 29 2011 mikala <mikala> 1:0.8.2-1.mga1
+ Revision: 78818
- Remove Requires(post) & Requires(postun)
- imported package networkmanager-openvpn

