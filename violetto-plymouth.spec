# Violetto plymouth theme
%define oname Violetto
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Violetto theme for Plymouth
Name:		violetto-plymouth
Version:	2.0.1
Release:	2
License:	Creative Commons Attribution-ShareAlike
Group:		System/Kernel and hardware
URL:		https://github.com/rugyada/violetto-plymouth
Source0:	%{oname}-%version.tar.gz
Requires:	plymouth
Requires:	plymouth-plugin-script
Requires:	plymouth-scripts
BuildArch:	noarch

%description
Violetto theme for Plymouth

%files
%{_datadir}/plymouth/themes/Violetto

%prep
%setup -qn %{oname}-%{version}

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/Violetto
cp -rf * %{buildroot}%{_datadir}/plymouth/themes/
