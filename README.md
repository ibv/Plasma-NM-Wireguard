# KDE Plasma Network Manager Wireguard 

### Updated: May 2021
- fixed for Mageia 8/9
- added .spec files for plasma-applet-nm-wireguard, networkmanager-wireguar

(plasma-nm-wireguard/plasma-applet-nm-wireguard)

I am not the dev of that project, this is just a mirror repo to make the tool available for those who don't want to wait a released version by KDE

Addition to plasma-nm to allow the use WireGuard VPN.

Just be aware that it is definitely still a work in progress. 

This requires installation of [network-manager-wireguard](https://github.com/max-moser/network-manager-wireguard) before this will have any effect.

This is just a mirrored/updated version of project https://phabricator.kde.org/D15093
                       
## Guide

### Dev
All merit to https://github.com/Druco  

### Releases
I am distributing an rpm package, RHEL based version awaiting the project to be upstreamed and released (Just check the releases page) 

RPM for Mageia/Opensuse/Fedora/Redhat/ROSA/OpenMandriva/PCLinuxOS/CentOS 

Note that i did not test my rpms on all those distro, if it does not work just extract the rpm and copy the needed files manually... you will probably only need plasma-applet-nm-wireguard-5.21.5-1.mga8.x86_64.rpm

### Compilation
- To compile you need to get [plasma-nm](https://github.com/KDE/plasma-nm) and clone this project under the 'vpn' directory in that tree, 
- Then edit the file 'plasma-nm/vpn/CMakeLists.txt' and add 'add_subdirectory(wireguard)'
- Then run the build process for plasma-nm and there should be a library called 'libplasmanetworkmanagement_wireguardui.so' created in the corresponding directory in the 'build' tree.

If you already have a binary version of plasma-nm installed, you can probably get away with just copying this library to where the rest of the VPN plugin libraries are located (in my case it was '/usr/lib64/qt5/plugins') but your mileage may vary. Then copy plasmanetworkmanagement_wireguardui.desktop to where all the rest of the 'plasmnetworkmanagement_xxx.desktop' files are. In my case this was /usr/share/kservices5.

