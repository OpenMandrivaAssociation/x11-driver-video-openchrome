# keeping it here just in case someone wants to use the SVN version
# svn co http://svn.openchrome.org/svn/trunk openchrome

# (anssi) The unversioned symlink of XvMC library must be present in
# %{_libdir} during normal use, as libXvMC uses that name for dlopening.
# Our devel requires finder catches that, hence this exception:
%define __noautoreq 'devel\\('

%define major 1
%define libxvmc %mklibname chromeXvMC %{major}
%define libpro %mklibname chromeXvMCPro %{major}
%define devname %mklibname %{name} -d

Summary:	X.org driver for Unichrome cards from the OpenChrome project
Name:		x11-driver-video-openchrome
Version:	0.5.0
Release:	1
Group:		System/X11
License:	MIT
Url:		http://www.openchrome.org
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-video-openchrome-%{version}.tar.bz2
# Mandriva patches
# http://billionmonkeys.net/openchrome - broken 2008/07
Patch100:	xf86-video-openchrome-0.2.901-billionmokeys.net_modelines.patch
Patch101:	0003-IDs-enable-LCD-on-Guillemot-NA01.patch
Patch102:	openchrome_mips_arm_xvmc.patch
Patch104:	xf86-video-openchrome-0.3.2-link-against-X11.patch
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xvmc)
BuildRequires:	pkgconfig(udev)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Requires:	udev
ExclusiveArch:	%{ix86} x86_64

%description
A free and Open Source video driver for the VIA/S3G
UniChrome and UniChrome Pro graphics chipsets. (CLE266,
KN400, KM400, K8M800, PM800, CN400, VN800)

%package -n %{libxvmc}
Summary:	X Library
Group:		System/Libraries
Conflicts:	%{name} < 0.3.1-3

%description -n %{libxvmc}
This package contains a shared library for %{name}.

%package -n %{libpro}
Summary:	X Library
Group:		System/Libraries
Conflicts:	%{name} < 0.3.1-3

%description -n %{libpro}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxvmc} = %{version}-%{release}
Requires:	%{libpro} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{name} < 0.3.1-3

%description -n %{libpro}
This package contains the development files for %{name}.

%prep
%setup -qn xf86-video-openchrome-%{version}
%patch100 -p1 -b .billionmonkeys~
%patch102 -p1 -b .xvmc~
%patch104 -p1 -b .link

%build
autoreconf -fiv
%configure \
	--disable-static \
	--enable-viaregtool \
	--enable-dri
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/openchrome_drv.so
%{_mandir}/man4/openchrome.*
%{_sbindir}/via_regs_dump

%files  -n %{libxvmc}
%{_libdir}/libchromeXvMC.so.%{major}*

%files  -n %{libpro}
%{_libdir}/libchromeXvMCPro.so.%{major}*

%files  -n %{devname}
%{_libdir}/libchromeXvMC.so
%{_libdir}/libchromeXvMCPro.so
