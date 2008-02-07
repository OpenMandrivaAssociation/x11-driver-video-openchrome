## keeping it here just in case someone wants to use the SVN version
# %define snapshot_date 20071015
# 20071015 = svnrel 412
# svn co http://svn.openchrome.org/svn/trunk openchrome

# (anssi) The unversioned symlink of XvMC library must be present in
# %{_libdir} during normal use, as libXvMC uses that name for dlopening.
# Our devel requires finder catches that, hence this exception:
%define _requires_exceptions devel(

Name: x11-driver-video-openchrome
Version: 0.2.901
Release: %mkrel 1
Summary: The X.org driver for Unichrome cards from the OpenChrome project
Group: System/X11
URL: http://www.openchrome.org
Source: http://www.openchrome.org/releases/xf86-video-openchrome-0.2.901.tar.bz2
# http://billionmokeys.net/openchrome
Patch0: xf86-video-openchrome-0.2.901-billionmokeys.net_modelines.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: GL-devel
BuildRequires: libdrm-devel
BuildRequires: libx11-devel
BuildRequires: libxvmc-devel
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
%patch0 -p1 -b .billionmonkeys

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/libchromeXvMC.la
%{_libdir}/libchromeXvMC.so
%{_libdir}/libchromeXvMC.so.1
%{_libdir}/libchromeXvMC.so.1.0.0
%{_libdir}/libchromeXvMCPro.la
%{_libdir}/libchromeXvMCPro.so
%{_libdir}/libchromeXvMCPro.so.1
%{_libdir}/libchromeXvMCPro.so.1.0.0
%{_libdir}/xorg/modules/drivers/openchrome_drv.la
%{_libdir}/xorg/modules/drivers/openchrome_drv.so
%{_mandir}/man4/openchrome.*

