#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lmdb
Version  : 0.9.23
Release  : 12
URL      : https://github.com/LMDB/lmdb/archive/LMDB_0.9.23.tar.gz
Source0  : https://github.com/LMDB/lmdb/archive/LMDB_0.9.23.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OLDAP-2.8
Requires: lmdb-bin = %{version}-%{release}
Requires: lmdb-license = %{version}-%{release}
Requires: lmdb-man = %{version}-%{release}
Patch1: build.patch

%description
No detailed description available

%package bin
Summary: bin components for the lmdb package.
Group: Binaries
Requires: lmdb-license = %{version}-%{release}
Requires: lmdb-man = %{version}-%{release}

%description bin
bin components for the lmdb package.


%package dev
Summary: dev components for the lmdb package.
Group: Development
Requires: lmdb-bin = %{version}-%{release}
Provides: lmdb-devel = %{version}-%{release}

%description dev
dev components for the lmdb package.


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
%setup -q -n lmdb-LMDB_0.9.23
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545411101
pushd libraries/liblmdb/
make  %{?_smp_mflags}
popd


%install
export SOURCE_DATE_EPOCH=1545411101
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lmdb
cp libraries/liblmdb/COPYRIGHT %{buildroot}/usr/share/package-licenses/lmdb/libraries_liblmdb_COPYRIGHT
cp libraries/liblmdb/LICENSE %{buildroot}/usr/share/package-licenses/lmdb/libraries_liblmdb_LICENSE
pushd libraries/liblmdb/
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
/usr/include/*.h
/usr/lib64/liblmdb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lmdb/libraries_liblmdb_COPYRIGHT
/usr/share/package-licenses/lmdb/libraries_liblmdb_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mdb_copy.1
/usr/share/man/man1/mdb_dump.1
/usr/share/man/man1/mdb_load.1
/usr/share/man/man1/mdb_stat.1
