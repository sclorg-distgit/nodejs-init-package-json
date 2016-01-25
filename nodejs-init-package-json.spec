%{?scl:%scl_package nodejs-init-package-json}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-init-package-json
Version:        1.9.1
Release:        1%{?dist}
Summary:        A node module to get your node module started
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/isaacs/init-package-json
Source0:        http://registry.npmjs.org/init-package-json/-/init-package-json-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A node module to get your node module started, by creating its package.json
metadata file.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/init-package-json
cp -pr default-input.js init-package-json.js package.json %{buildroot}%{nodejs_sitelib}/init-package-json

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/init-package-json
%doc README.md example/example-basic.js  example/example-default.js  example/example-npm.js
%changelog
* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.9.1-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- New upstream release 1.0.0

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.0.14-1
- New upstream release 0.0.14

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.10-2
- replace provides and requires with macro


* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.10-1
- new upstream release 0.0.10

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-6
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-5
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.7-5
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-3
- use HTTP in Source0 instead of HTTPS

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-2
- add missing build section
- improve description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-1
- initial package generated by npm2rpm
