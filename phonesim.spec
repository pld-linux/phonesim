Summary:	Phone Simulator for modem testing
Summary(pl.UTF-8):	Symulator telefonu do testowania modemów
Name:		phonesim
Version:	2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://www.kernel.org/pub/linux/network/ofono/%{name}-%{version}.tar.xz
# Source0-md5:	48ac291bdf726f0bc25f7ac445a8adb9
URL:		http://ofono.org/
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Qml-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5.10
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Widgets >= 5.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phone Simulator for modem testing. It's used by oFono project.

%description -l pl.UTF-8
Symulator telefonu do testowania modemów. Jest używany przez projekt
oFono.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/phonesim
%dir %{_datadir}/phonesim
%{_datadir}/phonesim/default.xml
