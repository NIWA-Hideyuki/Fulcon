# Fulcon
# Copyright (C) 2015 NIWA Hideyuki

prefix ?= /usr
exec_prefix ?= ${prefix}
datarootdir ?= ${prefix}/share
sbindir ?= ${exec_prefix}/sbin
libdir ?= ${exec_prefix}/lib
localstatedir ?= /var
mandir ?= ${prefix}/share/man
docdir ?= ${datarootdir}/doc/fulcon-${VERSION}

fulcon :

install : install-cmd install-lib install-driver install-doc

install-cmd :
	mkdir -p $(DESTDIR)$(sbindir)/sbin
	install -m 755 cmd/fulcon $(DESTDIR)$(sbindir)/fulcon

install-lib : 
	mkdir -p $(DESTDIR)$(libdir)/fulcon/sbin
	install -m 755 lib/default-image $(DESTDIR)$(libdir)/fulcon/sbin/default-image
	install -m 755 lib/driver-name $(DESTDIR)$(libdir)/fulcon/sbin/driver-name
	install -m 755 lib/list $(DESTDIR)$(libdir)/fulcon/sbin/list
	install -m 755 lib/sysgen $(DESTDIR)$(libdir)/fulcon/sbin/sysgen
	install -m 755 lib/clone $(DESTDIR)$(libdir)/fulcon/sbin/clone
	install -m 755 lib/erase $(DESTDIR)$(libdir)/fulcon/sbin/erase
	install -m 755 lib/start $(DESTDIR)$(libdir)/fulcon/sbin/start
	install -m 755 lib/stop $(DESTDIR)$(libdir)/fulcon/sbin/stop
	install -m 755 lib/suspend $(DESTDIR)$(libdir)/fulcon/sbin/suspend
	install -m 755 lib/resume $(DESTDIR)$(libdir)/fulcon/sbin/resume
	install -m 755 lib/rename $(DESTDIR)$(libdir)/fulcon/sbin/rename
	install -m 755 lib/br-info $(DESTDIR)$(libdir)/fulcon/sbin/br-info
	install -m 755 lib/br-add $(DESTDIR)$(libdir)/fulcon/sbin/br-add
	install -m 755 lib/br-del $(DESTDIR)$(libdir)/fulcon/sbin/br-del
	install -m 755 lib/net-add $(DESTDIR)$(libdir)/fulcon/sbin/net-add
	install -m 755 lib/net-del $(DESTDIR)$(libdir)/fulcon/sbin/net-del
	install -m 755 lib/net-info $(DESTDIR)$(libdir)/fulcon/sbin/net-info
	install -m 755 lib/resource $(DESTDIR)$(libdir)/fulcon/sbin/resource
	install -m 755 lib/setup $(DESTDIR)$(libdir)/fulcon/sbin/setup
	install -m 755 lib/load-ocf $(DESTDIR)$(libdir)/fulcon/sbin/load-ocf
	install -m 755 lib/save-ocf $(DESTDIR)$(libdir)/fulcon/sbin/save-ocf
	install -m 755 lib/ls-ocf $(DESTDIR)$(libdir)/fulcon/sbin/ls-ocf
	install -m 755 lib/del-ocf $(DESTDIR)$(libdir)/fulcon/sbin/del-ocf
	install -m 755 lib/add-user $(DESTDIR)$(libdir)/fulcon/sbin/add-user
	install -m 755 lib/del-user $(DESTDIR)$(libdir)/fulcon/sbin/del-user
	install -m 755 lib/set-passwd $(DESTDIR)$(libdir)/fulcon/sbin/set-passwd
	install -m 755 lib/image-catalog $(DESTDIR)$(libdir)/fulcon/sbin/image-catalog
	install -m 755 lib/ls-image $(DESTDIR)$(libdir)/fulcon/sbin/ls-image
	install -m 755 lib/del-image $(DESTDIR)$(libdir)/fulcon/sbin/del-image
	install -m 755 lib/set-default-image $(DESTDIR)$(libdir)/fulcon/sbin/set-default-image
	install -m 755 lib/update $(DESTDIR)$(libdir)/fulcon/sbin/update
	install -m 755 lib/console $(DESTDIR)$(libdir)/fulcon/sbin/console
	install -m 755 lib/help $(DESTDIR)$(libdir)/fulcon/sbin/help

install-driver : install-driver-docker

install-driver-docker : install-dockerfile
	mkdir -p $(DESTDIR)$(libdir)/fulcon/driver/docker
	install -m 755 driver/docker/cpu $(DESTDIR)$(libdir)/fulcon/driver/docker/cpu
	install -m 755 driver/docker/cpuset $(DESTDIR)$(libdir)/fulcon/driver/docker/cpuset
	install -m 755 driver/docker/docker-find-id $(DESTDIR)$(libdir)/fulcon/driver/docker/docker-find-id
	install -m 755 driver/docker/erase $(DESTDIR)$(libdir)/fulcon/driver/docker/erase
	install -m 755 driver/docker/find-proc $(DESTDIR)$(libdir)/fulcon/driver/docker/find-proc
	install -m 755 driver/docker/list $(DESTDIR)$(libdir)/fulcon/driver/docker/list
	install -m 755 driver/docker/mem $(DESTDIR)$(libdir)/fulcon/driver/docker/mem
	install -m 755 driver/docker/br-info $(DESTDIR)$(libdir)/fulcon/driver/docker/br-info
	install -m 755 driver/docker/net-add $(DESTDIR)$(libdir)/fulcon/driver/docker/net-add
	install -m 755 driver/docker/net-del $(DESTDIR)$(libdir)/fulcon/driver/docker/net-del
	install -m 755 driver/docker/net-ipv4 $(DESTDIR)$(libdir)/fulcon/driver/docker/net-ipv4
	install -m 755 driver/docker/start $(DESTDIR)$(libdir)/fulcon/driver/docker/start
	install -m 755 driver/docker/stop $(DESTDIR)$(libdir)/fulcon/driver/docker/stop
	install -m 755 driver/docker/suspend $(DESTDIR)$(libdir)/fulcon/driver/docker/suspend
	install -m 755 driver/docker/resume $(DESTDIR)$(libdir)/fulcon/driver/docker/resume
	install -m 755 driver/docker/rename $(DESTDIR)$(libdir)/fulcon/driver/docker/rename
	install -m 755 driver/docker/sysgen $(DESTDIR)$(libdir)/fulcon/driver/docker/sysgen
	install -m 755 driver/docker/clone $(DESTDIR)$(libdir)/fulcon/driver/docker/clone
	install -m 755 driver/docker/clone-newimage $(DESTDIR)$(libdir)/fulcon/driver/docker/clone-newimage
	install -m 755 driver/docker/setup $(DESTDIR)$(libdir)/fulcon/driver/docker/setup
	install -m 755 driver/docker/load-ocf $(DESTDIR)$(libdir)/fulcon/driver/docker/load-ocf
	install -m 755 driver/docker/save-ocf $(DESTDIR)$(libdir)/fulcon/driver/docker/save-ocf
	install -m 755 driver/docker/add-user $(DESTDIR)$(libdir)/fulcon/driver/docker/add-user
	install -m 755 driver/docker/del-user $(DESTDIR)$(libdir)/fulcon/driver/docker/del-user
	install -m 755 driver/docker/set-passwd $(DESTDIR)$(libdir)/fulcon/driver/docker/set-passwd
	install -m 755 driver/docker/ls-image $(DESTDIR)$(libdir)/fulcon/driver/docker/ls-image
	install -m 755 driver/docker/del-image $(DESTDIR)$(libdir)/fulcon/driver/docker/del-image
	install -m 755 driver/docker/update $(DESTDIR)$(libdir)/fulcon/driver/docker/update
	install -m 755 driver/docker/console $(DESTDIR)$(libdir)/fulcon/driver/docker/console
	install -m 755 driver/docker/parmchk-num-kmg $(DESTDIR)$(libdir)/fulcon/driver/docker/parmchk-num-kmg

install-dockerfile :
	mkdir -p $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile
	mkdir -p $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/centos7
	install -m 755 driver/docker/dockerfile/centos7/Dockerfile $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/centos7/Dockerfile
	mkdir -p $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/ubuntu1504
	install -m 755 driver/docker/dockerfile/ubuntu1504/Dockerfile $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/ubuntu1504/Dockerfile
	install -m 755 driver/docker/dockerfile/ubuntu1504/80proxy $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/ubuntu1504/80proxy
	mkdir -p $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/ubuntu1510
	install -m 755 driver/docker/dockerfile/ubuntu1510/Dockerfile $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/ubuntu1510/Dockerfile
	install -m 755 driver/docker/dockerfile/ubuntu1510/80proxy $(DESTDIR)/$(localstatedir)/lib/fulcon/driver/dockerfile/ubuntu1510/80proxy

install-doc :
	mkdir -p $(DESTDIR)$(libdir)/fulcon/doc
	install -m 644 doc/help.txt $(DESTDIR)$(libdir)/fulcon/doc/help.txt
	install -m 644 README $(DESTDIR)$(libdir)/fulcon/doc/README
	mkdir -p $(DESTDIR)$(localstatedir)/lib/fulcon
	install -m 644 doc/default-image $(DESTDIR)$(localstatedir)/lib/fulcon/default-image


uninstall : 
	rm -f $(DESTDIR)$(sbindir)/fulcon
	rm -rf $(DESTDIR)$(libdir)/fulcon
	rm -rf $(DESTDIR)/$(docdir)
	rm -rf $(DESTDIR)/var/lib/fulcon

clean :

