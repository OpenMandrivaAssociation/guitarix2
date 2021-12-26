%define debug_package          %{nil}

%define ladspadir %{_libdir}/ladspa
%define lv2dir %{_libdir}/lv2

%define major 0
%define libgxw %mklibname gxw %{major}
%define libgxwmm %mklibname gxwmm %{major}

Summary:	Guitar effect processor for JACK
Name:		guitarix2
Version:	0.43.1
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://guitarix.org
Source0:       https://downloads.sourceforge.net/project/guitarix/guitarix/guitarix2-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	faust
BuildRequires:	intltool
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
BuildRequires:	ladspa-devel
BuildRequires:	libzita-convolver-devel
BuildRequires:	libzita-resampler-devel
BuildRequires:	pkgconfig(avahi-gobject)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lrdf)
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(sndfile)
BuildRequires: pkgconfig(raptor2)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: gperf
BuildRequires: eigen3-devel
BuildRequires: python
BuildRequires: sassc
BuildRequires: waf
BuildRequires: pkgconfig(glibmm-2.4)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(gtk+-3.0)

Requires:	%{name}-plugins-ladspa = %{EVRD}
Provides:	guitarix = %{EVRD}
Obsoletes:	%{_lib}gxw-devel < 0.28.1-2

%description
Guitarix is a simple Linux Rock Guitar Amplifier for the Jack Audio
Connektion Kit with one input and two outputs. Designed to get nice
thrash/metal/rock/blues guitar sounds. There are controls for bass,
middle, treble, gain (in/out), compressor, preamp, tube's, drive,
overdrive, oversample, anti-alias, fuzz, balance, distortion, freeverb,
impulse response, vibrato, chorus, delay , cry-baby(wah) and echo.

%files -f guitarix.lang
%doc README
%{_bindir}/guitarix
%{_datadir}/pixmaps/*.png
%{_datadir}/gx_head/skins/*.jpg
%{_datadir}/gx_head/skins/*.png
%{_datadir}/gx_head/skins/*.svg
%{_datadir}/gx_head/skins/*.rc
%{_datadir}/gx_head/skins/LV2/*.rc
%{_datadir}/gx_head/sounds/*
%{_datadir}/gx_head/builder/*
%{_datadir}/gx_head/factorysettings/*
%{_datadir}/applications/guitarix.desktop

#----------------------------------------------------------------------------

%package plugins-ladspa
Summary:	LADSPA plugins coming with guitarix2
Group:		Sound
Requires:	ladspa

%description plugins-ladspa
Guitarix is a simple Linux Rock Guitar Amplifier for the Jack Audio
Connektion Kit. This package includes the LADSPA plugins for the amp,
which can be used with other LADSPA hosts as well.

%files plugins-ladspa
%dir %{ladspadir}
%{ladspadir}/*.so
%{_datadir}/ladspa/rdf/*.rdf

#----------------------------------------------------------------------------

%package plugins-lv2
Summary:	LV2 plugins coming with guitarix2
Group:		Sound
Requires:	lv2

%description plugins-lv2
Guitarix is a simple Linux Rock Guitar Amplifier for the Jack Audio
Connektion Kit. This package includes the LV2 plugins for the amp,
which can be used with LV2 hosts.

%files plugins-lv2
%dir %{_libdir}/lv2
%{_libdir}/lv2/*
%{_datadir}/gx_head/skins/LV2/*.png

#----------------------------------------------------------------------------

%package -n %{libgxw}
Summary:	Libraries required for guitarix LV2 plugins
Group:		Sound
Conflicts:	%{_lib}gxw1 < 0.28.1-2
Obsoletes:	%{_lib}gxw1 < 0.28.1-2

%description -n %{libgxw}
Libraries required for guitarix LV2 plugins.

%files -n %{libgxw}
%{_libdir}/libgxw.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgxwmm}
Summary:	Libraries required for guitarix LV2 plugins
Group:		Sound
Conflicts:	%{_lib}gxw1 < 0.28.1-2
Obsoletes:	%{_lib}gxw1 < 0.28.1-2

%description -n %{libgxwmm}
Libraries required for guitarix LV2 plugins.

%files -n %{libgxwmm}
%{_libdir}/libgxwmm.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q -n guitarix-%{version}

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--ladspadir=%{ladspadir} \
	--no-faust \
	--lv2dir=%{lv2dir}

./waf build

%install
./waf install --destdir=%{buildroot}
desktop-file-install \
	--remove-category="X-Jack;" \
	--remove-category="Midi;" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

# These are not needed, we don't have header files to use
rm -f %{buildroot}%{_libdir}/libgxw.so
rm -f %{buildroot}%{_libdir}/libgxwmm.so

%find_lang guitarix

