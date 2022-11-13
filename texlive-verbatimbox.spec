Name:		texlive-verbatimbox
Version:	33197
Release:	1
Summary:	Deposit verbatim text in a box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbatimbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
