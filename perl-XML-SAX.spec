%include	/usr/lib/rpm/macros.perl

%define	pdir	XML
%define	pnam	SAX
%define _noautoreq	"perl(Encode)" "perl(XML::SAX::PurePerl::DocType)" "perl(XML::SAX::PurePerl::DTDDecls)" "perl(XML::SAX::PurePerl::EncodingDetect)" "perl(XML::SAX::PurePerl::NoUnicodeExt)" "perl(XML::SAX::PurePerl::Reader::NoUnicodeExt)" "perl(XML::SAX::PurePerl::Reader::UnicodeExt)" "perl(XML::SAX::PurePerl::UnicodeExt)" "perl(XML::SAX::PurePerl::XMLDecl)"

Summary:	XML-SAX perl module
Summary(pl):	Modu³ perla XML-SAX
Name:		perl-%{pdir}-%{pnam}
Version:	0.10
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-XML-NamespaceSupport >= 1.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX consists of several framework classes for using and building
Perl SAX2 XML parsers, filters, and drivers. It is designed around the
need to be able to "plug in" different SAX parsers to an application
without requiring programmer intervention. Those of you familiar with
the DBI will be right at home. Some of the designs come from the Java
JAXP specification (SAX part), only without the javaness.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo 'y' | perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/XML/SAX.pm
%{perl_sitelib}/XML/SAX
%{_mandir}/man3/*
