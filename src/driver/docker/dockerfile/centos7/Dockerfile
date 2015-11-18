FROM centos
MAINTAINER NIWA Hideyuki 

# setup proxy
# The first # is removed, rewrite the following "http://xxx" in proxy. 

#ENV http_proxy http://xxx
#ENV https_proxy http://xxx
#ENV ftp_proxy http://xxx
#RUN /usr/bin/echo "proxy=http://xxx" >> /etc/yum.conf

ENV container docker

# setup systemd
RUN yum -y update; yum clean all
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs sh

# enable localedef
RUN yum -y update glibc-common
RUN yum -y reinstall glibc-common

# install packages
RUN yum -y install net-tools yum-langpacks system-config-language perl sudo \
	rsyslog cronie crontabs cronie-anacron

# unused services
RUN rm -rf /etc/systemd/system/*
RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    systemd-remount-fs.service sys-kernel-config.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount
RUN systemctl disable remote-fs.service gdm.service
RUN systemctl mask systemd-logind.service
RUN systemctl set-default multi-user.target

# setup rsyslog
RUN systemctl enable rsyslog.service

# setup cron
RUN systemctl enable crond.service

# install ssh
RUN yum -y install openssh-server initscripts openssh-clients

# setup ssh
RUN printf "\nUseDNS=no\n" >> /etc/ssh/sshd_config
RUN printf "\nGSSAPIAuthentication no\nAddressFamily inet\n" >>/etc/ssh/ssh_config
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN mkdir /var/run/sshd && chown root /var/run/sshd

RUN yum -y remove avahi avahi-libs avahi-glib

RUN systemctl disable network.service; \
    systemctl mask rhel-dmesg.service; \
    true

# setup root passwd
RUN passwd -l root

VOLUME ["/sys/fs/cgroup"]
VOLUME ["/run"]

CMD ["/sbin/init"]
