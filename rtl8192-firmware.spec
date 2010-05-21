Summary:	Firmware for the RTL8192SE chipset
Name:		rtl8192-firmware
Version:	0015
Release:	0.1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://WebUser:pGL7E6v@202.134.71.21/cn/wlan/rtl8192se_linux_2.6.%{version}.0127.2010.tar.gz
# Source0-md5:	39cf0e836d1608fb42f573393260369c
URL:		http://www.realtek.com.tw/downloads/downloadsView.aspx?Langid=1&PNid=48&PFid=48&Level=5&Conn=4&DownTypeID=3&GetDown=false&Downloads=true#2302
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the rtl8192se driver.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterownika rtl8192se.

%prep
%setup -qc
mv rtl8192se_linux_2.6.%{version}.0127.2010/firmware/RTL8192SE firmware

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a firmware/*.bin $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc firmware/Realtek-Firmware-License.txt
/lib/firmware/*
