%define modname	Test-MinimumVersion
%define modver	0.101080

Summary:	Does your code require newer perl than you think?
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(Perl::MinimumVersion)
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(YAML::Tiny)
BuildRequires:	perl-devel

%description
Does your code require newer perl than you think?

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

