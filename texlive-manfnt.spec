# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/manfnt
# catalog-date 2007-01-02 14:43:33 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-manfnt
Version:	20070102
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A LaTeX package for easy access to the symbols of the Knuth's
'manual' font, such as the Dangerous Bend and Manual-errata
Arrow.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
