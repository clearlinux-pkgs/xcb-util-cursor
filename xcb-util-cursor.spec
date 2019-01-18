#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xcb-util-cursor
Version  : 0.1.3
Release  : 5
URL      : https://xcb.freedesktop.org/dist/xcb-util-cursor-0.1.3.tar.gz
Source0  : https://xcb.freedesktop.org/dist/xcb-util-cursor-0.1.3.tar.gz
Summary  : XCB cursor utility library
Group    : Development/Tools
License  : MIT
Requires: xcb-util-cursor-lib
BuildRequires : doxygen
BuildRequires : pkgconfig(xcb-image)
BuildRequires : pkgconfig(xcb-render)
BuildRequires : pkgconfig(xcb-renderutil)
BuildRequires : pkgconfig(xorg-macros)

%description
About XCB util modules
======================
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package dev
Summary: dev components for the xcb-util-cursor package.
Group: Development
Requires: xcb-util-cursor-lib
Provides: xcb-util-cursor-devel

%description dev
dev components for the xcb-util-cursor package.


%package lib
Summary: lib components for the xcb-util-cursor package.
Group: Libraries

%description lib
lib components for the xcb-util-cursor package.


%prep
%setup -q -n xcb-util-cursor-0.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525194739
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1525194739
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/xcb/xcb_cursor.h
/usr/lib64/libxcb-cursor.so
/usr/lib64/pkgconfig/xcb-cursor.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxcb-cursor.so.0
/usr/lib64/libxcb-cursor.so.0.0.0
