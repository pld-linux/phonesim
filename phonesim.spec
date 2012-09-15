Summary:	Phone Simulator for modem testing
Summary(pl.UTF-8):	Symulator telefonu do testowania modemów
Name:		phonesim
Version:	1.19
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kernel.org/pub/linux/network/ofono/%{name}-%{version}.tar.xz
# Source0-md5:	9aa7403fb0435d89d59dd32ad27f37ca
URL:		http://ofono.org/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDBus-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtNetwork-devel >= 4
BuildRequires:	QtScript-devel >= 4
BuildRequires:	QtXml-devel >= 4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
