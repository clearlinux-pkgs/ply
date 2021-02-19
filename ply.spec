#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ply
Version  : 3.11
Release  : 50
URL      : https://files.pythonhosted.org/packages/e5/69/882ee5c9d017149285cab114ebeab373308ef0f874fcdac9beb90e0ac4da/ply-3.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/e5/69/882ee5c9d017149285cab114ebeab373308ef0f874fcdac9beb90e0ac4da/ply-3.11.tar.gz
Summary  : Python Lex & Yacc
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ply-python = %{version}-%{release}
Requires: ply-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PLY is yet another implementation of lex and yacc for Python. Some notable
        features include the fact that its implemented entirely in Python and it
        uses LALR(1) parsing which is efficient and well suited for larger grammars.
        
        PLY provides most of the standard lex/yacc features including support for empty 
        productions, precedence rules, error recovery, and support for ambiguous grammars. 
        
        PLY is extremely easy to use and provides very extensive error checking. 
        It is compatible with both Python 2 and Python 3.

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
export SOURCE_DATE_EPOCH=1603398918
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
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
