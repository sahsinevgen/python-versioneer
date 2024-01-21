%define _unpackaged_files_terminate_build 1
%define pypi_name versioneer

%def_without check

Name: python3-module-%pypi_name
Version: 0.29
Release: alt1

Summary: Easy VCS-based management of project version strings
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/versioneer/
Vcs: https://github.com/python-versioneer/python-versioneer

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Versioneer is a tool to automatically update version strings (in setup.py and
the conventional 'from PROJECT import _version' pattern) by asking your
version-control system about the current tree.

%prep
%setup

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir_noarch/%pypi_name.py
%python3_sitelibdir_noarch/__pycache__/%pypi_name.cpython-*
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jan 22 2024 Alexandr Sinelnikov <sasha@altlinux.org> 0.29-alt1
- Initial build for Sisyphus

