%define upstream_name    Test-MinimumVersion
%define upstream_version 0.101080

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Does your code require newer perl than you think?
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(Perl::MinimumVersion)
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(YAML::Tiny)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Does your code require newer perl than you think?

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.101.80-5mdv2012.0
+ Revision: 765703
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.101.80-3
+ Revision: 676640
- rebuild

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.101.80-2
+ Revision: 654312
- rebuild for updated spec-helper

* Mon Apr 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.80-1mdv2011.0
+ Revision: 536730
- update to 0.101080

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.50-1mdv2010.1
+ Revision: 536214
- update to 0.101050

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.13.0-1mdv2010.1
+ Revision: 493016
- fix typo in buildrequires:
- adding missing buildrequires:
- update to 0.013

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11.0-1mdv2010.0
+ Revision: 391190
- update to new version 0.011

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 381800
- update to 0.010
- using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.009-2mdv2010.0
+ Revision: 375897
- rebuild

* Fri May 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.009-1mdv2010.0
+ Revision: 373468
- import perl-Test-MinimumVersion


* Fri May 08 2009 cpan2dist 0.009-1mdv
- initial mdv release, generated with cpan2dist

