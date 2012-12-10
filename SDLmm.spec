%define api	0.1
%define	major	8
%define	lib_name	%mklibname %{name} %{api} %{major}
%define develname	%mklibname %{name} -d

Name:		SDLmm
Summary:	A C++ Wrapper for the Simple DirectMedia Layer
Version:	0.1.8
Release:	17
License:	LGPL
Group:		System/Libraries
Source0:	http://download.sourceforge.net/SDLmm/%{name}-%{version}.tar.bz2
Patch0:		SDLmm-0.1.8-fix-underquoted-calls.patch
Patch1:		SDLmm-0.1.8-link.patch
URL:		http://sdlmm.sourceforge.net/
BuildRequires:	pkgconfig(sdl)

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
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{lib_name}
%doc AUTHORS COPYING
%{_libdir}/libSDLmm-%{api}.so.%{major}*

%files -n %{develname}
%doc docs/html/*.{html,gif} NEWS README
%{_bindir}/sdlmm-config
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%{_mandir}/*/*


%changelog
* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.1.8-16mdv2010.1
+ Revision: 500137
- fix linkage
- new lib policy

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jun 08 2007 Olivier Blin <oblin@mandriva.com> 0.1.8-12mdv2008.0
+ Revision: 37301
- rebuild for directfb (and bunzip patch)
- Import SDLmm



* Thu Jun 22 2006 Lenny Cartier <lenny@mandriva.com> 0.1.8-11mdv2007.0
- rebuild

* Thu Jan 26 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.1.8-10mdk
- fix underquoted calls (P0)
- %%mkrel

* Wed May 04 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.1.8-9mdk
- multiarch
- drop packager tag

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.8-8mdk
- fix summary
- drop .bz2 ending for man pages

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.8-7mdk
- rebuild
- cosmetics

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.8-6mdk
- rebuild
- use %%mklibname macro

* Thu Nov 21 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.1.8-5mdk
- add missing %%{_libdir}/libSDLmm.a

* Mon Sep  2 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.8-4mdk
- rebuild

* Wed May 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.8-3mdk
- recompile against latest libstdc++

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.8-2mdk
- rebuild for new alsa

* Wed Mar  6 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.8-1mdk
- first mdk package
