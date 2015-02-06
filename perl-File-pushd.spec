%define upstream_name    File-pushd
%define upstream_version 1.007

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Change directory temporarily for a limited scope

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
File::pushd does a temporary 'chdir' that is easily and automatically
reverted, similar to 'pushd' in some Unix command shells. It works by
creating an object that caches the original working directory. When the
object is destroyed, the destructor calls 'chdir' to revert to the original
working directory. By storing the object in a lexical variable with a
limited scope, this happens automatically at the end of the scope.

This is very handy when working with temporary directories for tasks like
testing; a function is provided to streamline getting a temporary directory
from the File::Temp manpage.

For convenience, the object stringifies as the canonical form of the
absolute pathname of the directory entered.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*
