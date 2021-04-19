%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1
%global sname sushy

%global common_desc \
Sushy is a Python library to communicate with Redfish based systems (http://redfish.dmtf.org)

%global common_desc_tests Tests for Sushy

Name: python-%{sname}
Version: 3.2.1
Release: 1%{?dist}
Summary: Sushy is a Python library to communicate with Redfish based systems
License: ASL 2.0
URL: http://launchpad.net/%{sname}/

Source0: http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz

BuildArch: noarch

%description
%{common_desc}

%package -n python3-%{sname}
Summary: Sushy is a Python library to communicate with Redfish based systems
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: git
BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
# For running unit tests during check phase
BuildRequires: python3-requests
BuildRequires: python3-dateutil
BuildRequires: python3-stevedore

Requires: python3-pbr >= 2.0.0
Requires: python3-requests >= 2.14.2
Requires: python3-dateutil
Requires: python3-stevedore >= 1.29.0

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

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: Sushy documentation

BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-openstackdocstheme

%description -n python-%{sname}-doc
Documentation for Sushy
%endif

%prep
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%check
%{__python3} setup.py test

%install
%{py3_install}

%files -n python3-%{sname}
%license LICENSE
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Mon Apr 19 2021 RDO <dev@lists.rdoproject.org> 3.2.1-1
- Update to 3.2.1

* Mon Apr 27 2020 RDO <dev@lists.rdoproject.org> 3.2.0-1
- Update to 3.2.0

