#
# Please do not update/rebuild/touch this package before asking first
# to mikala and/or neoclust and/or daviddavid
# This package is part of the KDE Stack.
#

%define nm_version 1.0.4
%define pptp 1
%define openswan 0
%define openvn 1
%define vpnc 1
%define openconnect 1
%define l2tp 1
%define strongswan 0
%define wireguard 1

%define rel 1

Name:           plasma-nm
Summary:        Plasma 5 applet written in QML for managing network connections
Version: 	5.21.5
Release:        %mkrel %{rel}
Group:          Graphical desktop/KDE
License:        GPLv2 and LGPLv2+
URL:            https://www.kde.org/workspaces/plasmadesktop/
Source0:        https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz

# Upstream patches (100-200)

BuildRequires:  pkgconfig(libnm) >= %nm_version
BuildRequires:  pkgconfig(ModemManager)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(qca2-qt5)

BuildRequires:  kf5-macros

BuildRequires:  ki18n-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kservice-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kio-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kwallet-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  solid-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  knotifications-devel
BuildRequires:  plasma-framework-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kinit-devel
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Prison)

BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5UiTools)

%if %openconnect
BuildRequires:  pkgconfig(openconnect) >= 3.99
%endif

%rename plasma5-nm

%description
Plasma 5 applet written in QML for managing network connections.

#--------------------------------------------------------------------

%package -n plasma-applet-nm
Summary:        NetworkManager Plasma 5 applet
Group:          Graphical desktop/KDE
Requires:       networkmanager >= %nm_version
Requires:       kirigami2
Requires:       prison
Requires:       qca-qt5

%rename plasma5-applet-nm

# ease upgrade mga7->mga8
Conflicts:      plasma-applet-nm-openvpn < 5.18.5-2

%description -n plasma-applet-nm
Network Management Plasma 5 applet for controlling network
connections on systems that use the NetworkManager service.


%files -n plasma-applet-nm -f %name.lang
%_kf5_libdir/libplasmanm_editor.so
%_kf5_libdir/libplasmanm_internal.so
%_kf5_qmldir/org/kde/plasma/networkmanagement
%_kf5_plugindir/kded/networkmanagement.so
%_qt5_plugindir/kcm_networkmanagement.so
%_qt5_plugindir/libplasmanetworkmanagement_iodineui.so
%_qt5_plugindir/libplasmanetworkmanagement_wireguardui.so
%_kf5_datadir/plasma/plasmoids/org.kde.plasma.networkmanagement
%_kf5_datadir/kcm_networkmanagement/
%_kf5_knotificationsdir/networkmanagement.notifyrc
%_kf5_services/plasma-applet-org.kde.plasma.networkmanagement.desktop
%_kf5_services/kcm_networkmanagement.desktop
%_kf5_services/plasmanetworkmanagement_iodineui.desktop
%_kf5_services/plasmanetworkmanagement_wireguardui.desktop
%_kf5_servicetypes/plasma-networkmanagement-vpnuiplugin.desktop
%_kf5_metainfodir/org.kde.plasma.networkmanagement.appdata.xml

#--------------------------------------------------------------------

%if %{openvn}
%package  -n plasma-applet-nm-openvpn
Summary:        OpenVPN plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-openvpn

%rename plasma5-applet-nm-openvpn

%description -n plasma-applet-nm-openvpn
OpenVPN plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-openvpn -f plasmanetworkmanagement_openvpnui.lang
%_qt5_plugindir/libplasmanetworkmanagement_openvpnui.so
%_kf5_services/plasmanetworkmanagement_openvpnui.desktop
%endif

#--------------------------------------------------------------------

%if %{l2tp}

%package -n plasma-applet-nm-l2tp
Summary:        L2tp plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-l2tp

%rename plasma5-applet-nm-l2tp

%description -n plasma-applet-nm-l2tp
L2tp plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-l2tp  -f plasmanetworkmanagement_l2tpui.lang
%_qt5_plugindir/libplasmanetworkmanagement_l2tpui.so
%_kf5_services/plasmanetworkmanagement_l2tpui.desktop
%endif

#--------------------------------------------------------------------

%if %{pptp}

%package -n plasma-applet-nm-pptp
Summary:        Pptp plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-pptp

%rename plasma5-applet-nm-pptp

%description -n plasma-applet-nm-pptp
Pptp plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-pptp -f plasmanetworkmanagement_pptpui.lang 
%_kf5_services/plasmanetworkmanagement_pptpui.desktop
%_qt5_plugindir/libplasmanetworkmanagement_pptpui.so
%endif

#--------------------------------------------------------------------

%if %{openswan}

%package -n plasma-applet-nm-openswan
Summary:        OpenSwan plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-openswan

%rename plasma5-applet-nm-openswan

%description -n plasma-applet-nm-openswan
OpenSwan plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-openswan -f plasmanetworkmanagement_openswanui.lang
%_qt5_plugindir/libplasmanetworkmanagement_openswanui.so
%_kf5_services/plasmanetworkmanagement_openswanui.desktop
%endif

#--------------------------------------------------------------------

%if %{strongswan}

%package -n plasma-applet-nm-strongswan
Summary:        Strongswanui plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-strongswan

%rename plasma5-applet-nm-strongswan

%description -n plasma-applet-nm-strongswan
Strongswanui plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-strongswan -f plasmanetworkmanagement_strongswanui.lang
%_qt5_plugindir/libplasmanetworkmanagement_strongswanui.so
%_kf5_services/plasmanetworkmanagement_strongswanui.desktop
%endif

#--------------------------------------------------------------------

%if %{vpnc}

%package -n plasma-applet-nm-vpnc
Summary:        Vpnc plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-vpnc

%rename plasma5-applet-nm-vpnc

%description -n plasma-applet-nm-vpnc
Vpnc plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-vpnc  -f plasmanetworkmanagement_vpncui.lang
%_qt5_plugindir/libplasmanetworkmanagement_vpncui.so
%_kf5_services/plasmanetworkmanagement_vpncui.desktop
%endif

#-------------------------------------------------------------------

%if %{openconnect}
%package -n plasma-applet-nm-openconnect
Summary:        Openconnect plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-openconnect

%rename plasma5-applet-nm-openconnect

# ease upgrade mga7->mga8
Conflicts:      plasma-applet-nm < 5.18.5-2

%description -n plasma-applet-nm-openconnect
Openconnect plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-openconnect -f plasmanetworkmanagement_openconnectui.lang
%_qt5_plugindir/libplasmanetworkmanagement_openconnectui.so
%_kf5_services/plasmanetworkmanagement_openconnectui.desktop
%_kf5_services/plasmanetworkmanagement_openconnect_juniperui.desktop
%_kf5_services/plasmanetworkmanagement_openconnect_globalprotectui.desktop
%_kf5_services/plasmanetworkmanagement_openconnect_pulseui.desktop
%endif

#-------------------------------------------------------------------

%package -n plasma-applet-nm-ssh
Summary:        SSH plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-openconnect

%rename plasma5-applet-nm-ssh

%description -n plasma-applet-nm-ssh
SSH plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-ssh -f plasma-applet-nm-ssh.lang
%_qt5_plugindir/libplasmanetworkmanagement_ssh*.so
%_qt5_plugindir/libplasmanetworkmanagement_sstpui.so
%_kf5_services/plasmanetworkmanagement_sstpui.desktop
%_kf5_services/plasmanetworkmanagement_ssh*.desktop

#--------------------------------------------------------------------

%package -n plasma-applet-nm-fortisslvpnui
Summary:        Fortigate SSL VPN plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-openconnect

%description -n plasma-applet-nm-fortisslvpnui
Fortigate SSL VPN plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-fortisslvpnui -f plasmanetworkmanagement_fortisslvpnui.lang
%_qt5_plugindir/libplasmanetworkmanagement_fortisslvpnui.so
%_kf5_services/plasmanetworkmanagement_fortisslvpnui.desktop

#--------------------------------------------------------------------

%if %{wireguard}
%package  -n plasma-applet-nm-wireguard
Summary:        Wireguard plugin for Plasma 5 NetworkManager
Group:          Graphical desktop/KDE
Requires:       plasma-applet-nm = %{version}-%{release}
Requires:       networkmanager-wireguard

%rename plasma5-applet-nm-wireguard

%description -n plasma-applet-nm-wireguard
Wireguard plugin for Plasma 5 NetworkManager.

%files -n plasma-applet-nm-wireguard
%_qt5_plugindir/libplasmanetworkmanagement_wireguardui.so
%_kf5_services/plasmanetworkmanagement_wireguardui.desktop
%endif

#--------------------------------------------------------------------


%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%if ! %{l2tp}
rm %{buildroot}%{_qt5_plugindir}/libplasmanetworkmanagement_l2tpui.so
rm %{buildroot}%{_kf5_services}/plasmanetworkmanagement_l2tpui.desktop
rm %{buildroot}%{_kf5_datadir}/locale/*/LC_MESSAGES/plasmanetworkmanagement_l2tpui.mo
%endif

%if ! %{openswan}
rm %{buildroot}%{_qt5_plugindir}/libplasmanetworkmanagement_openswanui.so
rm %{buildroot}%{_kf5_services}/plasmanetworkmanagement_openswanui.desktop
rm %{buildroot}%{_kf5_datadir}/locale/*/LC_MESSAGES/plasmanetworkmanagement_openswanui.mo
%endif

%if ! %{strongswan}
rm %{buildroot}%{_qt5_plugindir}/libplasmanetworkmanagement_strongswanui.so
rm %{buildroot}%{_kf5_services}/plasmanetworkmanagement_strongswanui.desktop
rm %{buildroot}%{_kf5_datadir}/locale/*/LC_MESSAGES/plasmanetworkmanagement_strongswanui.mo
%endif

rm -f %{name}.lang
touch %{name}.lang
for n in \
    plasma_applet_org.kde.plasma.networkmanagement \
    plasmanetworkmanagement-kded \
    plasmanetworkmanagement-libs \
    plasmanetworkmanagement-kcm \
    plasmanetworkmanagement_iodineui \
    kcm_mobile_broadband \
    kcm_mobile_hotspot \
    kcm_mobile_wifi
do
  %find_lang $n
  cat ${n}.lang >>%{name}.lang
  rm -f ${n}.lang
done
%find_lang plasmanetworkmanagement_l2tpui
%find_lang plasmanetworkmanagement_openconnectui
%find_lang plasmanetworkmanagement_vpncui
%if %{strongswan}
%find_lang plasmanetworkmanagement_strongswanui
%endif
%find_lang plasmanetworkmanagement_pptpui
%find_lang plasmanetworkmanagement_openvpnui
%if %{openswan}
%find_lang plasmanetworkmanagement_openswanui
%endif
rm -f plasma-applet-nm-ssh.lang
touch plasma-applet-nm-ssh.lang
for n in \
    plasmanetworkmanagement_sshui \
    plasmanetworkmanagement_sstpui
do
  %find_lang  $n
  cat ${n}.lang >>plasma-applet-nm-ssh.lang
  rm -f ${n}.lang
done

%find_lang plasmanetworkmanagement_fortisslvpnui


%changelog
* Thu May 06 2021 daviddavid <daviddavid> 5.21.5-1.mga9
+ Revision: 1721774
- New version 5.21.5

* Mon Apr 12 2021 daviddavid <daviddavid> 5.21.4-1.mga9
+ Revision: 1715407
- New version 5.21.4

* Thu Mar 18 2021 daviddavid <daviddavid> 5.21.3-1.mga9
+ Revision: 1704284
- New version 5.21.3

* Fri Mar 05 2021 daviddavid <daviddavid> 5.21.2-2.mga9
+ Revision: 1699756
- update BRs, remove no more needed kdelibs4support

* Wed Mar 03 2021 daviddavid <daviddavid> 5.21.2-1.mga9
+ Revision: 1697457
- New version 5.21.2

* Sun Feb 28 2021 daviddavid <daviddavid> 5.21.1-1.mga9
+ Revision: 1693829
- New version 5.21.1

* Mon Dec 07 2020 daviddavid <daviddavid> 5.20.4-1.mga8
+ Revision: 1654208
- New version 5.20.4

* Sat Nov 14 2020 daviddavid <daviddavid> 5.20.3-1.mga8
+ Revision: 1645430
- New version 5.20.3

* Wed Oct 28 2020 daviddavid <daviddavid> 5.20.2-1.mga8
+ Revision: 1639999
- New version 5.20.2

* Wed Oct 21 2020 daviddavid <daviddavid> 5.20.1-1.mga8
+ Revision: 1637752
- New version 5.20.1

* Wed Oct 14 2020 daviddavid <daviddavid> 5.20.0-1.mga8
+ Revision: 1635719
- New version 5.20.0

* Wed Sep 02 2020 daviddavid <daviddavid> 5.19.5-1.mga8
+ Revision: 1620799
- New version 5.19.5

* Wed Jul 29 2020 daviddavid <daviddavid> 5.19.4-1.mga8
+ Revision: 1609617
- New version 5.19.4

* Wed Jul 08 2020 neoclust <neoclust> 5.19.3-1.mga8
+ Revision: 1603016
- New version 5.19.3

* Sun Jun 28 2020 daviddavid <daviddavid> 5.19.2-2.mga8
+ Revision: 1600015
- plasma-nm [2/2]: Fix password is asked twice

* Tue Jun 23 2020 daviddavid <daviddavid> 5.19.2-1.mga8
+ Revision: 1598731
- New version 5.19.2

* Thu Jun 18 2020 daviddavid <daviddavid> 5.19.1-2.mga8
+ Revision: 1596214
- enable KF5Kirigami2 support

* Thu Jun 18 2020 daviddavid <daviddavid> 5.19.1-1.mga8
+ Revision: 1596039
- New version 5.19.1
+ neoclust <neoclust>
- New version 5.18.90

* Fri May 08 2020 daviddavid <daviddavid> 5.18.5-2.mga8
+ Revision: 1581615
- move plasma-networkmanagement-vpnuiplugin.desktop file into the main pkg
- move plasmanetworkmanagement_openconnect_juniperui.desktop file into the openconnect sub-pkg
- make sure all sub-pkgs requires the main plasma-applet-nm pkg

* Wed May 06 2020 daviddavid <daviddavid> 5.18.5-1.mga8
+ Revision: 1580775
- New version 5.18.5
- New version 5.18.4.1

* Tue Mar 17 2020 daviddavid <daviddavid> 5.18.3-1.mga8
+ Revision: 1557174
- New version 5.18.3

* Tue Feb 25 2020 daviddavid <daviddavid> 5.18.2-1.mga8
+ Revision: 1550390
- New version 5.18.2

* Fri Feb 21 2020 daviddavid <daviddavid> 5.18.1-1.mga8
+ Revision: 1548262
- New version 5.18.1

* Thu Feb 20 2020 umeabot <umeabot> 5.18.0-2.mga8
+ Revision: 1547136
- Mageia 8 Mass Rebuild

* Wed Feb 12 2020 daviddavid <daviddavid> 5.18.0-1.mga8
+ Revision: 1496324
- New version 5.18.0

* Thu Feb 06 2020 neoclust <neoclust> 5.17.90.4-1.mga8
+ Revision: 1487478
- New version 5.17.90.4
- New version 5.17.90
+ wally <wally>
- build with new cmake macros

* Wed Dec 04 2019 daviddavid <daviddavid> 5.17.4-1.mga8
+ Revision: 1464311
- New version 5.17.4

* Fri Nov 15 2019 daviddavid <daviddavid> 5.17.3-1.mga8
+ Revision: 1460069
- New version 5.17.3

* Wed Oct 30 2019 daviddavid <daviddavid> 5.17.2-1.mga8
+ Revision: 1456780
- New version 5.17.2

* Sat Oct 26 2019 daviddavid <daviddavid> 5.17.1-2.mga8
+ Revision: 1455913
- enable Prison support

* Wed Oct 23 2019 daviddavid <daviddavid> 5.17.1-1.mga8
+ Revision: 1455345
- New version 5.17.1

* Mon Oct 14 2019 neoclust <neoclust> 5.17.0-1.mga8
+ Revision: 1453177
- New version 5.17.0

* Sun Sep 29 2019 neoclust <neoclust> 5.16.90-1.mga8
+ Revision: 1448073
- New version 5.16.90

* Wed Sep 04 2019 neoclust <neoclust> 5.16.5-1.mga8
+ Revision: 1437061
- New version 5.16.5

* Thu Aug 22 2019 daviddavid <daviddavid> 5.16.4-2.mga8
+ Revision: 1431296
- adjust BR for new NM

* Wed Jul 31 2019 neoclust <neoclust> 5.16.4-1.mga8
+ Revision: 1426329
- New version 5.16.4

* Thu Jul 25 2019 neoclust <neoclust> 5.16.3-1.mga8
+ Revision: 1424128
- New version 5.16.3

* Mon Apr 08 2019 neoclust <neoclust> 5.15.4-1.mga7
+ Revision: 1386861
- New version 5.15.4

* Mon Apr 01 2019 umeabot <umeabot> 5.15.3-2.mga7
+ Revision: 1384012
- Qt5 Rebuild

* Tue Mar 12 2019 neoclust <neoclust> 5.15.3-1.mga7
+ Revision: 1374944
- New version 5.15.3

* Thu Feb 28 2019 neoclust <neoclust> 5.15.2-1.mga7
+ Revision: 1370567
- New version 5.15.2

* Tue Feb 19 2019 neoclust <neoclust> 5.15.1-1.mga7
+ Revision: 1368607
- New version 5.15.1

* Sat Feb 16 2019 neoclust <neoclust> 5.15.0-1.mga7
+ Revision: 1367765
- New version 5.15.0

* Mon Jan 14 2019 neoclust <neoclust> 5.14.5-1.mga7
+ Revision: 1356191
- New version 5.14.5

* Sun Dec 09 2018 neoclust <neoclust> 5.14.4-1.mga7
+ Revision: 1339328
- New version 5.14.4

* Wed Oct 24 2018 neoclust <neoclust> 5.14.2-1.mga7
+ Revision: 1324893
- New version 5.14.2

* Sun Sep 23 2018 umeabot <umeabot> 5.13.4-2.mga7
+ Revision: 1300305
- Mageia 7 Mass Rebuild

* Sat Aug 18 2018 neoclust <neoclust> 5.13.4-1.mga7
+ Revision: 1252567
- New version 5.13.4

* Fri Feb 23 2018 neoclust <neoclust> 5.12.2-1.mga7
+ Revision: 1204457
- New version 5.12.2

* Wed Feb 14 2018 neoclust <neoclust> 5.12.1-1.mga7
+ Revision: 1201003
- New version 5.12.1

* Thu Jan 18 2018 neoclust <neoclust> 5.11.95-1.mga7
+ Revision: 1194309
- New version 5.11.95

* Wed Dec 27 2017 neoclust <neoclust> 5.11.4-1.mga7
+ Revision: 1185697
- New version 5.11.4

* Fri Oct 27 2017 neoclust <neoclust> 5.11.2-1.mga7
+ Revision: 1174117
- New version 5.11.2

* Sun Oct 22 2017 neoclust <neoclust> 5.11.1-1.mga7
+ Revision: 1173114
- New version 5.11.1
- New version 5.10.95

* Mon Sep 18 2017 cjw <cjw> 5.10.5-1.mga7
+ Revision: 1155126
- fix build with new find_lang
+ neoclust <neoclust>
- New version 5.10.5

* Tue Jul 25 2017 neoclust <neoclust> 5.10.4-1.mga7
+ Revision: 1130775
- New version 5.10.4
- New version 5.10.3

* Fri May 26 2017 neoclust <neoclust> 5.8.7-1.mga6
+ Revision: 1104853
- New version 5.8.7

* Wed Mar 08 2017 neoclust <neoclust> 5.8.6-2.mga6
+ Revision: 1089710
- Rebuild for arm

* Mon Mar 06 2017 neoclust <neoclust> 5.8.6-1.mga6
+ Revision: 1089039
- New version 5.8.6

* Tue Dec 27 2016 neoclust <neoclust> 5.8.5-1.mga6
+ Revision: 1078174
- New version 5.8.5

* Mon Nov 28 2016 neoclust <neoclust> 5.8.4-1.mga6
+ Revision: 1070731
- New version 5.8.4

* Thu Nov 03 2016 neoclust <neoclust> 5.8.3-2.mga6
+ Revision: 1065064
- Rebuild against Qt 5.6.2

* Tue Nov 01 2016 neoclust <neoclust> 5.8.3-1.mga6
+ Revision: 1064492
- New version 5.8.3

* Sat Oct 22 2016 neoclust <neoclust> 5.8.2-1.mga6
+ Revision: 1063062
- New version 5.8.2
- New version 5.8.2

* Wed Oct 12 2016 neoclust <neoclust> 5.8.1-1.mga6
+ Revision: 1060287
- New version 5.8.1

* Thu Sep 29 2016 neoclust <neoclust> 5.8.0-1.mga6
+ Revision: 1057613
- New version 5.8.0

* Thu Sep 15 2016 neoclust <neoclust> 5.7.95-1.mga6
+ Revision: 1053069
- New version 5.7.95

* Wed Sep 14 2016 neoclust <neoclust> 5.7.5-1.mga6
+ Revision: 1052697
- New version 5.7.5

* Thu Aug 25 2016 neoclust <neoclust> 5.7.4-1.mga6
+ Revision: 1048829
- New version 5.7.4

* Tue Aug 02 2016 neoclust <neoclust> 5.7.3-1.mga6
+ Revision: 1044283
- New version 5.7.3

* Tue Jul 19 2016 neoclust <neoclust> 5.7.2-1.mga6
+ Revision: 1042571
- New version 5.7.2

* Tue Jul 12 2016 neoclust <neoclust> 5.7.1-1.mga6
+ Revision: 1041408
- New version 5.7.1

* Thu Jul 07 2016 neoclust <neoclust> 5.7.0-1.mga6
+ Revision: 1039513
- New version 5.7.0

* Fri Jun 17 2016 neoclust <neoclust> 5.6.5-1.mga6
+ Revision: 1021885
- New version 5.6.5

* Fri May 13 2016 neoclust <neoclust> 5.6.4-1.mga6
+ Revision: 1014553
- New version 5.6.4

* Wed May 04 2016 neoclust <neoclust> 5.6.3-1.mga6
+ Revision: 1009290
- New version 5.6.3

* Fri Apr 08 2016 neoclust <neoclust> 5.6.2-1.mga6
+ Revision: 999274
- New version 5.6.2

* Sun Apr 03 2016 neoclust <neoclust> 5.6.1-1.mga6
+ Revision: 998029
- New version 5.6.1

* Wed Mar 23 2016 neoclust <neoclust> 5.6.0-1.mga6
+ Revision: 994407
- New version 5.6.0

* Sun Mar 20 2016 luigiwalser <luigiwalser> 5.5.95-3.mga6
+ Revision: 993373
- disable openswan applet, networkmanager-openswan no longer packaged

* Mon Mar 07 2016 neoclust <neoclust> 5.5.95-2.mga6
+ Revision: 987070
- Rebuild against kf5 5.20.0

* Wed Mar 02 2016 neoclust <neoclust> 5.5.95-1.mga6
+ Revision: 983756
- New version 5.5.95

* Tue Jan 26 2016 neoclust <neoclust> 5.5.4-1.mga6
+ Revision: 927984
- New version 5.5.4

* Wed Jan 13 2016 neoclust <neoclust> 5.5.3-1.mga6
+ Revision: 922518
- New version 5.5.3
- Rebuild against new cmake to have cmake() provides
- New version 5.5.2

* Wed Dec 23 2015 neoclust <neoclust> 5.5.1-2.mga6
+ Revision: 913647
- Rebuild against Qt 5.6.0 Beta

* Tue Dec 15 2015 neoclust <neoclust> 5.5.1-1.mga6
+ Revision: 910699
- New version 5.5.1

* Tue Dec 08 2015 neoclust <neoclust> 5.5.0-1.mga6
+ Revision: 908860
- New version 5.5.0

* Fri Nov 20 2015 neoclust <neoclust> 5.4.95-1.mga6
+ Revision: 904413
- New version 5.4.95

* Tue Nov 10 2015 neoclust <neoclust> 5.4.90-2.mga6
+ Revision: 900855
- Rebuild against fixed qtbase5
- New version 5.4.90

* Sun Oct 11 2015 neoclust <neoclust> 5.4.2-1.mga6
+ Revision: 889531
- New version 5.4.2

* Wed Sep 09 2015 neoclust <neoclust> 5.4.1-1.mga6
+ Revision: 874743
- New version 5.4.1

* Wed Aug 26 2015 neoclust <neoclust> 5.4.0-1.mga6
+ Revision: 869660
- New version 5.4.0

* Wed Aug 12 2015 neoclust <neoclust> 5.3.95-1.mga6
+ Revision: 863632
- New version 5.3.95

* Sun Jul 19 2015 sander85 <sander85> 5.3.2-2.mga6
+ Revision: 855544
- Enable openswan + fix renaming for plasma5-applet-nm-l2tp and plasma5-applet-nm-openconnect

* Sun Jul 19 2015 sander85 <sander85> 5.3.2-1.mga6
+ Revision: 855496
- Rename plasma5-* -> plasma-*
- Rename
- New version: 5.3.2

* Mon May 11 2015 tmb <tmb> 5.1.2-3.mga5
+ Revision: 821750
- rebuild for new NM

* Sun Dec 21 2014 lmenut <lmenut> 5.1.2-2.mga5
+ Revision: 804593
- add version to conflicts
- OpenVPN plugin : Add option for server certificate verification
  upstream patches from master (mga#14812, bko#341069)

* Fri Dec 19 2014 neoclust <neoclust> 5.1.2-1.mga5
+ Revision: 804202
- New version

* Mon Oct 27 2014 lmenut <lmenut> 5.0.1-4.mga5
+ Revision: 793589
- add missing conflicts with KDE 4

* Wed Oct 15 2014 umeabot <umeabot> 5.0.1-3.mga5
+ Revision: 744785
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 5.0.1-2.mga5
+ Revision: 687645
- Mageia 5 Mass Rebuild
+ lmenut <lmenut>
- disable openswan & strongswan plugins
- fix summaries & descriptions
- simplify find_lang
+ neoclust <neoclust>
- Rename as this is not a framework
- Rename

* Sat Aug 16 2014 neoclust <neoclust> 5.0.1-1.mga5
+ Revision: 663707
- imported package kf5-plasma-nm

