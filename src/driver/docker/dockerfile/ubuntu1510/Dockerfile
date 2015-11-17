FROM ubuntu:15.10
MAINTAINER NIWA Hideyuki

# setup proxy
# The first # is removed, rewrite the following "http://xxx" in proxy. 
# Please rewrite in "80proxy" file similarly. 

#ENV http_proxy http://xxx
#ENV https_proxy http://xxx
#ENV ftp_proxy http://xxx
#ADD 80proxy /etc/apt/apt.conf.d/

ENV container docker
ENV DEBIAN_FRONTEND noninteractive

# install packages
RUN apt-get update 
RUN apt-get install --reinstall -y --force-yes upstart
RUN apt-get install --reinstall -y --force-yes sysvinit-utils || true
RUN mv /sbin/initctl.distrib /sbin/initctl
RUN apt-get install -qq -y --force-yes rsyslog initscripts apt-utils sudo vim \
	less openssh-server net-tools
RUN rm -f /etc/apt/apt.conf.d/docker*
RUN rm -rf /etc/systemd/system/*
RUN systemctl mask systemd-logind.service
RUN systemctl disable remote-fs.service gdm.service 
RUN systemctl set-default multi-user.target
RUN systemctl enable rsyslog ssh

# setup ssh
RUN printf "\nUseDNS=no\n" >> /etc/ssh/sshd_config
RUN printf "\nGSSAPIAuthentication no\nAddressFamily inet\n" >>/etc/ssh/ssh_config
RUN rm -rf /etc/ssh/ssh_host_rsa_key && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN sed -i /etc/ssh/sshd_config \
	-e "s/PermitRootLogin without-password/PermitRootLogin yes/"

# setup passwd
RUN passwd -l root


VOLUME ["/sys/fs/cgroup"]
VOLUME ["/run"]

ENTRYPOINT ["/sbin/init"]

