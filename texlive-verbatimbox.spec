# revision 31022
# category Package
# catalog-ctan /macros/latex/contrib/verbatimbox
# catalog-date 2013-06-19 11:29:28 +0200
# catalog-license lppl
# catalog-version 3.1
Name:		texlive-verbatimbox
Version:	3.1
Release:	3
Summary:	Deposit verbatim text in a box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbatimbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a verbbox environment (which uses
techniques similar to those of the boxedverbatim environment of
the moreverb package) to place its contents into a globally
available box, or into a box specified by the user. The global
box may then be used in a variety of situations (for example,
providing a replica of the boxedverbatim environment itself). A
valuable use is in places where the standard verbatim
environment (which is based on a trivlist) may not appear. The
package makes use of the verbatim package (which is a required
part of any LaTeX distribution).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbatimbox/verbatimbox.sty
%doc %{_texmfdistdir}/doc/latex/verbatimbox/README
%doc %{_texmfdistdir}/doc/latex/verbatimbox/verbatimbox.pdf
%doc %{_texmfdistdir}/doc/latex/verbatimbox/verbatimbox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
