%define oname SystemTimer

Name:       rubygem-%{oname}
Version:    1.2
Release:    %mkrel 2
Summary:    Set a Timeout based on signals, which are more reliable than Timeout
Group:      Development/Ruby
License:    GPLv2+ or Ruby License
URL:        https://ph7spot.com/musings/system-timer
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildRequires: ruby-devel
Provides:   rubygem(%{oname}) = %{version}

%description
Set a Timeout based on signals, which are more reliable than Timeout. Timeout
is based on green threads.


%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
cp -rf .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

# install arch dependant files in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/system_timer_native.so %{buildroot}%{ruby_sitearchdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/ChangeLog
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/system_timer_native.so
