Name:		texlive-ptex-manual
Version:	71534
Release:	1
Summary:	Japanese pTeX manual
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ptex-manual
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-manual.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-manual.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains the Japanese pTeX manual. Feedback is
welcome!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/ptex/ptex-manual

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
