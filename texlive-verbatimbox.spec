%global tl_name verbatimbox
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	Deposit verbatim text in a box
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/verbatimbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a verbbox environment (which uses techniques
similar to those of the boxedverbatim environment of the moreverb
package) to place its contents into a globally available box, or into a
box specified by the user. The global box may then be used in a variety
of situations (for example, providing a replica of the boxedverbatim
environment itself). A valuable use is in places where the standard
verbatim environment (which is based on a trivlist) may not appear. The
package makes use of the verbatim package (which is a required part of
any LaTeX distribution).

