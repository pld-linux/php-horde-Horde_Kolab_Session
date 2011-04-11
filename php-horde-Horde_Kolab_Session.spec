%define		status		stable
%define		pearname	Horde_Kolab_Session
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A package managing an active Kolab session
Name:		php-horde-Horde_Kolab_Session
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	9d996ac76c0497515a0dc6c105f8e39c
URL:		http://pear.horde.org/package/Horde_Kolab_Session/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Kolab_Server < 2.0.0
Requires:	php-pear
Suggests:	php-horde-Horde_Log
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Log.*)

%description
This package handles a Kolab session. It allows to authenticate
against LDAP and provides the users storage locations.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Kolab/Session.php
%{php_pear_dir}/Horde/Kolab/Session
