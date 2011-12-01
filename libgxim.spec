%define major 2
%define libname %mklibname gxim %major
%define develname %mklibname -d gxim

Name:		libgxim
Version:	0.3.3
Release:	%mkrel 2
License:	LGPLv2+
URL:		http://code.google.com/p/libgxim/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	intltool gettext ruby
BuildRequires:	dbus-devel > 0.23
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	glib2-devel >= 2.16
BuildRequires:	gtk2-devel
Source0:	http://libgxim.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:		libgxim-fix-fontset.patch
Patch1:		libgxim-0.3.3-link.patch
Patch2:		libgxim-0.3.3-str-fmt.patch
Summary:	GObject-based XIM protocol library
Group:		System/Libraries

%description
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

%package	i18n
Summary:	Translation files for libgxim
Group:		System/Internationalization

%description	i18n
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the translation files.

%package -n	%libname
Summary:	Shared library for libgxim
Group:		System/Libraries
Requires:	%{name}-i18n = %version

%description -n	%libname
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the shared library.

%package -n	%develname
Summary:	Development files for libgxim
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	gxim-devel = %{version}-%{release}

%description -n	%develname
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the development files to make any applications with
libgxim.

%prep
%setup -q
%patch0 -p0 -b .0-fontset
%patch1 -p0 -b .link
%patch2 -p0 -b .str

%build
%configure2_5x --disable-static --disable-rebuilds
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files i18n -f %{name}.lang
%defattr(-, root, root, -)

%files -n %{libname}
%defattr(-, root, root, -)
%{_libdir}/libgxim.so.%{major}
%{_libdir}/libgxim.so.%{major}.*

%files -n %{develname}
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libgxim.so
%{_libdir}/libgxim.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgxim
%{_datadir}/gtk-doc/html/libgxim
