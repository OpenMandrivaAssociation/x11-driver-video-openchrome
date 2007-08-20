%define snapshot_date 20070406

# 20070406 = svnrel 313
# svn co http://svn.openchrome.org/svn/trunk openchrome

# (anssi) The unversioned symlink of XvMC library must be present in
# %{_libdir} during normal use, as libXvMC uses that name for dlopening.
# Our devel requires finder catches that, hence this exception:
%define _requires_exceptions devel(

Name: x11-driver-video-openchrome
Version: 0.2.0.%{snapshot_date}
Release: %mkrel 1
Summary: The X.org driver for Unichrome cards from the OpenChrome project
Group: System/X11
URL: http://www.openchrome.org
Source: openchrome-%{snapshot_date}.tar.bz2
Patch0: unichrome-driver_name.patch
Patch1: unichrome-fixcompile.patch
# http://wiki.openchrome.org/pipermail/openchrome-users/2007-February/002752.html
Patch2: vt1625_NTSC_modes.patch
# http://billionmokeys.net/openchrome
Patch3: billionmokeys.net_openchrome.patch
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
The X.org driver for Imstt



%prep
%setup -q -n openchrome
%patch0 -p1 -b .driver_name
#patch1 -p1 -b .fixcompile
%patch2 -p0 -b .vt1625_NTSC_modes
%patch3 -p0 -b .billionmonkeys
sh autogen.sh

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/libopenchromeXvMC.la
%{_libdir}/libopenchromeXvMC.so
%{_libdir}/libopenchromeXvMC.so.1
%{_libdir}/libopenchromeXvMC.so.1.0.0
%{_libdir}/libopenchromeXvMCPro.la
%{_libdir}/libopenchromeXvMCPro.so
%{_libdir}/libopenchromeXvMCPro.so.1
%{_libdir}/libopenchromeXvMCPro.so.1.0.0
%{_libdir}/xorg/modules/drivers/openchrome_drv.la
%{_libdir}/xorg/modules/drivers/openchrome_drv.so
%{_mandir}/man4/openchrome.*



