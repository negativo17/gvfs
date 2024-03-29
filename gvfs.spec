%define with_nfs 0

%global avahi_version 0.6
%global fuse_version 2.8.0
%global gettext_version 0.19.4
%global glib2_version 2.51.0
%global goa_version 3.17.1
%global gudev_version 147
%global libarchive_version 3.0.22
%global libcdio_paranoia_version 0.78.2
%global libgcrypt_version 1.2.2
%global libgdata_version 0.17.9
%global libgphoto2_version 2.5.0
%global libimobiledevice_version 1.2
%global libmtp_version 1.1.12
%global libnfs_version 1.9.8
%global libplist_version 0.15
%global libsmbclient_version 3.4.0
%global libsoup_version 2.42.0
%global libusb_version 1.0.21
%global systemd_version 206
%global talloc_version 1.3.0
%global udisks2_version 1.97

Name: gvfs
Version: 1.36.2
Release: 8%{?dist}
Summary: Backends for the gio framework in GLib

License: GPLv3 and LGPLv2+ and BSD and MPLv2.0
URL: https://wiki.gnome.org/Projects/gvfs
Source0: https://download.gnome.org/sources/gvfs/1.36/gvfs-%{version}.tar.xz

# http://bugzilla.gnome.org/show_bug.cgi?id=567235
Patch0: gvfs-archive-integration.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1632960
Patch1: daemon-Prevent-spawning-new-daemons-if-outgoing-oper.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1673887
Patch2: admin-Prevent-access-if-any-authentication-agent-isn.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1619719
Patch3: smbbrowse-Force-NT1-protocol-version-for-workgroup-s.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1758237
Patch4: udisks2-Fix-crashes-caused-by-missing-source-tag.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1944813
Patch5: udisks2-Fix-leak-when-updating-fstab-volumes.patch
Patch6: udisks2-Fix-leaks-of-drive-icons-description.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2093816
Patch7: smb-Use-O_RDWR-to-fix-fstat-when-writing.patch

BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: /usr/bin/ssh
BuildRequires: pkgconfig(libcdio_paranoia) >= %{libcdio_paranoia_version}
BuildRequires: pkgconfig(gudev-1.0) >= %{gudev_version}
BuildRequires: pkgconfig(libsoup-2.4) >= %{libsoup_version}
BuildRequires: pkgconfig(avahi-client) >= %{avahi_version}
BuildRequires: pkgconfig(avahi-glib) >= %{avahi_version}
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: gettext-devel >= %{gettext_version}
BuildRequires: pkgconfig(udisks2) >= %{udisks2_version}
BuildRequires: pkgconfig(libbluray)
BuildRequires: systemd-devel >= %{systemd_version}
BuildRequires: pkgconfig(libxslt)
BuildRequires: docbook-style-xsl
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(libcap)

# The patch touches Makefile.am files:
BuildRequires: automake autoconf
BuildRequires: libtool

Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: udisks2 >= %{udisks2_version}

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Obsoletes: gnome-mount <= 0.8
Obsoletes: gnome-mount-nautilus-properties <= 0.8
Obsoletes: gvfs-obexftp < 1.17.91-2

%description
The gvfs package provides backend implementations for the gio
framework in GLib. It includes ftp, sftp, cifs.


%package  client
Summary:  Client modules of backends for the gio framework in GLib
Conflicts: %{name} < 1.25.2-2

%description client
The gvfs package provides client modules of backend implementations for the gio
framework in GLib.


%package devel
Summary: Development files for gvfs
Requires: %{name}-client%{?_isa} = %{version}-%{release}

%description devel
The gvfs-devel package contains headers and other files that are
required to develop applications using gvfs.


%package fuse
Summary: FUSE support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(fuse) >= %{fuse_version}
Requires: fuse >= %{fuse_version}

%description fuse
This package provides support for applications not using gio
to access the gvfs filesystems.


%package smb
Summary: Windows fileshare support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: libsmbclient-devel >= %{libsmbclient_version}
BuildRequires: pkgconfig(talloc) >= %{talloc_version}

%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using gvfs.


%package archive
Summary: Archiving support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libarchive) >= %{libarchive_version}

%description archive
This package provides support for accessing files inside Zip and Tar archives,
as well as ISO images, to applications using gvfs.


%package gphoto2
Summary: gphoto2 support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libgphoto2) >= %{libgphoto2_version}
BuildRequires: libusb-devel >= %{libusb_version}
BuildRequires: libexif-devel

%description gphoto2
This package provides support for reading and writing files on
PTP based cameras (Picture Transfer Protocol) and MTP based
media players (Media Transfer Protocol) to applications using gvfs.


%ifnarch s390 s390x
%package afc
Summary: AFC support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: usbmuxd
BuildRequires: pkgconfig(libimobiledevice-1.0) >= %{libimobiledevice_version}
BuildRequires: pkgconfig(libplist) >= %{libplist_version}

%description afc
This package provides support for reading files on mobile devices
including phones and music players to applications using gvfs.
%endif


%package afp
Summary: AFP support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: libgcrypt-devel >= %{libgcrypt_version}
# this should ensure having this new subpackage installed on upgrade from older versions
Obsoletes: %{name} < 1.9.4-1

%description afp
This package provides support for reading and writing files on
Mac OS X and original Mac OS network shares via Apple Filing Protocol
to applications using gvfs.


%package mtp
Summary: MTP support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libmtp) >= %{libmtp_version}

%description mtp
This package provides support for reading and writing files on
MTP based devices (Media Transfer Protocol) to applications using gvfs.


%if 0%{?with_nfs}
%package nfs
Summary: NFS support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libnfs) >= %{libnfs_version}

%description nfs
This package provides support for reading and writing files on
NFS network shares (Network File System) to applications using gvfs.
%endif


%package goa
Summary: GOA support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(goa-1.0) >= %{goa_version}
BuildRequires: pkgconfig(libgdata) >= %{libgdata_version}
Requires: libgdata%{?_isa} >= %{libgdata_version}

%description goa
This package provides seamless integration with gnome-online-accounts
file services.

%package  tests
Summary:  Tests for the gvfs package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The gvfs-tests package contains tests that can be used to verify
the functionality of the installed gvfs package.

%prep
%setup -q
%patch0 -p1 -b .archive-integration
%patch1 -p1 -b .daemon-Prevent-spawning-new-daemons-if-outgoing-oper
%patch2 -p1 -b .admin-Prevent-access-if-any-authentication-agent-isn
%patch3 -p1 -b .smbbrowse-Force-NT1-protocol-version-for-workgroup-s
%patch4 -p1 -b .udisks2-Fix-crashes-caused-by-missing-source-tag
%patch5 -p1 -b .udisks2-Fix-leak-when-updating-fstab-volumes
%patch6 -p1 -b .udisks2-Fix-leaks-of-drive-icons-description
%patch7 -p1 -b .smb-Use-O_RDWR-to-fix-fstat-when-writing

# Needed for gvfs-0.2.1-archive-integration.patch
autoreconf -fi

%build
%configure \
%if ! 0%{?with_nfs}
        --disable-nfs \
%endif
        --disable-gdu \
        --enable-udisks2 \
        --enable-keyring \
        --enable-installed-tests
make %{?_smp_mflags} V=1

%install
%make_install

rm $RPM_BUILD_ROOT%{_libdir}/gvfs/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

# trashlib is GPLv3, include the license
cp -p daemon/trashlib/COPYING COPYING.GPL3

%find_lang gvfs

%post
/sbin/ldconfig
# Reload .mount files:
killall -USR1 gvfsd >&/dev/null || :
update-desktop-database &> /dev/null || :
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%postun
/sbin/ldconfig
update-desktop-database &> /dev/null ||:
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


# Reload .mount files when single subpackage is installed:
%post smb
killall -USR1 gvfsd >&/dev/null || :
%post gphoto2
killall -USR1 gvfsd >&/dev/null || :
%post mtp
killall -USR1 gvfsd >&/dev/null || :
%post goa
killall -USR1 gvfsd >&/dev/null || :
%ifnarch s390 s390x
%post afc
killall -USR1 gvfsd >&/dev/null || :
%endif

%post archive
update-desktop-database >&/dev/null || :
killall -USR1 gvfsd >&/dev/null || :

%postun archive
update-desktop-database >&/dev/null || :

%if 0%{?with_nfs}
%post nfs
killall -USR1 gvfsd >&/dev/null || :
%endif

%post afp
killall -USR1 gvfsd >&/dev/null || :


%files
%dir %{_datadir}/gvfs
%dir %{_datadir}/gvfs/mounts
%{_datadir}/gvfs/mounts/admin.mount
%{_datadir}/gvfs/mounts/sftp.mount
%{_datadir}/gvfs/mounts/trash.mount
%{_datadir}/gvfs/mounts/cdda.mount
%{_datadir}/gvfs/mounts/computer.mount
%{_datadir}/gvfs/mounts/dav.mount
%{_datadir}/gvfs/mounts/dav+sd.mount
%{_datadir}/gvfs/mounts/http.mount
%{_datadir}/gvfs/mounts/localtest.mount
%{_datadir}/gvfs/mounts/burn.mount
%{_datadir}/gvfs/mounts/dns-sd.mount
%{_datadir}/gvfs/mounts/network.mount
%{_datadir}/gvfs/mounts/ftp.mount
%{_datadir}/gvfs/mounts/ftps.mount
%{_datadir}/gvfs/mounts/recent.mount
%{_datadir}/dbus-1/services/org.gtk.vfs.Daemon.service
%{_datadir}/dbus-1/services/org.gtk.vfs.Metadata.service
%{_datadir}/dbus-1/services/org.gtk.vfs.UDisks2VolumeMonitor.service
%dir %{_datadir}/gvfs/remote-volume-monitors
%{_datadir}/gvfs/remote-volume-monitors/udisks2.monitor
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/polkit-1/actions/org.gtk.vfs.file-operations.policy
%{_datadir}/polkit-1/rules.d/org.gtk.vfs.file-operations.rules
%{_libdir}/gvfs/libgvfsdaemon.so
%{_libexecdir}/gvfsd
%{_libexecdir}/gvfsd-admin
%{_libexecdir}/gvfsd-ftp
%{_libexecdir}/gvfsd-sftp
%{_libexecdir}/gvfsd-trash
%{_libexecdir}/gvfsd-cdda
%{_libexecdir}/gvfsd-computer
%{_libexecdir}/gvfsd-dav
%{_libexecdir}/gvfsd-http
%{_libexecdir}/gvfsd-localtest
%{_libexecdir}/gvfsd-burn
%{_libexecdir}/gvfsd-dnssd
%{_libexecdir}/gvfsd-network
%{_libexecdir}/gvfsd-metadata
%{_libexecdir}/gvfs-udisks2-volume-monitor
%{_libexecdir}/gvfsd-recent
%{_mandir}/man1/gvfsd.1*
%{_mandir}/man1/gvfsd-metadata.1*
%{_userunitdir}/gvfs-daemon.service
%{_userunitdir}/gvfs-metadata.service
%{_userunitdir}/gvfs-udisks2-volume-monitor.service

%files client -f gvfs.lang
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.GPL3
%doc AUTHORS NEWS README
%dir %{_libdir}/gvfs
%{_libdir}/gvfs/libgvfscommon.so
%{_libdir}/gio/modules/libgioremote-volume-monitor.so
%{_libdir}/gio/modules/libgvfsdbus.so
%{_mandir}/man7/gvfs.7*
%{_bindir}/gvfs-*
%{_mandir}/man1/gvfs-*

%files devel
%dir %{_includedir}/gvfs-client
%dir %{_includedir}/gvfs-client/gvfs
%{_includedir}/gvfs-client/gvfs/gvfsurimapper.h
%{_includedir}/gvfs-client/gvfs/gvfsuriutils.h


%files fuse
%{_libexecdir}/gvfsd-fuse
%{_mandir}/man1/gvfsd-fuse.1*
%{_tmpfilesdir}/gvfsd-fuse-tmpfiles.conf

%files smb
%{_libexecdir}/gvfsd-smb
%{_libexecdir}/gvfsd-smb-browse
%{_datadir}/gvfs/mounts/smb-browse.mount
%{_datadir}/gvfs/mounts/smb.mount


%files archive
%{_datadir}/applications/mount-archive.desktop
%{_libexecdir}/gvfsd-archive
%{_datadir}/gvfs/mounts/archive.mount


%files gphoto2
%{_libexecdir}/gvfsd-gphoto2
%{_datadir}/gvfs/mounts/gphoto2.mount
%{_libexecdir}/gvfs-gphoto2-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/gphoto2.monitor
%{_userunitdir}/gvfs-gphoto2-volume-monitor.service

%ifnarch s390 s390x
%files afc
%{_libexecdir}/gvfsd-afc
%{_datadir}/gvfs/mounts/afc.mount
%{_libexecdir}/gvfs-afc-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.AfcVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/afc.monitor
%{_userunitdir}/gvfs-afc-volume-monitor.service
%endif

%files afp
%{_libexecdir}/gvfsd-afp
%{_libexecdir}/gvfsd-afp-browse
%{_datadir}/gvfs/mounts/afp.mount
%{_datadir}/gvfs/mounts/afp-browse.mount

%files mtp
%{_libexecdir}/gvfsd-mtp
%{_datadir}/gvfs/mounts/mtp.mount
%{_libexecdir}/gvfs-mtp-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/mtp.monitor
%{_userunitdir}/gvfs-mtp-volume-monitor.service

%if 0%{?with_nfs}
%files nfs
%{_libexecdir}/gvfsd-nfs
# for privileged ports
%caps(cap_net_bind_service=ep) %{_libexecdir}/gvfsd-nfs
%{_datadir}/gvfs/mounts/nfs.mount
%endif

%files goa
%{_libexecdir}/gvfs-goa-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.GoaVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/goa.monitor
%{_datadir}/gvfs/mounts/google.mount
%{_libexecdir}/gvfsd-google
%{_userunitdir}/gvfs-goa-volume-monitor.service

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/gvfs
%{_datadir}/installed-tests

%changelog
* Thu Aug 18 2022 Simone Caronni <negativo17@gmail.com> - 1.36.2-8
- Rebuild for libbluray update.

* Thu Jun 23 2022 Ondrej Holy <oholy@redhat.com> - 1.36.2-7
- Fix unapplied patch (#2093816)

* Tue Jun 14 2022 Ondrej Holy <oholy@redhat.com> - 1.36.2-6
- Use O_RDWR to fix fstat when writing on SMB share (#2093816)

* Fri Jul 2 2021 Ondrej Holy <oholy@redhat.com> - 1.36.2-5
- Fix udisks2 volume monitor leaks (rhbz#1944813)

* Wed Apr 22 2020 Ondrej Holy <oholy@redhat.com> - 1.36.2-4
- Fix udisks2 volume monitor crashes when stopping drive (rhbz#1758237)

* Fri Feb 15 2019 Ondrej Holy <oholy@redhat.com> - 1.36.2-3
- Force NT1 protocol version for workgroup support (#1619719)

* Thu Jan 31 2019 Ondrej Holy <oholy@redhat.com> - 1.36.2-2
- Prevent spawning new daemons if outgoing operation exists (#1632960)
- CVE-2019-3827: Prevent access if any authentication agent isn't available (#1673887)

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 1.36.2-1
- Update to 1.36.2
- Resolves: #1569268

* Fri Nov 10 2017 Ondrej Holy <oholy@redhat.com> - 1.30.4-5
- Fix network backend crashes when creating proxy failed (#1465302)

* Wed Oct 11 2017 Ondrej Holy <oholy@redhat.com> - 1.30.4-4
- Rebuild against newer libgphoto2 (#1500216)

* Tue Apr 18 2017 Ondrej Holy <oholy@redhat.com> - 1.30.4-3
- Handle SecurID password prompt
- Resolves: #1440256

* Tue Mar 28 2017 Ondrej Holy <oholy@redhat.com> - 1.30.4-2
- Add explicit gvfs-client requirements
- Resolves: #1386993

* Tue Mar 28 2017 Ondrej Holy <oholy@redhat.com> - 1.30.4-1
- Update to 1.30.4
- Resolves: #1386993

* Thu Feb 16 2017 Ondrej Holy <oholy@redhat.com> - 1.30.3-1
- Update to 1.30.3
- Disable nfs support (#1387270)
- Revert desktop database scriplets
- Resolves: #1386993, #1399343, #1306146, #1259746, #1344317

* Mon Jun 27 2016 Ondrej Holy <oholy@redhat.com> - 1.22.4-8
- Update translations
- Resolves: #1304254

* Tue Apr  5 2016 Matthias Clasen <mclasen@redhat.com> - 1.22.4-7
- Update translations
- Resolves: #1304254

* Fri Oct 16 2015 Debarshi Ray <rishi@fedoraproject.org> - 1.22.4-6
- Properly handle failure to create a remote proxy
- Resolves: #1221695

* Wed Sep 30 2015 Debarshi Ray <rishi@fedoraproject.org> - 1.22.4-5
- Guard access to the internal caches of the proxy volume monitor
- Resolves: #1221695

* Tue Aug 4 2015 Ondrej Holy <oholy@redhat.com> - 1.22.4-4
- Handle libsecret errors
- Resolves: #1230974

* Fri Jun 12 2015 Ondrej Holy <oholy@redhat.com> - 1.22.4-3
- Fix gvfs-open issues
- Resolves: #1229178

* Fri May 15 2015 Ondrej Holy <oholy@redhat.com> - 1.22.4-2
- Add translation updates from translation team
- Resolves: #1174716

* Tue May 5 2015 Ondrej Holy <oholy@redhat.com> - 1.22.4-1
- Update to 1.22.4
- Remove obsolete upstream patches
- Add translations updates from upstream
- Resolves: #1174716

* Thu Apr 23 2015 Ondrej Holy <oholy@redhat.com> - 1.16.4-9
- Add missing man page (#948924)

* Tue Jan 6 2015 Ondrej Holy <oholy@redhat.com> - 1.16.4-8
- Avoid endless looping when the metatree entry is too large (#1163743)

* Mon Feb 24 2014 Matthias Clasen <mclasen@redhat.com> - 1.16.4-7
- Rebuild against newer libcdio
Resolves: #1069206

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.16.4-6
- Mass rebuild 2014-01-24

* Thu Jan 9 2014 Ondrej Holy <oholy@redhat.com> - 1.16.4-5
- Fix mtp crashes (#1042899)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.16.4-4
- Mass rebuild 2013-12-27

* Thu Dec 12 2013 Ondrej Holy <oholy@redhat.com> - 1.16.4-3
- Translation updates (#1030357)

* Fri Dec 6 2013 Ondrej Holy <oholy@redhat.com> - 1.16.4-2
- Fix mtp crashes during unmount (#1031578)

* Fri Dec 6 2013 Ondrej Holy <oholy@redhat.com> - 1.16.4-1
- Update to 1.16.4 (#1038744)

* Fri Nov 22 2013 Ondrej Holy <oholy@redhat.com> 1.16.3-4
- MTP reading support (#1031584)

* Fri Oct 11 2013 Ondrej Holy <oholy@redhat.com> 1.16.3-3
- Drop obexftp subpackage due to serious problems (#1020348)

* Thu Jun 20 2013 Bastien Nocera <bnocera@redhat.com> 1.16.3-2
- Fix gvfs-afc crashes due to new libimobiledevice (#951731)

* Fri Jun 14 2013 Kalev Lember <kalevlember@gmail.com> - 1.16.3-1
- Update to 1.16.3

* Wed May 22 2013 Kalev Lember <kalevlember@gmail.com> - 1.16.2-2
- gvfs-archive: Add the update-desktop-database rpm scriptlets (#954214)

* Wed May 22 2013 Kalev Lember <kalevlember@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 1.16.1-1
- Update to 1.16.1

* Thu Mar 28 2013 Tomas Bzatek <tbzatek@redhat.com> - 1.16.0-1
- Update to 1.16.0

* Wed Mar 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.15.4-2
- Rebuild for new libimobiledevice

* Mon Mar 04 2013 Richard Hughes <rhughes@redhat.com> - 1.15.4-1
- Update to 1.15.4

* Wed Feb  6 2013 Tomas Bzatek <tbzatek@redhat.com> - 1.15.3-2
- Install systemd tmpfiles.d exclusion file for gvfs-fuse (#902743)

* Tue Feb  5 2013 Tomas Bzatek <tbzatek@redhat.com> - 1.15.3-1
- Update to 1.15.3

* Tue Jan 15 2013 Tomas Bzatek <tbzatek@redhat.com> - 1.15.2-1
- Update to 1.15.2

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> - 1.15.1-3
- Rebuilt for libcdio-0.90

* Wed Dec 19 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.15.1-2
- Rebuilt for new udisks

* Tue Dec 18 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.15.1-1
- Update to 1.15.1

* Fri Dec  7 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.15.0-3
- Enable verbose build messages
- Remove deprecated Encoding key from mount-archive.desktop

* Tue Nov  6 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.15.0-2
- Clarify licensing
- Explicitly disable HAL

* Mon Oct 29 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.15.0-1
- Update to 1.15.0

* Tue Sep 25 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.14.0-1
- Update to 1.14.0

* Tue Sep 18 2012 Matthias Clasen <mclasen@redhat.com> - 1.13.9-1
- Update to 1.13.9

* Wed Sep  5 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.13.8-1
- Update to 1.13.8

* Wed Aug 29 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.13.7-3
- Bring archive mounter back

* Mon Aug 27 2012 Cosimo Cecchi <cosimoc@redhat.com> - 1.13.7-2
- Make sure keyring integration is enabled

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 1.13.7-1
- Update to 1.13.7

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 1.13.4-1
- Update to 1.13.4

* Tue Aug  7 2012 Jindrich Novy <jnovy@redhat.com> - 1.13.3-4
- add BR: docbook-style-xsl so that gvfs actually builds

* Sun Aug  5 2012 Jindrich Novy <jnovy@redhat.com> - 1.13.3-3
- add patch to fix gvfs build against libgphoto2 (inspired by SUSE)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.13.3-1
- Update to 1.13.3

* Mon Jul 16 2012 Nils Philippsen <nils@redhat.com> - 1.13.2-2
- rebuild for new libgphoto2

* Tue Jun 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.13.2-1
- Update to 1.13.2

* Mon Jun  4 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.13.1-1
- Update to 1.13.1

* Wed May  2 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.13.0-1
- Update to 1.13.0

* Fri Apr 27 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.12.2-1
- Update to 1.12.2
- Backport multiseat patches from master

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.1-3
- Silence rpm scriptlet output

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.1-2
- Rebuild again for new libimobiledevice and usbmuxd

* Tue Apr 17 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Thu Apr 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.12.0-2
- Rebuild for new libimobiledevice and usbmuxd

* Mon Mar 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Tue Mar 20 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.5-1
- Update to 1.11.5

* Fri Feb 24 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.4-1
- Update to 1.11.4

* Tue Feb  7 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.3-1
- Update to 1.11.3

* Fri Feb  3 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.3-0.4.20120120
- Exclude the obexftp package from s390 builds

* Wed Jan 25 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.3-0.3.20120120
- Rebuilt for new libarchive

* Tue Jan 24 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.3-0.2.20120120
- Add udisks2 runtime Requires

* Fri Jan 20 2012 Matthias Clasen <mclasen@redhat.com> - 1.11.3-0.1.20120120-1
- Prelease that works with udisks2

* Wed Jan 18 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.11.2-1
- Update to 1.11.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 1.11.1-1
- Update to 1.11.1

* Tue Dec 13 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.11.0-5
- Rebuilt for new libbluray

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> - 1.11.0-4
- Rebuild for libcdio-0.83

* Wed Nov 16 2011 Adam Jackson <ajax@redhat.com> 1.11.0-3
- Rebuild for new libarchive

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for glibc bug#747377

* Wed Oct 26 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Mon Oct 17 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.10.1-1
- Update to 1.10.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Mon Sep  5 2011 Matthias Clasen <mclasen@redhat.com> - 1.9.5-1
- Update to 1.9.5

* Tue Aug 30 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.9.4-1
- Update to 1.9.4
- New AFP backend in separate subpackage

* Tue Aug 16 2011 Matthias Clasen <mclasen@redhat.com> - 1.9.3-1
- Update to 1.9.3
- Drop obsolete patches
- Clean up spec a bit

* Wed Jul 27 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.9.2-1
- Update to 1.9.2
- Enable real statfs calls in the fuse daemon

* Wed Jun 15 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Mon May 09 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 1.8.1-2
- Update gsettings scriptlet

* Tue Apr 26 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Fri Apr 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.8.0-3
- Build without HAL -> expect obexftp breakage.

* Mon Apr 18 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.8.0-2
- Fix threadsafety of closing channels
- Fix d-bus messages leaks
- Fix /dev symlink checks in gdu volume monitor

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Mon Mar 21 2011 Matthias Clasen <mclasen@redhat.com> - 1.7.3-1
- Update to 1.7.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  1 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Sun Dec 26 2010 Bastien Nocera <bnocera@redhat.com> 1.7.1-1
- Update to 1.7.1

* Thu Dec  2 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Mon Nov  1 2010 Matthias Clasen <mclasen@redhat.com> - 1.6.5-1
- Update to 1.6.5
- Drop upstreamed patches

* Mon Nov  1 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.4-4
- Use correct "usb:" address for GPhoto mounts with gudev (#642836)

* Wed Oct 13 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.4-3
- FUSE: Add O_TRUNC support for open()

* Mon Oct  4 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.4-2
- Fix sftp poll timeout

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 1.6.4-1
- Update to 1.6.4

* Wed Sep  8 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.3-3
- Fix smb daemons deadlock due to GConf initialization

* Mon Jul 12 2010 Dan Horák <dan[at]danny.cz> - 1.6.3-2
- s390(x) machines can't connect mobile phones or players

* Mon Jul 12 2010 Matthias Clasen <mclasen@redhat.com> - 1.6.3-1
- Update to 1.6.3

* Thu May 27 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.2-1
- Update to 1.6.2

* Tue May  4 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.1-3
- Fix Nautilus 100% CPU after trashing a file with an emblem (#584784)

* Mon Apr 26 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.1-2
- Explicitly require minimal glib2 version (#585912)

* Mon Apr 26 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Mon Apr 19 2010 Matthias Clasen <mclasen@redhat.com> - 1.6.0-2
- Use update-gio-modules

* Mon Mar 29 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Mon Mar 22 2010 Bastien Nocera <bnocera@redhat.com> 1.5.5-3
- Fix build with new libimobiledevice
- Don't mount both gphoto and AFC mounts on AFC devices

* Sun Mar 21 2010 Peter Robinson <pbrobinson@gmail.com> 1.5.5-2
- Rebuild for new stable libimobiledevice 

* Mon Mar  8 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.5-1
- Update to 1.5.5

* Thu Feb 25 2010 Matthias Clasen <mclasen@redhat.com> - 1.5.4-2
- Re-add missing service files

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 1.5.4-1
- Update to 1.5.4

* Mon Feb 15 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.3-2
- sftp: fix crash on unmount

* Tue Feb  9 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.3-1
- Update to 1.5.3

* Mon Feb  8 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.2-5
- ftp: backport several PASV/EPSV fixes from master (#542205, #555033)

* Fri Feb  5 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.2-4
- AFC: Use new libimobiledevice library

* Tue Jan 26 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.2-3
- Fix AFC build against new libiphone

* Mon Jan 25 2010 Matthias Clasen <mclasen@redhat.com> - 1.5.2-2
- Update the GIO module cache

* Mon Jan 25 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.2-1
- Update to 1.5.2

* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> - 1.5.1-6
- Rebuild for libcdio-0.82

* Mon Jan 18 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.1-5
- Avoid crash on race to mount gvfstrash (#555337)
- Nuke HAL volume monitor

* Tue Jan 12 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.5.1-4
- Don't leak mount job operation (#552842)
- Recognize gphoto2 cameras which don't implement get storageinfo (#552856)
- ObexFTP: Use a private D-Bus connection for obex-data-server (#539347)

* Tue Dec 15 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.5.1-3
- Rebuilt against new libiphone

* Mon Nov 30 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.5.1-2
- Metadata fixes
- SMB: Fix free space calculation for older samba servers
- fuse: Fix setting timestamps

* Wed Nov 18 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.5.1-1
- Update to 1.5.1
- AFC: temporarily disable setting file modification times

* Thu Nov 12 2009 Matthias Clasen <mclasen@redhat.com> 1.4.1-6
- Add obsoletes for gnome-mount

* Thu Nov 12 2009 Bastien Nocera <bnocera@redhat.com> 1.4.1-5
- Add obsoletes for gnome-vfs2-obexftp

* Tue Nov 10 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-4
- SMB: Support querying filesystem size and free space

* Tue Nov  3 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-3
- gdu-volume-monitor: don't crash on NULL devices (#529982)

* Mon Nov  2 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-2
- Reload .mount files when single package is installed

* Tue Oct 20 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Oct 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-7
- HTTP: Support g_file_input_stream_query_info()
- HTTP: Use libsoup header parsing function
- Set correct MIME type for MTP music players

* Wed Oct 14 2009 Bastien Nocera <bnocera@redhat.com> 1.4.0-6
- Fix crasher in ObexFTP (#528181)

* Fri Oct  9 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-5
- Don't always overwrite on trash restore
- Separate "Safely Remove Drive" from "Eject"
- Don't advertise can_poll for drives not using removable media
- Disallow mounting empty drives
- Disallow ejecting empty drives
- Silently drop eject error messages when detaching drive

* Thu Oct  8 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-4
- Fix Nautilus not displaying friendly icons for SSH-connected system (#526892)
- Actually apply the logical partitions patch

* Thu Oct  1 2009 Matthias Clasen <mclasen@redhat.com> - 1.4.0-3
- Consider logical partitions when deciding if a drive should be ignored

* Tue Sep 29 2009 Matthias Clasen <mclasen@redhat.com> - 1.4.0-2
- Fix the lack of icons in the http backend

* Mon Sep 21 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.3.6-2
- Rebuilt with new fuse

* Mon Sep  7 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.6-1
- Update to 1.3.6

* Wed Aug 26 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.5-2
- Don't mount interactively during login

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.5-1
- Update to 1.3.5

* Mon Aug 17 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.4-7
- Fix Nautilus can't create "untitled folder" on sftp mounts (#512611)

* Fri Aug 14 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-6
- Update AFC patch

* Thu Aug 13 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.4-5
- More complete fix for DAV mount path prefix issues

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-4
- Fix crash on startup for the afc volume monitor

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-3
- libgudev-devel is required for the gphoto2 monitor

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-2
- Add AFC backend

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Fri Aug  7 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.3-3
- Fix bad mount prefix stripping (part of #509612)
- Fix gvfsd-sftp segfault when asking a question
- Enable tar+xz in the archive mounter

* Tue Aug  4 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.3-2
- Fix gedit crashed with SEGV in strlen()
- Fix SMB protocol not handled when opening from a bookmark (#509832)

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Mon Jul 27 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.2-3
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.2-1
- Update to 1.3.2
- Drop upstreamed patches

* Mon Jun 22 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.1-2
- Bump version requirements
- Backport FTP and Computer backend patches from master

* Mon Jun 15 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.1-1
- Update to 1.3.1
- Drop obsolete patches

* Fri Jun 12 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.3-3
- Move bash-completion out of profile.d (#466883)

* Mon Jun  8 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.3-2
- SFTP: Increase timeout (#504339)

* Mon May 18 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.3-1
- Update to 1.2.3
- Prevent deadlocks in dnssd resolver (#497631)

* Tue May 12 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.2-5
- Require separate libtalloc to fix libsmbclient
- Ref the infos in next_files_finish (gnome #582195)
- FTP: parse file sizes > 4GB correctly (#499286)
- CDDA: allow query well-formed filenames only (#499266)

* Sat May 02 2009 David Zeuthen <davidz@redhat.com> - 1.2.2-4
- Don't show drives that are supposed to be hidden (#498649)
- Only automount if media or drive was just inserted - this fixes
  a problem with spurious automounts when partitioning/formatting

* Wed Apr 15 2009 David Zeuthen <davidz@redhat.com> - 1.2.2-3
- Sync with the gdu-volume-monitor branch

* Mon Apr 13 2009 Alexander Larsson <alexl@redhat.com> - 1.2.2-2
- Add ssh-auth-sock patch from svn

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 1.2.2-1
- Update to 1.2.2
- Allow eject even on non-ejectable devices

* Sat Apr 11 2009 David Zeuthen <davidz@redhat.com> - 1.2.1-5
- Don't show drives in computer:/// if media is available but
  no volumes are recognized (#495152)

* Sat Apr 11 2009 Matthias Clasen <mclasen@redhat.com> - 1.2.1-4
- No need for bash completion to be executable

* Thu Apr  9 2009 David Zeuthen <davidz@redhat.com> - 1.2.1-3
- Clean up gdu patches and bump BR for gdu to 0.3
- Avoiding showing volume for ignored mounts (#495033)

* Thu Apr  9 2009 David Zeuthen <davidz@redhat.com> - 1.2.1-2
- Avoid automounting device-mapper devices and similar (#494144)

* Thu Apr  2 2009 Matthias Clasen <mclasen@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Wed Mar 18 2009 David Zeuthen <davidz@redhat.com> - 1.2.0-2
- GNOME #575728 - crash in Open Folder: mounting a crypto volume

* Mon Mar 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Wed Mar 11 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.8-2
- Fix 100% cpu usage when connecting to a ssh key and denying key access
- Fix monitors leak

* Tue Mar 10 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.8-1
- Update to 1.1.8

* Mon Mar  9 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.7-5
- Expose device file attribute for all items in computer://

* Fri Mar  6 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.7-4
- Fix volume lists not filled correctly

* Wed Mar  4 2009 David Zeuthen <davidz@redhat.com> - 1.1.7-3
- Update GVfs gdu patch to fix mount detection confusion (#488399)

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 1.1.7-2
- Port to DeviceKit-disks

* Mon Mar  2 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.7-1
- Update to 1.1.7

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.6-1
- Update to 1.1.6

* Mon Feb  2 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.5-1
- Update to 1.1.5

* Wed Jan 28 2009 - Bastien Nocera <bnocera@redhat.com> - 1.1.4-2
- ObexFTP write support

* Tue Jan 20 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.4-1
- Update to 1.1.4

* Tue Jan 13 2009 Adrian Reber <adrian@lisas.de> - 1.1.3-4
- Rebuild for libcdio-0.81

* Mon Jan 12 2009 Matthias Clasen  <mclasen@redhat.com> - 1.1.3-3
- Fix dav+sd.mount

* Fri Jan  9 2009 Matthias Clasen  <mclasen@redhat.com> - 1.1.3-2
- Support moving files in the burn backend

* Tue Jan  6 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Wed Dec 17 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.2-2
- Update the smb-browse auth patch

* Tue Dec 16 2008 Matthias Clasen  <mclasen@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Fri Dec 12 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-5
- FTP: Fix PASV connections

* Tue Dec  9 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-4
- Add support for .tar.lzma archives in archive mounter

* Fri Dec  5 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-3
- Added experimental smb-browse auth patch

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 1.1.1-2
- Update file lists to include the dav+sd backend

* Tue Dec  2 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Mon Dec  1 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Fri Nov  7 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.2-4
- SMB: timestamp setting support (#461505)

* Tue Nov  4 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.2-3
- Return an empty array on success when no content type
  matches (#468946)

* Fri Oct 24 2008 Alexander Larsson <alexl@redhat.com> - 1.0.2-2
- Don't return generic fallback icons for files,
  as this means custom mimetypes don't work (from svn)

* Mon Oct 20 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Tue Oct  7 2008 Tomas Bzatek <tbzatek@redhat.com>  - 1.0.1-5
- Don't make warnings fatal (resolves #465693)

* Wed Oct  1 2008 David Zeuthen <davidz@redhat.com>  - 1.0.1-4
- Add patch for reverse mapping FUSE paths (bgo #530654)

* Mon Sep 29 2008 Matthias Clasen <mclasen@redhat.com>  - 1.0.1-3
- Fix mounting

* Mon Sep 29 2008 - Bastien Nocera <bnocera@redhat.com> - 1.0.1-2
- Update obexftp patch from upstream

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com>  - 1.0.1-1
- Update to 1.0.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com>  - 1.0.0-2
- Update to 1.0.0

* Fri Sep 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.8-6
- Update patch for missing file

* Fri Sep 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.8-5
- Updated patch, fixed deadlock whilst mounting

* Wed Sep 17 2008 Tomas Bzatek <tbzatek@redhat.com>  - 0.99.8-4
- Actually apply the kerberos patch

* Tue Sep 16 2008 Tomas Bzatek <tbzatek@redhat.com>  - 0.99.8-3
- SMB: Fix kerberos authentication

* Mon Sep 15 2008 Matthias Clasen <mclasen@redhat.com>  - 0.99.8-2
- Update to 0.99.8

* Mon Sep 15 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.7.1-4
- Update for BlueZ and obex-data-server D-Bus API changes

* Thu Sep 11 2008 Matthias Clasen <mclasen@redhat.com>  - 0.99.7.1-3
- Rebuild 

* Tue Sep 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.7.1-2
- Somebody made the build system be obnoxious and point out my
  errors in obvious ways

* Tue Sep 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.7.1-1
- Update to 0.99.7.1

* Tue Sep  2 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.6-1
- Update to 0.99.6

* Thu Aug 28 2008 Matthias Clasen <mclasen@redhat.com> - 0.99.5-3
- Add a comma

* Wed Aug 27 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.5-2
- Update some descriptions

* Wed Aug 20 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.5-1
- Update to 0.99.5

* Mon Aug  4 2008 Matthias Clasen  <mclasen@redhat.com> - 0.99.4-1
- Update to 0.99.4

* Sun Jul 27 2008 Matthias Clasen  <mclasen@redhat.com> - 0.99.3-2
- Use standard icon names

* Wed Jul 23 2008 Matthias Clasen  <mclasen@redhat.com> - 0.99.3-1
- Update to 0.99.3

* Tue Jul 22 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.2-1
- Update to 0.99.2
- Split out backends to separate packages

* Tue Jun 24 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.1-3
- gvfsd-trash: Skip autofs mounts

* Thu Jun 12 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.1-2
- Fix transfer of whole directories from FTP (#448560)

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 0.99.1-1
- Update to 0.99.1

* Tue May 27 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-10
- Add application/zip to the supported mime types for the archive
  backend (launchpad #211697)

* Sun Apr 19 2008 David Zeuthen <davidz@redhat.com> - 0.2.3-9
- Ensure archive mounts are read-only and turn on thumbnailing on them
- Update fuse threading patch

* Fri Apr 18 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-8
- Fix thread-safety issues in gvfs-fuse-daemon
- Prevent dbus from shutting us down unexpectedly

* Thu Apr 17 2008 David Zeuthen <davidz@redhat.com> - 0.2.3-7
- Put X-Gnome-Vfs-System=gio into mount-archarive.desktop (See #442835)

* Wed Apr 16 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-6
- Reenable gphoto automounting 
- Support unmounting all mounts for a scheme

* Wed Apr 16 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-5
- Fix hangs when unmounting gphoto mounts

* Wed Apr 16 2008 David Zeuthen <davidz@redhat.com> - 0.2.3-4
- Only show mounts in /media and inside $HOME (#442189)

* Mon Apr 14 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-3
- Fix a bug that causes application crashes (#441084)

* Fri Apr 11 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-2
- Fix a crash of the fuse daemon on 64bit

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Fri Mar 28 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Tue Mar 25 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-4
- Moved fuse stuff to a dedicated package

* Thu Mar 20 2008 Alexander Larsson <alexl@redhat.com> - 0.2.1-3
- Add patch with simple archive backend UI integration

* Tue Mar 19 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-2
- Added libarchive dependency for archive backend
- Require new libsmbclient in order to get smb backend working again

* Tue Mar 18 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-1
- Update to 0.2.1 (archive backend temporarily disabled)

* Mon Mar 17 2008 Matthias Clasen  <mclasen@redhat.com> - 0.2.0.1-2
- Silence %%post

* Mon Mar 10 2008 Matthias Clasen  <mclasen@redhat.com> - 0.2.0.1-1
- Update to 0.2.0.1

* Thu Mar  6 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.1.11-2
- Add patch that fixes a deadlock when foreign volume is removed

* Tue Mar  4 2008 Matthias Clasen  <mclasen@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Tue Mar 04 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Mon Feb 25 2008 Alexander Larsson <alexl@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Thu Feb 14 2008 Alexander Larsson <alexl@redhat.com> - 0.1.7-3
- Add patch that fixes a smb bug that can cause short reads when copying files

* Tue Feb 12 2008 Alexander Larsson <alexl@redhat.com> - 0.1.7-2
- Fix double free in hal volume monitor
- Ensure gconf module is built by adding build dep

* Mon Feb 11 2008 Matthias Clasen <mclasen@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Mon Jan 28 2008 Matthias Clasen <mclasen@redhat.com> - 0.1.5-1
- Update to 0.1.5
- Reenable http/dav 

* Mon Jan 21 2008 Alexander Larsson <alexl@redhat.com> - 0.1.4-2 
- Remove the http/dav stuff for now, as we don't have the latest libsoup

* Mon Jan 21 2008 Alexander Larsson <alexl@redhat.com> - 0.1.4-1
- Update to 0.1.4
- Send USR1 in post to reload config

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> 0.1.2-1
- Update to 0.1.2

* Tue Jan  8 2008 Matthias Clasen <mclasen@redhat.com> 0.1.1-1
- Update to 0.1.1

* Thu Dec 20 2007 Matthias Clasen <mclasen@redhat.com> 0.1.0-1
- Initial packaging
