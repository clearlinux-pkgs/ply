#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ply
Version  : 3.9
Release  : 21
URL      : http://pypi.debian.net/ply/ply-3.9.tar.gz
Source0  : http://pypi.debian.net/ply/ply-3.9.tar.gz
Summary  : Python Lex & Yacc
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ply-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This directory mostly contains tests for various types of error
conditions.  To run:

%package python
Summary: python components for the ply package.
Group: Default

%description python
python components for the ply package.


%prep
%setup -q -n ply-3.9

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
