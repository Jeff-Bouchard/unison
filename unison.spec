Name:		unison
Version:	2.48.3
Release:	1%{?dist}
Summary:	Unison File Synchronizer
Group:		Applications/Internet
Vendor:		Benjamin Pierce
License:	GPLv3
URL:		http://www.cis.upenn.edu/~bcpierce/unison
Source0:	%{name}.tar.gz
BuildArch:	x86_64
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	ocaml ctags-etags
Requires:	ocaml ctags-etags

%description
Unison File Synchronizer

%prep
%setup -q -n %{name}

%build
cd src
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_sbindir}
%{__cp} src/unison $RPM_BUILD_ROOT%{_sbindir}
%{__cp} src/unison-fsmonitor $RPM_BUILD_ROOT%{_sbindir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc LICENSE
%defattr(-,root,root,-)
%{_sbindir}/unison
%{_sbindir}/unison-fsmonitor

%changelog
* Mon Oct 5 2015 Benjamin Pierce <bcpierce00@gmail.com> 2.48.3
- Stable release
