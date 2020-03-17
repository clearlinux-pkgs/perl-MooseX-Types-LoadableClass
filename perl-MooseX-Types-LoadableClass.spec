#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Types-LoadableClass
Version  : 0.015
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-0.015.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-0.015.tar.gz
Summary  : 'ClassName type constraint with coercion to load the class.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MooseX-Types-LoadableClass-license = %{version}-%{release}
Requires: perl-MooseX-Types-LoadableClass-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Carp::Clan)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Devel::OverloadInfo)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moose)
BuildRequires : perl(Moose::Role)
BuildRequires : perl(MooseX::Types)
BuildRequires : perl(MooseX::Types::Moose)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Exporter::ForMethods)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution MooseX-Types-LoadableClass,
version 0.015:

%package dev
Summary: dev components for the perl-MooseX-Types-LoadableClass package.
Group: Development
Provides: perl-MooseX-Types-LoadableClass-devel = %{version}-%{release}
Requires: perl-MooseX-Types-LoadableClass = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Types-LoadableClass package.


%package license
Summary: license components for the perl-MooseX-Types-LoadableClass package.
Group: Default

%description license
license components for the perl-MooseX-Types-LoadableClass package.


%package perl
Summary: perl components for the perl-MooseX-Types-LoadableClass package.
Group: Default
Requires: perl-MooseX-Types-LoadableClass = %{version}-%{release}

%description perl
perl components for the perl-MooseX-Types-LoadableClass package.


%prep
%setup -q -n MooseX-Types-LoadableClass-0.015
cd %{_builddir}/MooseX-Types-LoadableClass-0.015

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooseX-Types-LoadableClass
cp %{_builddir}/MooseX-Types-LoadableClass-0.015/LICENCE %{buildroot}/usr/share/package-licenses/perl-MooseX-Types-LoadableClass/c8c0ad8e3cb7dee58a02780133fc8f79b45edaba
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Types::LoadableClass.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooseX-Types-LoadableClass/c8c0ad8e3cb7dee58a02780133fc8f79b45edaba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/MooseX/Types/LoadableClass.pm
