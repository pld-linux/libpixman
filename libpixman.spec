Summary:	Pixel manipulation library
Summary:	Biblioteka operacji na pikselach
Name:		libpixman
Version:	0.1.5
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	756107dd2b23553df2f85cd92cab82d5
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

%description -l pl
libpixman to biblioteka do operacji na pikselach. Jest po³±czeniem
libpixregion i libic.

libpixregion by³a ogóln± bibliotek± do przetwarzania obszarów
pikselowych. Obszar pikselowy (PixRegion) to zbiór prostok±tów
ograniczonych Y-X pokrywaj±cych ¿±dany obszar.

libic by³a ogóln± bibliotek± mieszania obrazów. libic udostêpnia³a
mieszanie obrazów metod± Portera-Duffa oraz po¶rednie generowanie
masek dla prymitywów geometrycznych obejmuj±cych trapezoidy, trójk±ty
i prostok±ty.

%package devel
Summary:	Development files for libpixregion
Summary(pl):	Pliki dla programistów do biblioteki libpixregion
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libic-devel
Obsoletes:	libpixregion-devel
Obsoletes:	slim

%description devel
This package contains development files for libpixregion library.

%description devel -l pl
Ten pakiet zawiera pliki dla programistów korzystaj±cych z biblioteki
libpixregion.

%package static
Summary:	Static libpixman library
Summary(pl):	Statyczna biblioteka libpixman
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libic-static
Obsoletes:	libpixregion-static

%description static
This package contains static libpixman library.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki libpixman.

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
