FROM ubuntu
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
RUN apt-get update && apt-get upgrade -y
RUN rm -f /lib/systemd/systemd
RUN apt-get install --reinstall -y --force-yes systemd-services \
	systemd-shim systemd-sysv upstart  sysv-rc sysvinit-utils
RUN mv /sbin/initctl.distrib /sbin/initctl
RUN apt-get install -qq -y --force-yes rsyslog apt-utils sudo vim \
	language-pack-ja less openssh-server net-tools
RUN update-rc.d rsyslog defaults
RUN update-rc.d ssh defaults

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

