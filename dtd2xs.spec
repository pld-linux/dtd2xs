Summary:	Convert DTD to XML Schema
Summary(pl):	Konwertuje DTD do formatu XML Schema
Name:		dtd2xs
Version:	1.4
Release:	1
License:	Free for non-commercial use
Group:		Applications/Text
# Download from http://www.syntext.com/products/index.htm
Source0:	http://downloads.syntext.com/%{name}-%{version}.tar.gz
# NoSource0-md5:	ce37fcc46b440699a8473d64340f6a8d
NoSource:	0
URL:		http://www.syntext.com/products/index.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dtd2Xs allows you to convert complex, modularized XML DTDs and DTDs
with namespaces to XML Schemas. As an example of Dtd2Xs conversion
check out DocBook XML Schema generated from XML DocBook DTD 4.2, and
XSL-FO Schema generated from XSL-FO DTD.

%description -l pl
Dtd2Xs pozwala na konwersjê z³o¿onych, modularyzowanych DTD plików XML
oraz DTD z przestrzeniami nazw do XML Schemas. Przyk³adem dzia³ania
Dtd3Xs jest DocBook XML Schema wygenerowany z XML DocBook DTD 4.2 oraz
XSL-FO Schema wygenerowany z XSL-FO DTD.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install bin/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
