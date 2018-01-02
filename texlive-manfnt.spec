Name:		texlive-manfnt
Version:	20170414
Release:	1
Summary:	LaTeX support for the TeX book symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/manfnt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manfnt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manfnt.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for easy access to the symbols of the Knuth's
'manual' font, such as the Dangerous Bend and Manual-errata
Arrow.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/manfnt
#- source
%doc %{_texmfdistdir}/source/latex/manfnt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
