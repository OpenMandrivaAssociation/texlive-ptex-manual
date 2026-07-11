%global tl_name ptex-manual
%global tl_revision 75173

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Japanese pTeX manual
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/ptex-manual
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-manual.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-manual.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains the Japanese pTeX manual. Feedback is welcome!

