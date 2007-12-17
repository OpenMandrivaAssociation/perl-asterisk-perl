Summary:	Asterisk modules for perl
Name:		perl-asterisk-perl
Version:	0.10
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://asterisk.gnuinter.net/
Source0:	http://asterisk.gnuinter.net/files/asterisk-perl-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch

%description
perl-%{name} are modules for interfacing with the Asterisk open
source pbx system.

%prep

%setup -q -n asterisk-perl-%{version}

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


