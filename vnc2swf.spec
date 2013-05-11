Summary:	Screen Recorder which saves a VNC session as a .swf file
Summary(pl.UTF-8):	Nagrywacz obrazu z ekranu
Name:		vnc2swf
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.unixuser.org/~euske/vnc2swf/%{name}-%{version}.tar.gz
# Source0-md5:	2eed9cd91cff76e69004c905660b00ae
Patch0:		%{name}-link.patch
URL:		http://www.unixuser.org/~euske/vnc2swf/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
# for recordwin
Requires:	awk
Requires:	x11vnc
Requires:	xorg-app-xwininfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vnc2swf is a screen recording tool. Vnc2swf captures the live motion
of a screen with VNC protocol and generates a Macromedia Flash(TM)
movie (.swf).

%description -l pl.UTF-8
Vnc2swf jest narzędziem rejestrującym obraz z ekranu. Dostęp do
ruchomej zawartości ekranu odbywa się za pośrednictwem protokołu VNC.
Wynikowy plik jest zapisany w formacie filmu Macromedia Flash (.swf).

%description -l ja.UTF-8
Vnc2Swf は VNC を録画して Flash に変換するプログラムです。

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vnc2swf $RPM_BUILD_ROOT%{_bindir}
install recordwin.sh $RPM_BUILD_ROOT%{_bindir}/recordwin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{recordwin,vnc2swf}.html
%attr(755,root,root) %{_bindir}/vnc2swf
%attr(755,root,root) %{_bindir}/recordwin
