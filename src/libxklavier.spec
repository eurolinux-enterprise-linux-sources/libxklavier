Name:		libxklavier
Summary:	libXklavier library
Version:	4.0
Release:	1
License:	LGPL
Group:		Development/Libraries
Url: http://gswitchit.sourceforge.net/
BuildRequires: gtk-doc
Source: http://gswitchit.sourceforge.net/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This library allows you simplify XKB-related development.

%package devel
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libxklavier applications.

%prep
%setup -q

%build

CONFIG_FLAGS="--prefix=%{_prefix} --libdir=%{_libdir} \
  --includedir=%{_includedir} --bindir=%{_bindir}"

if [ ! -f configure ]; then
    CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $CONFIG_FLAGS
fi

CFLAGS="$RPM_OPT_FLAGS" ./configure $CONFIG_FLAGS

make 

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR="$RPM_BUILD_ROOT" make install

strip $RPM_BUILD_ROOT%{_libdir}/*.so*
strip $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING.LIB 
%{_libdir}/lib*.so*
%{_datadir}/libxklavier

%files devel
%defattr(-, root, root)

%{_libdir}/pkgconfig/*.pc
%{_libdir}/*a
%{_includedir}/*
%{_datadir}/gtk-doc/html/libxklavier

