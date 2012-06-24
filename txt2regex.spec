Summary:	Regular Expression Calculator
Summary(pl):	Kalkulator dla wyra�e� regularnych
Name:		txt2regex
Version:	0.7
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://txt2regex.sourceforge.net//%{name}-%{version}.tgz
URL:		http://txt2regex.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
^txt2regex$ is a Regular Expression "wizard", all written with bash2
builtins, that converts human sentences to RegExs. with a simple
interface, you just answer to questions and build your own RegEx for a
large variety of programs, like awk, ed, emacs, grep, perl, php,
procmail, python, sed and vim. there are more than 20 supported
programs. it's bash so download and run, no compilation needed.

%description -l pl
^txt2regex$ to czarodziej wyra�e� regularnych, napisany w bashu. Jego
zadaniem jest konwersja ludzkich zda� na wyra�enia regularne. W prosty
spos�b odpowiadasz na pytania i budujesz w�asne wyra�enia regularne
dla r�nych program�w, takich jak awk, ed, emacs, grep, perl, php,
procmail, python, sed i vim. Obs�ugiwanych jest wi�cej ni� 20
program�w. Poniewa� ^txt2regex$ jest napisany w bashu, nie trzeba go
kompilowa�, wystarczy uruchomi�.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install txt2regex-0.7.sh $RPM_BUILD_ROOT%{_bindir}/txt2regex
install txt2regex.man $RPM_BUILD_ROOT%{_mandir}/man1/txt2regex.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
