%define upstream_name    asterisk-perl
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Asterisk modules for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JAMESGOL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
perl-%{name} are modules for interfacing with the Asterisk open
source pbx system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

%files
%doc README CHANGES examples
%{perl_vendorlib}/*
%{_mandir}/man3/*




%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 657862
- rebuild for updated spec-helper

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 603052
- normalize version

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2011.0
+ Revision: 389773
- update to new version 1.01

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 241150
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
+ Revision: 63919
- update to new version 0.10

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.09-1mdv2008.0
+ Revision: 19247
-New version


* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-3mdv2007.0
+ Revision: 99240
- Import perl-asterisk-perl

* Wed Feb 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.08-3mdk
- rebuild

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.08-2mdk
- rebuild

* Sun Dec 26 2004 Oden Eriksson <oden.eriksson@linux-mandrake.com> 0.08-1mdk
- initial mandrake package

