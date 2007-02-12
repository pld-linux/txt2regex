Summary:	Regular Expression Calculator
Summary(pl.UTF-8):	Kalkulator dla wyrażeń regularnych
Summary(pt_BR.UTF-8):	Assistente "wizard" de Expressões Regulares
Name:		txt2regex
Version:	0.8
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://txt2regex.sourceforge.net/%{name}-%{version}.tgz
# Source0-md5:	83bc1f95b36fe51ade8d130fab390103
URL:		http://txt2regex.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
^txt2regex$ is a Regular Expression "wizard", all written with bash2
builtins, that converts human sentences to RegExs. with a simple
interface, you just answer to questions and build your own RegEx for a
large variety of programs, like AWK, ed, Emacs, grep, Perl, PHP,
procmail, Python, sed and vim. there are more than 20 supported
programs. it's bash so download and run, no compilation needed.

%description -l pl.UTF-8
^txt2regex$ to czarodziej wyrażeń regularnych, napisany w bashu. Jego
zadaniem jest konwersja ludzkich zdań na wyrażenia regularne. W prosty
sposób odpowiadasz na pytania i budujesz własne wyrażenia regularne
dla różnych programów, takich jak AWK, ed, Emacs, grep, Perl, PHP,
procmail, Python, sed i vim. Obsługiwanych jest więcej niż 20
programów. Ponieważ ^txt2regex$ jest napisany w bashu, nie trzeba go
kompilować, wystarczy uruchomić.

%description -l pt_BR.UTF-8
O ^txt2regex$ é um assistente "wizard" de Expressões Regulares todo escrito
com builtins do bash2, que converte frases humanas nas expressões. Com uma
aparência simples, você apenas responde a perguntas e constrói sua própria
Expressão Regular para uma grande variedade de programas como: AWK, Emacs,
grep, Perl, PHP, procmail, Python, sed e vim. Há mais de 20 programas
cadastrados. É todo em bash, então basta baixar e rodar, não precisa
compilar.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install txt2regex-%{version}.sh $RPM_BUILD_ROOT%{_bindir}/txt2regex
install txt2regex.man $RPM_BUILD_ROOT%{_mandir}/man1/txt2regex.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog NEWS README TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
