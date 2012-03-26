# keeping it here just in case someone wants to use the SVN version
# svn co http://svn.openchrome.org/svn/trunk openchrome

# (anssi) The unversioned symlink of XvMC library must be present in
# %{_libdir} during normal use, as libXvMC uses that name for dlopening.
# Our devel requires finder catches that, hence this exception:
%define __noautoreq 'devel\\('

Name: x11-driver-video-openchrome
Version: 0.2.905
Release: 2
Summary: X.org driver for Unichrome cards from the OpenChrome project
Group: System/X11
URL: http://www.openchrome.org
Source0: http://www.openchrome.org/releases/xf86-video-openchrome-%{version}.tar.bz2
# Mandriva patches
# http://billionmonkeys.net/openchrome - broken 2008/07
Patch100: xf86-video-openchrome-0.2.901-billionmokeys.net_modelines.patch
Patch101: 0003-IDs-enable-LCD-on-Guillemot-NA01.patch
Patch102: openchrome_mips_xvmc.patch
License: MIT

BuildRequires: GL-devel
BuildRequires: libdrm-devel
BuildRequires: libx11-devel
BuildRequires: libxvmc-devel
BuildRequires: libxext-devel
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
A free and Open Source video driver for the VIA/S3G
UniChrome and UniChrome Pro graphics chipsets. (CLE266,
KN400, KM400, K8M800, PM800, CN400, VN800)

%prep
%setup -q -n xf86-video-openchrome-%{version}
%patch100 -p1 -b .billionmonkeys
%patch102 -p1 -b .xvmc

#needed by patch0
libtoolize
autoreconf

%build
%configure2_5x --disable-static --enable-dri
%make

%install
%makeinstall_std
# From Fedora:
# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%files
%{_libdir}/libchromeXvMC.so
%{_libdir}/libchromeXvMC.so.1
%{_libdir}/libchromeXvMC.so.1.0.0
%{_libdir}/libchromeXvMCPro.so
%{_libdir}/libchromeXvMCPro.so.1
%{_libdir}/libchromeXvMCPro.so.1.0.0
%{_libdir}/xorg/modules/drivers/openchrome_drv.so
%{_mandir}/man4/openchrome.*
