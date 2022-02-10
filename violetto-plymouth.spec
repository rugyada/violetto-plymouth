# Violetto plymouth theme
%define oname Violetto
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	"Violetto" Plymouth theme
Name:		violetto-plymouth
Version:	2.0.1
Release:	1
License:	Creative Commons Attribution-ShareAlike
Group:		System/Kernel and hardware
URL:		https://github.com/rugyada/violetto-plymouth
Source0:	%{oname}-%version.tar.gz
Requires:	plymouth
Requires:	plymouth-plugin-script
Requires:	plymouth-scripts
Requires(post,postun):	plymouth-scripts


%description
This package contains the "Violetto" Plymouth theme.

%files
%{_datadir}/plymouth/themes/Violetto

%post
if [ -x %{_sbindir}/plymouth-set-default-theme ]; then
    export LIB=%{_lib}
    if [ $1 -eq 1 ]; then
        %{_sbindir}/plymouth-set-default-theme --rebuild-initrd Violetto
    else
        THEME=$(%{_sbindir}/plymouth-set-default-theme)
        if [ "$THEME" == "text" -o "$THEME" == "Violetto" ]; then
            %{_sbindir}/plymouth-set-default-theme --rebuild-initrd Violetto
        fi
    fi
fi

%postun
export LIB=%{_lib}
if [ $1 -eq 0 -a -x %{_sbindir}/plymouth-set-default-theme ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "Violetto" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset --rebuild-initrd
    fi
fi

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/

cp -r Violetto %{buildroot}%{_datadir}/plymouth/themes/
