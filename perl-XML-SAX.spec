#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	SAX
Summary:	XML::SAX - simple API for XML
Summary(pl.UTF-8):	XML::SAX - proste API dla XML-a
Name:		perl-XML-SAX
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b62e3754523695c7f5bbcafa3676a38d
Patch0:		%{name}-noalter.patch
URL:		https://metacpan.org/release/XML-SAX
BuildRequires:	perl-XML-NamespaceSupport >= 0.03
BuildRequires:	perl-XML-SAX-Base >= 1.05
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires(post):	coreutils
Requires:	perl-XML-NamespaceSupport >= 0.03
Requires:	perl-XML-SAX-Base >= 1.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX consists of several framework classes for using and building
Perl SAX2 XML parsers, filters, and drivers. It is designed around the
need to be able to "plug in" different SAX parsers to an application
without requiring programmer intervention. Those of you familiar with
the DBI will be right at home. Some of the designs come from the Java
JAXP specification (SAX part), only without the javaness.

%description -l pl.UTF-8
XML::SAX składa się z kilku klas tworzących szkielet do używania i
budowania parserów, filtrów i sterowników SAX2 XML w Perlu. Zadaniem
modułu jest umożliwienie włączania różnych parserów SAX do aplikacji
bez udziału programisty. Znający moduły DBI będą się czuli jak w domu.
Niektóre koncepcje pochodzą ze specyfikacji Java JAXP (część SAX), ale
bez javowości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT%{perl_vendorlib}/XML/SAX/ParserDetails.ini

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/XML/SAX/Intro.pod

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
touch %{perl_vendorlib}/XML/SAX/ParserDetails.ini

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/SAX.pm
%{perl_vendorlib}/XML/SAX/DocumentLocator.pm
%{perl_vendorlib}/XML/SAX/ParserFactory.pm
%{perl_vendorlib}/XML/SAX/PurePerl.pm
%{perl_vendorlib}/XML/SAX/PurePerl
%ghost %{perl_vendorlib}/XML/SAX/ParserDetails.ini
%{_mandir}/man3/XML::SAX.3pm*
%{_mandir}/man3/XML::SAX::DocumentLocator.3pm*
%{_mandir}/man3/XML::SAX::Intro.3pm*
%{_mandir}/man3/XML::SAX::ParserFactory.3pm*
%{_mandir}/man3/XML::SAX::PurePerl*.3pm*
