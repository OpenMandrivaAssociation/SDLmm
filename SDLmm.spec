%define	name	SDLmm
%define	version	0.1.8
%define	release	%mkrel 16

%define api	0.1
%define	major	8
%define	lib_name	%mklibname %{name} %{api} %{major}
%define develname	%mklibname %{name} -d

Name:		%{name}
Summary:	A C++ Wrapper for the Simple DirectMedia Layer
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
Source0:	http://download.sourceforge.net/SDLmm/%{name}-%{version}.tar.bz2
Patch0:		SDLmm-0.1.8-fix-underquoted-calls.patch
Patch1:		SDLmm-0.1.8-link.patch
URL:		http://sdlmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel

%description
SDLmm is a C++ glue for SDL, or the Simple DirectMedia Layer, which is a
generic API that provides low level access to audio, keyboard, mouse,
joystick, 3D hardware via OpenGL, and 2D framebuffer across multiple
platforms.

SDLmm aims to stay as close as possible to the C API while taking
advantage of native C++ features like object orientation.

%package -n	%{lib_name}
Summary:	Main library for SDLmm
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}SDLmm0.1 < 0.1.8-16

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with SDLmm.

%package -n	%{develname}
Summary:	Headers for developing programs that will use SDLmm
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}SDLmm0.1-devel < 0.1.8-16

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use SDLmm, the C++ interface to SDL.

%prep
%setup -q
%patch0 -p1 -b .underquoted
%patch1 -p0 -b .link

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#multiarch
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/sdlmm-config

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_libdir}/libSDLmm-%{api}.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc docs/html/*.{html,gif} NEWS README
%{_bindir}/sdlmm-config
%multiarch %{multiarch_bindir}/sdlmm-config
%{_includedir}/*
%{_libdir}/*.?a
%{_libdir}/libSDLmm.a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_mandir}/*/*
