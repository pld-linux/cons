Summary:	Cons - A software Construction System
Summary(pl):	Cons - system do konstruowania oprogramowania
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

%description -l pl
Cons to oparty na Perlu zastêpca make. Nie jest kompatybilny z make
ale ma wiele potê¿nych mo¿liwo¶ci, których nie ma ¿aden inny system do
konstruowania oprogramowania, w³±cznie z make.

Czy u¿ywasz plików Makefile w swoim projekcie? Robi³e¶ kiedy¶ "make
clean; make all", bo nie by³e¶ pewien, czy zmienione pliki zostan±
przebudowane poprawnie? A mo¿e pracujesz na kilku maszynach z u¿yciem
serwera NFS, i je¶li ich zegary nie s± zsynchronizowane, make nie wie,
co trzeba przebudowaæ? Tak, witamy na nowej i lepszej drodze do
sterowania budowaniem projektów.

%package test
Summary:	Cons-Test - Cons software construction utility regression test package
Summary(pl):	Cons-Test - pakiet z testami regresji dla narzêdzia Cons
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description test
The regression test package for the Cons software construction tool,
containing the tests, a wrapper script for executing them, and
supporting modules.

Cons is a Perl-based make replacement. It is not compatible with make,
but has a number of powerful capabilities not found in other software
construction systems, including make.

%description test -l pl
Pakiet z testami regresji dla narzêdzia do konstruowania
oprogramowania Cons. Pakiet zawiera testy, skrypt obudowuj±cy do ich
wykonywania i wspieraj±ce modu³y.

Cons to oparty na Perlu zastêpca make. Nie jest kompatybilny z make
ale ma wiele potê¿nych mo¿liwo¶ci, których nie ma ¿aden inny system do
konstruowania oprogramowania, w³±cznie z make.

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
