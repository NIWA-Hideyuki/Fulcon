# Fulcon
# Copyright (C) 2015-2016 NIWA Hideyuki

prefix ?= /usr
exec_prefix ?= ${prefix}
datarootdir ?= ${prefix}/share
sbindir ?= ${exec_prefix}/sbin
libdir ?= ${exec_prefix}/lib
localstatedir ?= /var
mandir ?= ${prefix}/share/man
docdir ?= ${datarootdir}/doc/fulcon-${VERSION}

fulcon :

install : install-cmd install-subcmd install-driver install-doc

install-cmd :
	mkdir -p $(DESTDIR)$(sbindir)/sbin
	install -m 755 cmd/fulcon $(DESTDIR)$(sbindir)/fulcon

install-subcmd : 
	mkdir -p $(DESTDIR)$(libdir)/fulcon/sbin
	install -m 755 subcmd/default-image $(DESTDIR)$(libdir)/fulcon/sbin/default-image
	install -m 755 subcmd/driver-name $(DESTDIR)$(libdir)/fulcon/sbin/driver-name
	install -m 755 subcmd/list $(DESTDIR)$(libdir)/fulcon/sbin/list
	install -m 755 subcmd/sysgen $(DESTDIR)$(libdir)/fulcon/sbin/sysgen
	install -m 755 subcmd/clone $(DESTDIR)$(libdir)/fulcon/sbin/clone
	install -m 755 subcmd/erase $(DESTDIR)$(libdir)/fulcon/sbin/erase
	install -m 755 subcmd/start $(DESTDIR)$(libdir)/fulcon/sbin/start
	install -m 755 subcmd/stop $(DESTDIR)$(libdir)/fulcon/sbin/stop
	install -m 755 subcmd/suspend $(DESTDIR)$(libdir)/fulcon/sbin/suspend
	install -m 755 subcmd/resume $(DESTDIR)$(libdir)/fulcon/sbin/resume
	install -m 755 subcmd/rename $(DESTDIR)$(libdir)/fulcon/sbin/rename
	install -m 755 subcmd/br-info $(DESTDIR)$(libdir)/fulcon/sbin/br-info
	install -m 755 subcmd/br-add $(DESTDIR)$(libdir)/fulcon/sbin/br-add
	install -m 755 subcmd/br-del $(DESTDIR)$(libdir)/fulcon/sbin/br-del
	install -m 755 subcmd/net-add $(DESTDIR)$(libdir)/fulcon/sbin/net-add
	install -m 755 subcmd/net-del $(DESTDIR)$(libdir)/fulcon/sbin/net-del
	install -m 755 subcmd/net-info $(DESTDIR)$(libdir)/fulcon/sbin/net-info
	install -m 755 subcmd/resource $(DESTDIR)$(libdir)/fulcon/sbin/resource
	install -m 755 subcmd/setup $(DESTDIR)$(libdir)/fulcon/sbin/setup
	install -m 755 subcmd/load-ocf $(DESTDIR)$(libdir)/fulcon/sbin/load-ocf
	install -m 755 subcmd/save-ocf $(DESTDIR)$(libdir)/fulcon/sbin/save-ocf
	install -m 755 subcmd/ls-ocf $(DESTDIR)$(libdir)/fulcon/sbin/ls-ocf
	install -m 755 subcmd/del-ocf $(DESTDIR)$(libdir)/fulcon/sbin/del-ocf
	install -m 755 subcmd/add-user $(DESTDIR)$(libdir)/fulcon/sbin/add-user
	install -m 755 subcmd/del-user $(DESTDIR)$(libdir)/fulcon/sbin/del-user
	install -m 755 subcmd/set-passwd $(DESTDIR)$(libdir)/fulcon/sbin/set-passwd
	install -m 755 subcmd/set-driver $(DESTDIR)$(libdir)/fulcon/sbin/set-driver
	install -m 755 subcmd/image-catalog $(DESTDIR)$(libdir)/fulcon/sbin/image-catalog
	install -m 755 subcmd/ls-image $(DESTDIR)$(libdir)/fulcon/sbin/ls-image
	install -m 755 subcmd/del-image $(DESTDIR)$(libdir)/fulcon/sbin/del-image
	install -m 755 subcmd/set-default-image $(DESTDIR)$(libdir)/fulcon/sbin/set-default-image
	install -m 755 subcmd/setup-prog $(DESTDIR)$(libdir)/fulcon/sbin/setup-prog
	install -m 755 subcmd/update $(DESTDIR)$(libdir)/fulcon/sbin/update
	install -m 755 subcmd/deploy $(DESTDIR)$(libdir)/fulcon/sbin/deploy
	install -m 755 subcmd/console $(DESTDIR)$(libdir)/fulcon/sbin/console
	install -m 755 subcmd/help $(DESTDIR)$(libdir)/fulcon/sbin/help

install-driver : install-driver-docker

install-driver-docker : install-dockerfile
	mkdir -p $(DESTDIR)$(libdir)/fulcon/driver/docker
	install -m 755 driver/docker/fulcon-exec $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-exec
	install -m 755 driver/docker/fulcon-list-all $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-list-all
	install -m 755 driver/docker/fulcon-list-paused $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-list-paused
	install -m 755 driver/docker/fulcon-list-running $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-list-running
	install -m 755 driver/docker/fulcon-list-stopped $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-list-stopped
	install -m 755 driver/docker/fulcon-start $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-start
	install -m 755 driver/docker/fulcon-stop $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-stop
	install -m 755 driver/docker/fulcon-suspend $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-suspend
	install -m 755 driver/docker/fulcon-resume $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-resume
	install -m 755 driver/docker/fulcon-sysgen $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-sysgen
	install -m 755 driver/docker/fulcon-erase $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-erase
	install -m 755 driver/docker/fulcon-image-gc $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-image-gc
	install -m 755 driver/docker/fulcon-rename $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-rename
	install -m 755 driver/docker/fulcon-cp-in $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-cp-in
	install -m 755 driver/docker/fulcon-cp-out $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-cp-out
	install -m 755 driver/docker/fulcon-ls-image $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-ls-image
	install -m 755 driver/docker/fulcon-del-image $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-del-image
	install -m 755 driver/docker/fulcon-load-ocf $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-load-ocf
	install -m 755 driver/docker/fulcon-save-ocf $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-save-ocf
	mkdir -p $(DESTDIR)$(libdir)/fulcon/lib
	install -m 755 driver/docker/fulcon-cpu $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-cpu
	install -m 755 driver/docker/fulcon-cpuset $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-cpuset
	install -m 755 driver/docker/docker-find-id $(DESTDIR)$(libdir)/fulcon/driver/docker/docker-find-id
	install -m 755 lib/lib-erase $(DESTDIR)$(libdir)/fulcon/lib/lib-erase
	install -m 755 driver/docker/find-proc $(DESTDIR)$(libdir)/fulcon/driver/docker/find-proc
	install -m 755 lib/lib-list $(DESTDIR)$(libdir)/fulcon/lib/lib-list
	install -m 755 driver/docker/fulcon-mem $(DESTDIR)$(libdir)/fulcon/driver/docker/fulcon-mem
	install -m 755 lib/lib-start $(DESTDIR)$(libdir)/fulcon/lib/lib-start
	install -m 755 lib/lib-stop $(DESTDIR)$(libdir)/fulcon/lib/lib-stop
	install -m 755 lib/lib-suspend $(DESTDIR)$(libdir)/fulcon/lib/lib-suspend
	install -m 755 lib/lib-resume $(DESTDIR)$(libdir)/fulcon/lib/lib-resume
	install -m 755 lib/lib-rename $(DESTDIR)$(libdir)/fulcon/lib/lib-rename
	install -m 755 lib/lib-sysgen $(DESTDIR)$(libdir)/fulcon/lib/lib-sysgen
	install -m 755 lib/lib-clone $(DESTDIR)$(libdir)/fulcon/lib/lib-clone
	install -m 755 lib/lib-load-ocf $(DESTDIR)$(libdir)/fulcon/lib/lib-load-ocf
	install -m 755 lib/lib-save-ocf $(DESTDIR)$(libdir)/fulcon/lib/lib-save-ocf
	install -m 755 lib/lib-add-user $(DESTDIR)$(libdir)/fulcon/lib/lib-add-user
	install -m 755 lib/lib-del-user $(DESTDIR)$(libdir)/fulcon/lib/lib-del-user
	install -m 755 driver/docker/set-passwd $(DESTDIR)$(libdir)/fulcon/driver/docker/set-passwd
	install -m 755 lib/lib-ls-image $(DESTDIR)$(libdir)/fulcon/lib/lib-ls-image
	install -m 755 lib/lib-del-image $(DESTDIR)$(libdir)/fulcon/lib/lib-del-image
	install -m 755 lib/lib-setup-prog $(DESTDIR)$(libdir)/fulcon/lib/lib-setup-prog
	install -m 755 lib/lib-update $(DESTDIR)$(libdir)/fulcon/lib/lib-update
	install -m 755 lib/lib-deploy $(DESTDIR)$(libdir)/fulcon/lib/lib-deploy
	install -m 755 lib/lib-console $(DESTDIR)$(libdir)/fulcon/lib/lib-console
	install -m 755 driver/docker/net-ipv4 $(DESTDIR)$(libdir)/fulcon/driver/docker/net-ipv4
	install -m 755 lib/lib-image-catalog $(DESTDIR)$(libdir)/fulcon/lib/lib-image-catalog
	install -m 755 lib/parmchk-num-kmg $(DESTDIR)$(libdir)/fulcon/lib/parmchk-num-kmg

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
	install -m 644 doc/default-driver $(DESTDIR)$(localstatedir)/lib/fulcon/default-driver


uninstall : 
	rm -f $(DESTDIR)$(sbindir)/fulcon
	rm -rf $(DESTDIR)$(libdir)/fulcon
	rm -rf $(DESTDIR)/$(docdir)

clean :

