#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	SAX
Summary:	XML::SAX - Simple API for XML
Summary(pl):	XML::SAX - Proste API dla XML
Name:		perl-XML-SAX
Version:	0.12
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bff58bd077a9693fc8cf32e2b95f571f
Patch0:		%{name}-noalter.patch
BuildRequires:	perl-XML-NamespaceSupport >= 0.03
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(XML::SAX::PurePerl::Productions)
Provides:	perl(XML::SAX::PurePerl::Reader)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _noautoreq	"perl(Encode)" "perl(XML::SAX::PurePerl::DocType)" "perl(XML::SAX::PurePerl::DTDDecls)" "perl(XML::SAX::PurePerl::EncodingDetect)" "perl(XML::SAX::PurePerl::NoUnicodeExt)" "perl(XML::SAX::PurePerl::Reader::NoUnicodeExt)" "perl(XML::SAX::PurePerl::Reader::UnicodeExt)" "perl(XML::SAX::PurePerl::UnicodeExt)" "perl(XML::SAX::PurePerl::XMLDecl)"

%description
XML::SAX consists of several framework classes for using and building
Perl SAX2 XML parsers, filters, and drivers. It is designed around the
need to be able to "plug in" different SAX parsers to an application
without requiring programmer intervention. Those of you familiar with
the DBI will be right at home. Some of the designs come from the Java
JAXP specification (SAX part), only without the javaness.

%description -l pl
XML::SAX sk³ada siê z kilku klas tworz±cych szkielet do u¿ywania i
budowania parserów, filtrów i sterowników SAX2 XML w Perlu. Zadaniem
modu³u jest umo¿liwienie w³±czania ró¿nych parserów SAX do aplikacji
bez udzia³u programisty. Znaj±cy modu³y DBI bêd± siê czuli jak w domu.
Niektóre koncepcje pochodz± ze specyfikacji Java JAXP (czê¶æ SAX), ale
bez javowo¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{perl_vendorlib}/XML/SAX/ParserDetails.ini

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
touch %{perl_vendorlib}/XML/SAX/ParserDetails.ini

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/SAX.pm
%dir %{perl_vendorlib}/XML/SAX
%{perl_vendorlib}/XML/SAX/*.pm
%{perl_vendorlib}/XML/SAX/PurePerl
%ghost %{perl_vendorlib}/XML/SAX/ParserDetails.ini
%{_mandir}/man3/*
