# keeping it here just in case someone wants to use the SVN version
# svn co http://svn.openchrome.org/svn/trunk openchrome

# (anssi) The unversioned symlink of XvMC library must be present in
# %{_libdir} during normal use, as libXvMC uses that name for dlopening.
# Our devel requires finder catches that, hence this exception:
%define _requires_exceptions devel(

Name: x11-driver-video-openchrome
Version: 0.2.902
Release: %mkrel 1
Summary: X.org driver for Unichrome cards from the OpenChrome project
Group: System/X11
URL: http://www.openchrome.org
Source0: http://www.openchrome.org/releases/xf86-video-openchrome-%{version}.tar.gz
# Fedora patches (stay in sync with Fedora rawhide)
# Patches with _mdv extension had to be rediffed for MDV for some
# reason - AdamW 2008/07
# re_enable_AGPDMA.patch should only be used when kernel >= 2.6.25rc7
Patch0: openchrome-0.2.902-re_enable_AGPDMA.patch
Patch1: openchrome-0.2.902-report_version.patch
Patch2: openchrome-0.2.902-chipset_revision_mdv.patch
Patch3: openchrome-0.2.902-unbreak_ActiveDevice.patch
Patch4: openchrome-0.2.902-CX700_Xv_on_LCD_mdv.patch
Patch5: openchrome-0.2.902-disable_XvDMA_P4M890_K8M890.patch
Patch6: openchrome-0.2.902-sync_pciids.patch
# Mandriva patches
# http://billionmonkeys.net/openchrome - broken 2008/07
Patch100: xf86-video-openchrome-0.2.901-billionmokeys.net_modelines.patch
# Fix underlinking - AdamW 2008/07
Patch101: xf86-video-openchrome-0.2.902-underlink.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: GL-devel
BuildRequires: libdrm-devel
BuildRequires: libx11-devel
BuildRequires: libxvmc-devel
BuildRequires: libxext-devel
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
A free and Open Source video driver for the VIA/S3G
UniChrome and UniChrome Pro graphics chipsets. (CLE266,
KN400, KM400, K8M800, PM800, CN400, VN800)

%prep
%setup -q -n xf86-video-openchrome-%{version}
%patch0 -p0 -b .agpdma
%patch1 -p0 -b .version
%patch2 -p0 -b .chiprev
%patch3 -p0 -b .activedevice
%patch4 -p0 -b .cx700_xv_lcd
%patch5 -p0 -b .XvDMA
%patch6 -p0 -b .pciids
%patch100 -p1 -b .billionmonkeys
%patch101 -p1 -b .underlink

%build
# needed for underlink.patch - AdamW 2008/07
autoreconf
%configure2_5x --disable-static --enable-dri
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# From Fedora:
# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/libchromeXvMC.so
%{_libdir}/libchromeXvMC.so.1
%{_libdir}/libchromeXvMC.so.1.0.0
%{_libdir}/libchromeXvMCPro.so
%{_libdir}/libchromeXvMCPro.so.1
%{_libdir}/libchromeXvMCPro.so.1.0.0
%{_libdir}/xorg/modules/drivers/openchrome_drv.so
%{_mandir}/man4/openchrome.*

