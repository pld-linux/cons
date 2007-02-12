Summary:	Cons - A software Construction System
Summary(pl.UTF-8):   Cons - system do konstruowania oprogramowania
Name:		cons
Version:	2.2.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.gnu.org/software/cons/stable/%{name}-%{version}.tgz
# Source0-md5:	4e42d6aa29bc8c3da76e3ad6b9030414
Source1:	http://www.gnu.org/software/cons/stable/%{name}-test-%{version}.tgz
# Source1-md5:	c09f2cfe93b5f78337d159309e917e73
URL:		http://www.gnu.org/software/cons/
Requires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cons is a Perl-based make replacement. It is not compatible with make,
but has a number of powerful capabilities not found in other software
construction systems, including make.

Do you use Makefiles for your project? Have you ever done a "make
clean; make all" just because you didn't know if the files you changed
would be rebuilt correctly? Or perhaps you work on several machines
accessing an NFS server, and if their clocks aren't in sync, make
won't know to rebuild things? Well, welcome to a new and better way to
control the building of your projects.

%description -l pl.UTF-8
Cons to oparty na Perlu zastępca make. Nie jest kompatybilny z make
ale ma wiele potężnych możliwości, których nie ma żaden inny system do
konstruowania oprogramowania, włącznie z make.

Czy używasz plików Makefile w swoim projekcie? Robiłeś kiedyś "make
clean; make all", bo nie byłeś pewien, czy zmienione pliki zostaną
przebudowane poprawnie? A może pracujesz na kilku maszynach z użyciem
serwera NFS, i jeśli ich zegary nie są zsynchronizowane, make nie wie,
co trzeba przebudować? Tak, witamy na nowej i lepszej drodze do
sterowania budowaniem projektów.

%package test
Summary:	Cons-Test - Cons software construction utility regression test package
Summary(pl.UTF-8):   Cons-Test - pakiet z testami regresji dla narzędzia Cons
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description test
The regression test package for the Cons software construction tool,
containing the tests, a wrapper script for executing them, and
supporting modules.

Cons is a Perl-based make replacement. It is not compatible with make,
but has a number of powerful capabilities not found in other software
construction systems, including make.

%description test -l pl.UTF-8
Pakiet z testami regresji dla narzędzia do konstruowania
oprogramowania Cons. Pakiet zawiera testy, skrypt obudowujący do ich
wykonywania i wspierające moduły.

Cons to oparty na Perlu zastępca make. Nie jest kompatybilny z make
ale ma wiele potężnych możliwości, których nie ma żaden inny system do
konstruowania oprogramowania, włącznie z make.

%prep
%setup -q
%setup -q -D -T -b 1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/cons}

install cons test/cons-test $RPM_BUILD_ROOT%{_bindir}
install cons.1.gz test/cons-test.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
cp -p -r test/t $RPM_BUILD_ROOT%{_datadir}/cons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README RELEASE TODO cons.html
%attr(755,root,root) %{_bindir}/cons
%{_mandir}/man1/cons.1*

%files test
%defattr(644,root,root,755)
%doc test/CHANGES test/README test/TODO test/Tests.txt
%attr(755,root,root) %{_bindir}/cons-test
%{_datadir}/cons
%{_mandir}/man1/cons-test.1*
