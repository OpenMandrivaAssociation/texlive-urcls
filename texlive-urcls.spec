Name:		texlive-urcls
Version:	49903
Release:	2
Summary:	Beamer and scrlttr2 classes and styles for the University of Regensburg
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/urcls
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urcls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urcls.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a beamer-derived class and a theme style
file for the corporate design of the University of Regensburg.
It also contains a scrlttr2-derived class for letters using the
corporate design of the UR. Users may use the class itself
(URbeamer) or use the theme in the usual way with
\usetheme{UR}. Examples of using both letters and presentations
are provided as .tex and .pdf-files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/urcls
%doc %{_texmfdistdir}/doc/latex/urcls

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
