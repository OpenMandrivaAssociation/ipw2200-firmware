Name: ipw2200-firmware
Version: 3.1
Release: %mkrel 1
Summary: Intel PRO/Wireless 2200BG firmware
Source: ipw2200-fw-%{version}.tgz
License: Proprietary
Group: System/Kernel and hardware
URL: http://ipw2200.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
Firmware for Intel PRO/Wireless 2200BG (IPW2200) mini PCI adapter support.

%prep
%setup -q -n ipw2200-fw-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.fw %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE.*
/lib/firmware/*.fw

