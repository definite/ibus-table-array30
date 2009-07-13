Name:       ibus-table-array30
Version:    1.2.0.20090713
Release:    1%{?dist}
Summary:     Array30 Chinese input method
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://github.com/definite/ibus-table-array30/tree/master
Source0:    %{name}-%{version}-Source.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  ibus-table >= 1.1
BuildRequires:  cmake >= 2.4
Requires:  ibus-table >= 1.1
Requires(post):  ibus-table >= 1.1

%description
The Chewing engine for IBus platform. It provides Chinese input method from
libchewing.

%prep
%setup -q -n %{name}-%{version}-Source

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_usr}
make VERBOSE=1 C_DEFINES="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/Array30.db

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README ChangeLog COPYING INSTALL
%{_datadir}/ibus-table/tables/Array30.db
%{_datadir}/ibus-table/icons/Array30.png

%changelog
* Mon Jul 13 2009 Ding-Yi Chen <dchen at redhat.com> - 1.2.0.20090713-1






