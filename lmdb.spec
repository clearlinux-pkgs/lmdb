#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lmdb
Version  : LMDB_0.9.18
Release  : 1
URL      : https://github.com/LMDB/lmdb/archive/LMDB_0.9.18.tar.gz
Source0  : https://github.com/LMDB/lmdb/archive/LMDB_0.9.18.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OLDAP-2.8

%description
No detailed description available

%package dev
Summary: dev components for the lmdb package.
Group: Development
Provides: lmdb-devel

%description dev
dev components for the lmdb package.


%prep
%setup -q -n lmdb-LMDB_0.9.18

%build
pushd libraries/liblmdb/
make V=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd libraries/liblmdb/
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/local/bin/mdb_copy
/usr/local/bin/mdb_dump
/usr/local/bin/mdb_load
/usr/local/bin/mdb_stat
/usr/local/lib/liblmdb.so
/usr/local/share/man/man1/mdb_copy.1
/usr/local/share/man/man1/mdb_dump.1
/usr/local/share/man/man1/mdb_load.1
/usr/local/share/man/man1/mdb_stat.1

%files dev
%defattr(-,root,root,-)
/usr/local/include/lmdb.h
