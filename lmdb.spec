#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v12
# autospec commit: 381dfd8
#
Name     : lmdb
Version  : 0.9.31
Release  : 21
URL      : https://github.com/LMDB/lmdb/archive/LMDB_0.9.31/lmdb-0.9.31.tar.gz
Source0  : https://github.com/LMDB/lmdb/archive/LMDB_0.9.31/lmdb-0.9.31.tar.gz
Summary  : Key-value embedded data store
Group    : Development/Tools
License  : OLDAP-2.8
Requires: lmdb-bin = %{version}-%{release}
Requires: lmdb-lib = %{version}-%{release}
Requires: lmdb-license = %{version}-%{release}
Requires: lmdb-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: build.patch
Patch2: 0001-install-pkgconfig-descriptor.patch
Patch3: 0002-Add-soname-for-liblmdb.so.patch

%description
Symas LMDB is an extraordinarily fast, memory-efficient database we developed
for the OpenLDAP Project. With memory-mapped files, it has the read performance
of a pure in-memory database while retaining the persistence of standard
disk-based databases.

%package bin
Summary: bin components for the lmdb package.
Group: Binaries
Requires: lmdb-license = %{version}-%{release}

%description bin
bin components for the lmdb package.


%package dev
Summary: dev components for the lmdb package.
Group: Development
Requires: lmdb-lib = %{version}-%{release}
Requires: lmdb-bin = %{version}-%{release}
Provides: lmdb-devel = %{version}-%{release}
Requires: lmdb = %{version}-%{release}

%description dev
dev components for the lmdb package.


%package lib
Summary: lib components for the lmdb package.
Group: Libraries
Requires: lmdb-license = %{version}-%{release}

%description lib
lib components for the lmdb package.


%package license
Summary: license components for the lmdb package.
Group: Default

%description license
license components for the lmdb package.


%package man
Summary: man components for the lmdb package.
Group: Default

%description man
man components for the lmdb package.


%prep
%setup -q -n lmdb-LMDB_0.9.31
cd %{_builddir}/lmdb-LMDB_0.9.31
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719529377
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
pushd libraries/liblmdb/
export GOAMD64=v2
make  %{?_smp_mflags}  XCFLAGS="$CFLAGS"
popd


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
export SOURCE_DATE_EPOCH=1719529377
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lmdb
cp %{_builddir}/lmdb-LMDB_%{version}/libraries/liblmdb/COPYRIGHT %{buildroot}/usr/share/package-licenses/lmdb/7578422c24f1c556f2a5884294bdf7a545a53a64 || :
cp %{_builddir}/lmdb-LMDB_%{version}/libraries/liblmdb/LICENSE %{buildroot}/usr/share/package-licenses/lmdb/bc06cbdf781c87d2df2fe385214f936d010dd2a2 || :
export GOAMD64=v2
pushd libraries/liblmdb/
GOAMD64=v2
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mdb_copy
/usr/bin/mdb_dump
/usr/bin/mdb_load
/usr/bin/mdb_stat

%files dev
%defattr(-,root,root,-)
/usr/include/lmdb.h
/usr/lib64/pkgconfig/lmdb.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblmdb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lmdb/7578422c24f1c556f2a5884294bdf7a545a53a64
/usr/share/package-licenses/lmdb/bc06cbdf781c87d2df2fe385214f936d010dd2a2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mdb_copy.1
/usr/share/man/man1/mdb_dump.1
/usr/share/man/man1/mdb_load.1
/usr/share/man/man1/mdb_stat.1
