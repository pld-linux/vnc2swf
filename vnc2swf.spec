Summary:	Screen recorder
Summary(pl):	Nagrywacz obrazu z ekranu
Name:		vnc2swf
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.unixuser.org/~euske/vnc2swf/%{name}-%{version}.tar.gz
# Source0-md5:	57a61191010a15cbbf8d0e3a3ec4ca11
URL:		http://www.unixuser.org/~euske/vnc2swf/
BuildRequires:	autoconf
BuildRequires:	ming-devel = 0.2a
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
Requires:	XFree86-tools
Requires:	ming = 0.2a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vnc2swf is a screen recording tool. Vnc2swf captures the live motion
of a screen with VNC protocol and generates a Macromedia Flash(TM)
movie (.swf).

%description -l pl
Vnc2swf jest narzêdziem rejestruj±cym obraz z ekranu. Dostêp do
ruchomej zawarto¶ci ekranu odbywa siê za po¶rednictwem protoko³u VNC.
Wynikowy plik jest zapisany w formacie filmu Macromedia Flash (.swf).

%description -l ja
Vnc2Swf ¤Ï VNC ¤òÏ¿²è¤·¤Æ Flash ¤ËÊÑ´¹¤¹¤ë¥×¥í¥°¥é¥à¤Ç¤¹¡£

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

cat recordwin.sh | sed s@./vnc2swf@vnc2swf@ > recordwin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vnc2swf recordwin $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/vnc2swf.html TODO sample.html
%attr(755,root,root) %{_bindir}/*
