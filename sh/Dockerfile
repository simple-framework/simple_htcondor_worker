FROM cern/cc7-base
MAINTAINER Mayank Sharma (mayank.sharma@cern.ch)
ENV SIMPLE_CONFIG_DIR=/etc/simple_grid
ENV HTCONDOR_CE_CONFIG_DIR=/etc/condor-ce
ENV HTCONDOR_CONFIG_DIR=/etc/condor

## Install condor ##
RUN yum install -y wget
RUN wget https://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor
RUN rpm --import RPM-GPG-KEY-HTCondor
WORKDIR /etc/yum.repos.d/
RUN wget https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo
RUN yum -y install condor HEP_OSlibs
## Install utils ##
RUN yum install -y vim less

RUN yum install -y iproute openssh openssh-server openssh-clients openssl-libs
RUN yum install -y net-tools telnet
ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

WORKDIR /root
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]