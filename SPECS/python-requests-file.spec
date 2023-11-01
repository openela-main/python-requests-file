%global srcname requests-file

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{srcname}
Version:        1.4.3
Release:        5%{?dist}
Summary:        Transport adapter for using file:// URLs with python-requests

License:        ASL 2.0
URL:            https://github.com/dashea/requests-file
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Requests-File is a transport adapter for use with the Requests Python
library to allow local file system access via file:// URLs.

This is the Python 2 version of the requests_file module

%if %{with python2}
%package -n python2-%{srcname}
Summary:        Transport adapter for using file:// URLs with python-requests
%{?python_provide:%python_provide python2-%{srcname}}

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-requests
BuildRequires:  python-six

Requires:       python-requests
Requires:       python-six
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-requests
BuildRequires:  python2-six

Requires:       python2-requests
Requires:       python2-six
%endif

%description -n python2-%{srcname}
Requests-File is a transport adapter for use with the Requests Python
library to allow local file system access via file:// URLs.

This is the Python 2 version of the requests_file module
%endif

%if %{with python3}
%package -n python3-requests-file
Summary:        Transport adapter for using file:// URLs with python3-requests
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-six

Requires:       python3-requests
Requires:       python3-six

%description -n python3-requests-file
Requests-File is a transport adapter for use with the Requests Python
library to allow local file system access via file:// URLs.

This is the Python 3 version of the requests_file module
%endif

%prep
%autosetup -n %{srcname}-%{version}
rm -rf requests_file.egg-info

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%check
%if %{with python2}
%{__python2} setup.py test
%endif
%if %{with python3}
%{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/requests_file.py*
%{python2_sitelib}/requests_file*.egg-info*
%endif

%if %{with python3}
%files -n python3-requests-file
%license LICENSE
%doc README.rst
%{python3_sitelib}/requests_file.py*
%{python3_sitelib}/__pycache__/requests_file.*
%{python3_sitelib}/requests_file*.egg-info*
%endif

%changelog
* Fri Mar 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.3-6
- Don't build Python 2 subpackage on EL > 7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb  7 2018 Eli Young <elyscape@gmail.com> - 1.4.3-3
- Package for EPEL7

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan  3 2018 David Shea <dshea@redhat.com> - 1.4.3-1
- Update to requests-file-1.4.3, which sets the response URL to the request URL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis cstratak@redhat.com> - 1.4-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 1.4-2
- Rebuilt for Python3.5 rebuild

* Mon Sep 14 2015 David Shea <dshea@redhat.com> - 1.4-1
- Use getprerredencoding instead of nl_langinfo
- Handle files with a drive component
- Switch to the new Fedora packaging guidelines, which renames python-requests-file to python2-requests-file

* Mon May 18 2015 David Shea <dshea@redhat.com> - 1.3.1-1
- Add python version classifiers to the package info

* Mon May 18 2015 David Shea <dshea@redhat.com> - 1.3-1
- Fix a crash when closing a file response.
- Use named aliases instead of integers for status codes.

* Fri May  8 2015 David Shea <dshea@redhat.com> - 1.2-1
- Added support for HEAD requests

* Thu Mar 12 2015 David Shea <dshea@redhat.com> - 1.1-1
- Added handing for %% escapes in URLs
- Proofread the README

* Tue Mar 10 2015 David Shea <dshea@redhat.com> - 1.0-1
- Initial package
