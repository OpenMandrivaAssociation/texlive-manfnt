# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/manfnt
# catalog-date 2007-01-02 14:43:33 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-manfnt
Version:	20070102
Release:	6
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
%{_texmfdistdir}/fonts/afm/hoekwater/manfnt/manfnt.afm
%{_texmfdistdir}/fonts/map/dvips/manfnt/manfnt.map
%{_texmfdistdir}/fonts/type1/hoekwater/manfnt/manfnt.pfb
%{_texmfdistdir}/tex/latex/manfnt/manfnt.sty
#- source
%doc %{_texmfdistdir}/source/latex/manfnt/manfnt.dtx
%doc %{_texmfdistdir}/source/latex/manfnt/manfnt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070102-2
+ Revision: 753735
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070102-1
+ Revision: 718952
- texlive-manfnt
- texlive-manfnt
- texlive-manfnt
- texlive-manfnt

