Summary:	Regular Expression Calculator
Summary(pl):	Kalkulator dla wyra�e� regularnych
Summary(pt_BR):	Assistente "wizard" de Express�es Regulares
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

%description -l pl
^txt2regex$ to czarodziej wyra�e� regularnych, napisany w bashu. Jego
zadaniem jest konwersja ludzkich zda� na wyra�enia regularne. W prosty
spos�b odpowiadasz na pytania i budujesz w�asne wyra�enia regularne
dla r�nych program�w, takich jak AWK, ed, Emacs, grep, Perl, PHP,
procmail, Python, sed i vim. Obs�ugiwanych jest wi�cej ni� 20
program�w. Poniewa� ^txt2regex$ jest napisany w bashu, nie trzeba go
kompilowa�, wystarczy uruchomi�.

%description -l pt_BR
O ^txt2regex$ � um assistente "wizard" de Express�es Regulares todo escrito
com builtins do bash2, que converte frases humanas nas express�es. Com uma
apar�ncia simples, voc� apenas responde a perguntas e constr�i sua pr�pria
Express�o Regular para uma grande variedade de programas como: AWK, Emacs,
grep, Perl, PHP, procmail, Python, sed e vim. H� mais de 20 programas
cadastrados. � todo em bash, ent�o basta baixar e rodar, n�o precisa
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
