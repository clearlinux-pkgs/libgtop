#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgtop
Version  : 2.40.0
Release  : 13
URL      : https://download.gnome.org/sources/libgtop/2.40/libgtop-2.40.0.tar.xz
Source0  : https://download.gnome.org/sources/libgtop/2.40/libgtop-2.40.0.tar.xz
Summary  : LibGTop library
Group    : Development/Tools
License  : GPL-2.0
Requires: libgtop-bin = %{version}-%{release}
Requires: libgtop-data = %{version}-%{release}
Requires: libgtop-info = %{version}-%{release}
Requires: libgtop-lib = %{version}-%{release}
Requires: libgtop-license = %{version}-%{release}
Requires: libgtop-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc.

On Linux systems, these information are taken directly from the /proc
filesystem while on other systems a server is used to read those
information from /dev/kmem or whatever.

%package bin
Summary: bin components for the libgtop package.
Group: Binaries
Requires: libgtop-data = %{version}-%{release}
Requires: libgtop-license = %{version}-%{release}

%description bin
bin components for the libgtop package.


%package data
Summary: data components for the libgtop package.
Group: Data

%description data
data components for the libgtop package.


%package dev
Summary: dev components for the libgtop package.
Group: Development
Requires: libgtop-lib = %{version}-%{release}
Requires: libgtop-bin = %{version}-%{release}
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
Requires: libgtop-license = %{version}-%{release}

%description lib
lib components for the libgtop package.


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
%setup -q -n libgtop-2.40.0
cd %{_builddir}/libgtop-2.40.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586240920
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1586240920
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgtop
cp %{_builddir}/libgtop-2.40.0/COPYING %{buildroot}/usr/share/package-licenses/libgtop/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/libgtop-2.40.0/copyright.txt %{buildroot}/usr/share/package-licenses/libgtop/25953e10e4c2bf3c77db0e6e5f3f9eb9d502d747
%make_install
%find_lang libgtop

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libgtop_daemon2
/usr/bin/libgtop_server2

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
/usr/lib64/libgtop-2.0.so.11
/usr/lib64/libgtop-2.0.so.11.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgtop/25953e10e4c2bf3c77db0e6e5f3f9eb9d502d747
/usr/share/package-licenses/libgtop/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files locales -f libgtop.lang
%defattr(-,root,root,-)

