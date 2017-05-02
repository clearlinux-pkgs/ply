#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ply
Version  : 3.10
Release  : 25
URL      : http://pypi.debian.net/ply/ply-3.10.tar.gz
Source0  : http://pypi.debian.net/ply/ply-3.10.tar.gz
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
%setup -q -n ply-3.10

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487184112
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487184112
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
