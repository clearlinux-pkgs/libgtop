#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: f4bef72
#
Name     : libgtop
Version  : 2.41.3
Release  : 17
URL      : https://download.gnome.org/sources/libgtop/2.41/libgtop-2.41.3.tar.xz
Source0  : https://download.gnome.org/sources/libgtop/2.41/libgtop-2.41.3.tar.xz
Summary  : LibGTop library
Group    : Development/Tools
License  : GPL-2.0
Requires: libgtop-data = %{version}-%{release}
Requires: libgtop-info = %{version}-%{release}
Requires: libgtop-lib = %{version}-%{release}
Requires: libgtop-libexec = %{version}-%{release}
Requires: libgtop-license = %{version}-%{release}
Requires: libgtop-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : file
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc.

On Linux systems, these information are taken directly from the /proc
filesystem while on other systems a server is used to read those
information from /dev/kmem or whatever.

%package data
Summary: data components for the libgtop package.
Group: Data

%description data
data components for the libgtop package.


%package dev
Summary: dev components for the libgtop package.
Group: Development
Requires: libgtop-lib = %{version}-%{release}
Requires: libgtop-data = %{version}-%{release}
Provides: libgtop-devel = %{version}-%{release}
Requires: libgtop = %{version}-%{release}

%description dev
dev components for the libgtop package.


%package doc
Summary: doc components for the libgtop package.
Group: Documentation
Requires: libgtop-info = %{version}-%{release}

%description doc
doc components for the libgtop package.


%package info
Summary: info components for the libgtop package.
Group: Default

%description info
info components for the libgtop package.


%package lib
Summary: lib components for the libgtop package.
Group: Libraries
Requires: libgtop-data = %{version}-%{release}
Requires: libgtop-libexec = %{version}-%{release}
Requires: libgtop-license = %{version}-%{release}

%description lib
lib components for the libgtop package.


%package libexec
Summary: libexec components for the libgtop package.
Group: Default
Requires: libgtop-license = %{version}-%{release}

%description libexec
libexec components for the libgtop package.


%package license
Summary: license components for the libgtop package.
Group: Default

%description license
license components for the libgtop package.


%package locales
Summary: locales components for the libgtop package.
Group: Default

%description locales
locales components for the libgtop package.


%prep
%setup -q -n libgtop-2.41.3
cd %{_builddir}/libgtop-2.41.3
pushd ..
cp -a libgtop-2.41.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710950529
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710950529
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgtop
cp %{_builddir}/libgtop-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libgtop/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/libgtop-%{version}/copyright.txt %{buildroot}/usr/share/package-licenses/libgtop/25953e10e4c2bf3c77db0e6e5f3f9eb9d502d747 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang libgtop
## install_append content
chmod -s %{buildroot}*/usr/libexec/libgtop_server2
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GTop-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libgtop-2.0/glibtop.h
/usr/include/libgtop-2.0/glibtop/close.h
/usr/include/libgtop-2.0/glibtop/command.h
/usr/include/libgtop-2.0/glibtop/cpu.h
/usr/include/libgtop-2.0/glibtop/disk.h
/usr/include/libgtop-2.0/glibtop/fsusage.h
/usr/include/libgtop-2.0/glibtop/global.h
/usr/include/libgtop-2.0/glibtop/gnuserv.h
/usr/include/libgtop-2.0/glibtop/loadavg.h
/usr/include/libgtop-2.0/glibtop/mem.h
/usr/include/libgtop-2.0/glibtop/mountlist.h
/usr/include/libgtop-2.0/glibtop/msg_limits.h
/usr/include/libgtop-2.0/glibtop/netlist.h
/usr/include/libgtop-2.0/glibtop/netload.h
/usr/include/libgtop-2.0/glibtop/open.h
/usr/include/libgtop-2.0/glibtop/parameter.h
/usr/include/libgtop-2.0/glibtop/ppp.h
/usr/include/libgtop-2.0/glibtop/procaffinity.h
/usr/include/libgtop-2.0/glibtop/procargs.h
/usr/include/libgtop-2.0/glibtop/procio.h
/usr/include/libgtop-2.0/glibtop/prockernel.h
/usr/include/libgtop-2.0/glibtop/proclist.h
/usr/include/libgtop-2.0/glibtop/procmap.h
/usr/include/libgtop-2.0/glibtop/procmem.h
/usr/include/libgtop-2.0/glibtop/procopenfiles.h
/usr/include/libgtop-2.0/glibtop/procsegment.h
/usr/include/libgtop-2.0/glibtop/procsignal.h
/usr/include/libgtop-2.0/glibtop/procstate.h
/usr/include/libgtop-2.0/glibtop/proctime.h
/usr/include/libgtop-2.0/glibtop/procuid.h
/usr/include/libgtop-2.0/glibtop/procwd.h
/usr/include/libgtop-2.0/glibtop/sem_limits.h
/usr/include/libgtop-2.0/glibtop/shm_limits.h
/usr/include/libgtop-2.0/glibtop/signal.h
/usr/include/libgtop-2.0/glibtop/swap.h
/usr/include/libgtop-2.0/glibtop/sysdeps.h
/usr/include/libgtop-2.0/glibtop/sysinfo.h
/usr/include/libgtop-2.0/glibtop/union.h
/usr/include/libgtop-2.0/glibtop/uptime.h
/usr/include/libgtop-2.0/glibtop_machine.h
/usr/include/libgtop-2.0/glibtop_server.h
/usr/include/libgtop-2.0/glibtop_suid.h
/usr/include/libgtop-2.0/libgtopconfig.h
/usr/lib64/libgtop-2.0.so
/usr/lib64/pkgconfig/libgtop-2.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libgtop/home.png
/usr/share/gtk-doc/html/libgtop/index.html
/usr/share/gtk-doc/html/libgtop/left-insensitive.png
/usr/share/gtk-doc/html/libgtop/left.png
/usr/share/gtk-doc/html/libgtop/libgtop-Close.html
/usr/share/gtk-doc/html/libgtop/libgtop-Command.html
/usr/share/gtk-doc/html/libgtop/libgtop-GlibTop-Server.html
/usr/share/gtk-doc/html/libgtop/libgtop-GlibTop.html
/usr/share/gtk-doc/html/libgtop/libgtop-Net-List.html
/usr/share/gtk-doc/html/libgtop/libgtop-Net-Load.html
/usr/share/gtk-doc/html/libgtop/libgtop-PPP.html
/usr/share/gtk-doc/html/libgtop/libgtop-Process-Arguments.html
/usr/share/gtk-doc/html/libgtop/libgtop-Process-List.html
/usr/share/gtk-doc/html/libgtop/libgtop-Process-Time.html
/usr/share/gtk-doc/html/libgtop/libgtop-Shared-Memory-Limits.html
/usr/share/gtk-doc/html/libgtop/libgtop-Uptime.html
/usr/share/gtk-doc/html/libgtop/libgtop-cpu.html
/usr/share/gtk-doc/html/libgtop/libgtop-fsusage.html
/usr/share/gtk-doc/html/libgtop/libgtop-lib.html
/usr/share/gtk-doc/html/libgtop/libgtop-loadavg.html
/usr/share/gtk-doc/html/libgtop/libgtop-mem.html
/usr/share/gtk-doc/html/libgtop/libgtop-mountlist.html
/usr/share/gtk-doc/html/libgtop/libgtop-msg-limits.html
/usr/share/gtk-doc/html/libgtop/libgtop-open.html
/usr/share/gtk-doc/html/libgtop/libgtop-parameter.html
/usr/share/gtk-doc/html/libgtop/libgtop-prockernel.html
/usr/share/gtk-doc/html/libgtop/libgtop-procmap.html
/usr/share/gtk-doc/html/libgtop/libgtop-procmem.html
/usr/share/gtk-doc/html/libgtop/libgtop-procopenfiles.html
/usr/share/gtk-doc/html/libgtop/libgtop-procsegment.html
/usr/share/gtk-doc/html/libgtop/libgtop-procsignal.html
/usr/share/gtk-doc/html/libgtop/libgtop-procstate.html
/usr/share/gtk-doc/html/libgtop/libgtop-procuid.html
/usr/share/gtk-doc/html/libgtop/libgtop-sem-limits.html
/usr/share/gtk-doc/html/libgtop/libgtop-signal.html
/usr/share/gtk-doc/html/libgtop/libgtop-swap.html
/usr/share/gtk-doc/html/libgtop/libgtop-sysdeps.html
/usr/share/gtk-doc/html/libgtop/libgtop-sysinfo.html
/usr/share/gtk-doc/html/libgtop/libgtop-union.html
/usr/share/gtk-doc/html/libgtop/libgtop-version.html
/usr/share/gtk-doc/html/libgtop/libgtop-white-paper-overview.html
/usr/share/gtk-doc/html/libgtop/libgtop-white-paper.html
/usr/share/gtk-doc/html/libgtop/libgtop.devhelp2
/usr/share/gtk-doc/html/libgtop/right-insensitive.png
/usr/share/gtk-doc/html/libgtop/right.png
/usr/share/gtk-doc/html/libgtop/style.css
/usr/share/gtk-doc/html/libgtop/up-insensitive.png
/usr/share/gtk-doc/html/libgtop/up.png

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libgtop2.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgtop-2.0.so.11.1.0
/usr/lib64/libgtop-2.0.so.11
/usr/lib64/libgtop-2.0.so.11.1.0

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/libgtop_daemon2
/V3/usr/libexec/libgtop_server2
/usr/libexec/libgtop_daemon2
/usr/libexec/libgtop_server2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgtop/25953e10e4c2bf3c77db0e6e5f3f9eb9d502d747
/usr/share/package-licenses/libgtop/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files locales -f libgtop.lang
%defattr(-,root,root,-)

