Name:           budgie-backgrounds
Version:        3.0
Release:        1
Summary:        The default background set for the Budgie Desktop
License:        CC0-1.0
Group:          System/Backgrounds
URL:            https://github.com/BuddiesOfBudgie/budgie-backgrounds
Source0:        https://github.com/BuddiesOfBudgie/budgie-backgrounds/releases/download/v%{version}/budgie-backgrounds-v%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  imagemagick
BuildRequires:  jhead
  
BuildArch:      noarch

%description
Budgie Backgrounds is the default set of background images for the Budgie Desktop.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/budgie
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/budgie-backgrounds.xml
