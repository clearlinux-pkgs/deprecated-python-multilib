#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-python-multilib
Version  : 1.2
Release  : 24
URL      : http://pypi.debian.net/python-multilib/python-multilib-1.2.tar.gz
Source0  : http://pypi.debian.net/python-multilib/python-multilib-1.2.tar.gz
Summary  : module for determining if a package is multilib
Group    : Development/Tools
License  : GPL-2.0
Requires: deprecated-python-multilib-license = %{version}-%{release}
Requires: deprecated-python-multilib-python = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-legacypython
BuildRequires : six

%description
# python-multilib
A Python library for determining if a package is multilib or not

%package legacypython
Summary: legacypython components for the deprecated-python-multilib package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-python-multilib package.


%package license
Summary: license components for the deprecated-python-multilib package.
Group: Default

%description license
license components for the deprecated-python-multilib package.


%package python
Summary: python components for the deprecated-python-multilib package.
Group: Default

%description python
python components for the deprecated-python-multilib package.


%prep
%setup -q -n python-multilib-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554327280
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-python-multilib
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-python-multilib/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-python-multilib/LICENSE

%files python
%defattr(-,root,root,-)
