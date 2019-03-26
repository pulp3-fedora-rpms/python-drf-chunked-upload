# Created by pyp2rpm-3.3.2
%global pypi_name drf-chunked-upload

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        1%{?dist}
Summary:        Upload large files to Django REST Framework in multiple chunks, with the ability to resume if the upload is interrupted

License:        MIT-Zero
URL:            https://github.com/jkeifer/drf-chunked-upload
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
drf-chunked-upload This simple django app enables users to upload large files
to Django Rest Framework in multiple chunks, with the ability to resume if the
upload is interrupted.This app is based to a large degree on the work of Julio
Malegria < specifically his django-chunked-upload app < MIT-Zero < Install via
pip::: pip install drf-chunked-uploadAnd then add it to your Django...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
drf-chunked-upload This simple django app enables users to upload large files
to Django Rest Framework in multiple chunks, with the ability to resume if the
upload is interrupted.This app is based to a large degree on the work of Julio
Malegria < specifically his django-chunked-upload app < MIT-Zero < Install via
pip::: pip install drf-chunked-uploadAnd then add it to your Django...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/drf_chunked_upload
%{python3_sitelib}/drf_chunked_upload-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 0.4.2-1
- Initial package.