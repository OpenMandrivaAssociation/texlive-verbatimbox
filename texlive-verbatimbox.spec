# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/verbatimbox
# catalog-date 2009-10-11 01:33:30 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-verbatimbox
Version:	1.0
Release:	1
Summary:	Deposit verbatim text in a box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbatimbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a verbbox environment (which uses
techniques similar to those of the boxedverbatim of the
moreverb package) to place its contents into a globally
available box. The global box may then be used in a variety of
situations (for example, providing a replica of the
boxedverbatim environment itself). A valuable use is in places
where the standard verbatim environment (which is based on a
trivlist) may not appear. The package makes use of the verbatim
package (which is a required part of any LaTeX distribution).

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
%{_texmfdistdir}/tex/latex/verbatimbox/verbatimbox.sty
%doc %{_texmfdistdir}/doc/latex/verbatimbox/README
%doc %{_texmfdistdir}/doc/latex/verbatimbox/verbatimbox_example.pdf
%doc %{_texmfdistdir}/doc/latex/verbatimbox/verbatimbox_example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
