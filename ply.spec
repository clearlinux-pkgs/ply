#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ply
Version  : 3.11
Release  : 45
URL      : https://files.pythonhosted.org/packages/e5/69/882ee5c9d017149285cab114ebeab373308ef0f874fcdac9beb90e0ac4da/ply-3.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/e5/69/882ee5c9d017149285cab114ebeab373308ef0f874fcdac9beb90e0ac4da/ply-3.11.tar.gz
Summary  : Python Lex & Yacc
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ply-python = %{version}-%{release}
Requires: ply-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Inspired by a September 14, 2006 Salon article "Why Johnny Can't Code" by
David Brin (http://www.salon.com/tech/feature/2006/09/14/basic/index.html),
I thought that a fully working BASIC interpreter might be an interesting,
if not questionable, PLY example.  Uh, okay, so maybe it's just a bad idea,
but in any case, here it is.

%package python
Summary: python components for the ply package.
Group: Default
Requires: ply-python3 = %{version}-%{release}

%description python
python components for the ply package.


%package python3
Summary: python3 components for the ply package.
Group: Default
Requires: python3-core
Provides: pypi(ply)

%description python3
python3 components for the ply package.


%prep
%setup -q -n ply-3.11
cd %{_builddir}/ply-3.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583202741
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
