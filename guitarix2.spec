%define ladspadir       %{_libdir}/ladspa

Name:           guitarix2
Summary:        Guitar effect processor for JACK
Version:        0.23.2
Release:        1

Source:         http://prdownloads.sourceforge.net/guitarix/%{name}-%{version}.tar.bz2
URL:            http://guitarix.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        GPLv2
Group:          Sound
BuildRequires:  sigc++2.0-devel fftw3-devel ladspa-devel
BuildRequires:  gtk+2-devel gtkmm2.4-devel
BuildRequires:  sndfile-devel jackit-devel
BuildRequires:  libzita-convolver-devel libzita-resampler-devel boost-devel
BuildRequires:  liblrdf-devel
BuildRequires:  faust
BuildRequires:  intltool gettext-devel desktop-file-utils
Requires:       %{name}-plugins-ladspa = %{version}
Provides:       guitarix = %{version}-%{release}
Obsoletes:      guitarix < %{version}-%{release}

%description
Guitarix is a simple Linux Rock Guitar Amplifier for the Jack Audio
Connektion Kit with one input and two outputs. Designed to get nice
thrash/metal/rock/blues guitar sounds. There are controls for bass,
middle, treble, gain (in/out), compressor, preamp, tube's, drive,
overdrive, oversample, anti-alias, fuzz, balance, distortion, freeverb,
impulse response, vibrato, chorus, delay , cry-baby(wah) and echo.

%package plugins-ladspa
Summary:        LADSPA plugins coming with guitarix2
Group:          Sound

Requires:       ladspa

%description plugins-ladspa
Guitarix is a simple Linux Rock Guitar Amplifier for the Jack Audio
Connektion Kit. This package includes the LADSPA plugins for the amp,
which can be used with other LADSPA hosts as well.

%prep
%setup -q -n guitarix-%{version}

%build

./waf -vv configure --prefix=%{_prefix} --ladspadir=%ladspadir -j1
#      --cxxflags="-std=c++0x -fomit-frame-pointer -ftree-loop-linear         \
#      -ffinite-math-only -fno-math-errno -fno-signed-zeros -fstrength-reduce \
#      %{optflags}"                                                           \


./waf build -j1

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="X-Jack;" \
                     --remove-category="Midi;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/guitarix
%{_datadir}/pixmaps/*.png
%{_datadir}/gx_head/skins/*.jpg
%{_datadir}/gx_head/skins/*.png
%{_datadir}/gx_head/skins/*.svg
%{_datadir}/gx_head/skins/*.rc
%{_datadir}/gx_head/sounds/*.wav
%{_datadir}/gx_head/builder/*
%{_datadir}/gx_head/factorysettings/*
%{_datadir}/applications/guitarix.desktop
%{_localedir}/es/LC_MESSAGES/guitarix.mo
%{_localedir}/fr/LC_MESSAGES/guitarix.mo
%{_localedir}/it/LC_MESSAGES/guitarix.mo

%files plugins-ladspa
%defattr(-,root,root)
%ladspadir/*.so
%{_datadir}/ladspa/rdf/*.rdf
