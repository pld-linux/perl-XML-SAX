%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	SAX
Summary:	XML::SAX - Simple API for XML
Summary(pl):	XML::SAX - Proste API dla XML
Name:		perl-XML-SAX
Version:	0.11
Release:	4
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-noalter.patch
BuildRequires:	perl-XML-NamespaceSupport >= 0.03
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-56
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{perl_sitelib}/XML/SAX/ParserDetails.ini

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/XML/SAX.pm
%dir %{perl_sitelib}/XML/SAX
%{perl_sitelib}/XML/SAX/*.pm
%ghost %{perl_sitelib}/XML/SAX/ParserDetails.ini
%{_mandir}/man3/*
