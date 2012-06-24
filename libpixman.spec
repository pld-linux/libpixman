Summary:	Pixel manipulation library
Summary:	Biblioteka operacji na pikselach
Name:		libpixman
Version:	0.1.6
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	4af4bbf35840016f40f287a0bb6526b1
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libic
Obsoletes:	libpixregion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpixman is a pixel manipulation library. It is a merge of
libpixregion and libic.

libpixregion was a generic library for manipulating pixel regions (a
PixRegion is a set of Y-X banded rectangles that cover the desired
region).

libic was a generic image compositing library. libic provided
Porter/Duff compositing of images and implicit mask generation for
geometric primitives including trapezoids, triangles, and rectangles.

%description -l pl.UTF-8
libpixman to biblioteka do operacji na pikselach. Jest połączeniem
libpixregion i libic.

libpixregion była ogólną biblioteką do przetwarzania obszarów
pikselowych. Obszar pikselowy (PixRegion) to zbiór prostokątów
ograniczonych Y-X pokrywających żądany obszar.

libic była ogólną biblioteką mieszania obrazów. libic udostępniała
mieszanie obrazów metodą Portera-Duffa oraz pośrednie generowanie
masek dla prymitywów geometrycznych obejmujących trapezoidy, trójkąty
i prostokąty.

%package devel
Summary:	Development files for libpixregion
Summary(pl.UTF-8):   Pliki dla programistów do biblioteki libpixregion
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libic-devel
Obsoletes:	libpixregion-devel
Obsoletes:	slim

%description devel
This package contains development files for libpixregion library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki dla programistów korzystających z biblioteki
libpixregion.

%package static
Summary:	Static libpixman library
Summary(pl.UTF-8):   Statyczna biblioteka libpixman
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libic-static
Obsoletes:	libpixregion-static

%description static
This package contains static libpixman library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki libpixman.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog* NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
