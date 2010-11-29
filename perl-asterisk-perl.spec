%define upstream_name    asterisk-perl
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Asterisk modules for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/J/JA/JAMESGOL/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
perl-%{name} are modules for interfacing with the Asterisk open
source pbx system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES examples
%{perl_vendorlib}/*
%{_mandir}/man3/*


