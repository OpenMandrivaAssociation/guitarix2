%define ladspadir       %{_libdir}/ladspa
%define debug_package %{nil}

Name:           guitarix2
Summary:        Guitar effect processor for JACK
Version:        0.23.3
Release:        1

Source:         http://prdownloads.sourceforge.net/guitarix/%{name}-%{version}.tar.bz2
URL:            http://guitarix.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        GPLv2
Group:          Sound
BuildRequires:  sigc++2.0-devel fftw3-devel ladspa-devel
BuildRequires:  gtk+2.0-devel gtkmm2.4-devel
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


%changelog
* Tue Jul 31 2012 Frank Kober <emuse@mandriva.org> 0.23.3-1
+ Revision: 811492
- new version 0.23.3

* Thu Jul 12 2012 Frank Kober <emuse@mandriva.org> 0.23.2-1
+ Revision: 809068
- new version 0.23.2

* Thu Jul 05 2012 Frank Kober <emuse@mandriva.org> 0.23.1-1
+ Revision: 808161
- new version 0.23.1

* Fri May 18 2012 Frank Kober <emuse@mandriva.org> 0.22.3-1
+ Revision: 799574
- new version 0.22.3 (bugfixes)

* Tue Apr 17 2012 Frank Kober <emuse@mandriva.org> 0.22.0-3
+ Revision: 791535
- provide separate package for guitarix ladspa plugins

* Sun Apr 15 2012 Frank Kober <emuse@mandriva.org> 0.22.0-2
+ Revision: 791118
- rebuild using distro-own packages of zita-convolver and zita-resampler

* Sun Apr 15 2012 Frank Kober <emuse@mandriva.org> 0.22.0-1
+ Revision: 791085
- new version 0.22.0

* Wed Nov 09 2011 Frank Kober <emuse@mandriva.org> 0.20.1-1
+ Revision: 729562
- new version 0.20.1
  o try build with original waf configure forcing single CPU (works locally)

* Wed Nov 02 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.18.0-2
+ Revision: 712244
- buildfix or we always have Unable to open file  osc.lib ERROR
- added libzita-resampler-devel to req section

* Wed Aug 10 2011 Frank Kober <emuse@mandriva.org> 0.18.0-1
+ Revision: 693878
- new version 0.18.0

* Sat Jul 09 2011 Frank Kober <emuse@mandriva.org> 0.17.0-1
+ Revision: 689409
- new version 0.17.0 (mainly bugfixes, some new features)

* Fri Jun 10 2011 Frank Kober <emuse@mandriva.org> 0.16.0-1
+ Revision: 684098
- added intltool BR
- Conflicts old version in guitarix package
- import guitarix2

