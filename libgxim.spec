%define major	2
%define libname %mklibname gxim %major
%define devname %mklibname -d gxim

%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	GObject-based XIM protocol library
Name:		libgxim
Version:	0.3.3
Release:	14
License:	LGPLv2+
Group:		System/Libraries
Url:		http://code.google.com/p/libgxim/
Source0:	http://libgxim.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:		libgxim-fix-fontset.patch
Patch1:		libgxim-0.3.3-link.patch
Patch2:		libgxim-0.3.3-str-fmt.patch

BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	ruby
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

%package	i18n
Summary:	Translation files for libgxim
Group:		System/Internationalization

%description	i18n
This package contains the translation files for %{name}.

%package -n	%libname
Summary:	Shared library for libgxim
Group:		System/Libraries
Requires:	%{name}-i18n = %{version}-%{release}

%description -n	%libname
libgxim is a X Input Method protocol library that is implemented by GObject.
this library helps you to implement XIM servers or client applications to
communicate through XIM protocol without using Xlib API directly, particularly
if your application uses GObject-based main loop.

This package contains the shared library.

%package -n	%{devname}
Summary:	Development files for libgxim
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	gxim-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development files to make any applications with
libgxim.

%prep
%setup -q
%patch0 -p0 -b .0-fontset
%patch1 -p0 -b .link
%patch2 -p0 -b .str

%build
%configure2_5x \
	--disable-static \
	--disable-rebuilds
%make

%install
%makeinstall_std

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libgxim.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README
%doc %{_datadir}/gtk-doc/html/libgxim
%{_libdir}/libgxim.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgxim

