%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname sushy

%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc \
Sushy is a Python library to communicate with Redfish based systems (http://redfish.dmtf.org)

%global common_desc_tests Tests for Sushy

Name: python-%{sname}
Version: 1.3.1
Release: 1%{?dist}
Summary: Sushy is a Python library to communicate with Redfish based systems
License: ASL 2.0
URL: http://launchpad.net/%{sname}/

Source0: http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
%{common_desc}

%package -n python2-%{sname}
Summary: Sushy is a Python library to communicate with Redfish based systems
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: git
BuildRequires: python2-devel
BuildRequires: python2-pbr
BuildRequires: python2-setuptools
# For running unit tests during check phase
BuildRequires: python2-requests
BuildRequires: python2-six

Requires: python2-pbr >= 2.0.0
Requires: python2-six >= 1.10.0
Requires: python2-requests >= 2.14.2

%description -n python2-%{sname}
%{common_desc}

%package -n python2-%{sname}-tests
Summary: Sushy tests
Requires: python2-%{sname} = %{version}-%{release}

BuildRequires: python2-oslotest
BuildRequires: python2-testrepository
BuildRequires: python2-testscenarios
BuildRequires: python2-testtools

Requires: python2-oslotest
Requires: python2-testrepository
Requires: python2-testscenarios
Requires: python2-testtools

%description -n python2-%{sname}-tests
%{common_desc_tests}

%if 0%{?with_python3}

%package -n python3-%{sname}
Summary: Sushy is a Python library to communicate with Redfish based systems

%{?python_provide:%python_provide python3-%{sname}}
BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
# For running unit tests during check phase
BuildRequires: python3-requests
BuildRequires: python3-six

Requires: python3-pbr >= 2.0.0
Requires: python3-six >= 1.10.0
Requires: python3-requests >= 2.14.2

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: Sushy tests
Requires: python3-%{sname} = %{version}-%{release}

BuildRequires: python3-oslotest
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools

Requires: python3-oslotest
Requires: python3-testrepository
Requires: python3-testscenarios
Requires: python3-testtools

%description -n python3-%{sname}-tests
%{common_desc_tests}

%endif # with_python3

%package -n python-%{sname}-doc
Summary: Sushy documentation

BuildRequires: python-sphinx
BuildRequires: python-openstackdocstheme

%description -n python-%{sname}-doc
Documentation for Sushy

%prep
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif # with_python3

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif # with_python3

%files -n python2-%{sname}
%license LICENSE
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}-*.egg-info
%exclude %{python2_sitelib}/%{sname}/tests

%files -n python2-%{sname}-tests
%license LICENSE
%{python2_sitelib}/%{sname}/tests

%if 0%{?with_python3}

%files -n python3-%{sname}
%license LICENSE
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%endif # with_python3

%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
* Tue Feb 13 2018 RDO <dev@lists.rdoproject.org> 1.3.1-1
- Update to 1.3.1

