FROM docker-devcloud.di2e.net/di2e/jdk8:1.8.0_151
#RUN yum update -y
COPY epel.repo /etc/yum.repos.d
COPY RPM-GPG-KEY-EPEL-7 /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
COPY di2e.repo /etc/yum.repos.d
RUN yum install -y yum-plugin-ovl
RUN rm -rf /var/cache/yum/*
RUN yum clean all
RUN yum install -y make
RUN yum install -y gcc
RUN yum install -y gcc-c++
RUN yum install -y curl
RUN yum install -y git
RUN yum install -y python36
RUN yum install -y python36-setuptools
RUN yum install -y python2-pip
RUN pip install -U setuptools
RUN pip install --upgrade pip
RUN easy_install pip
RUN pip install coveralls bandit
RUN yum install -y python-virtualenv

RUN yum install -y nodejs openldap cyrus-sasl saslwrapper openssl-devel
RUN yum install -y libffi-devel
RUN mkdir mkdir /www

COPY docker-entrypoint.sh /

WORKDIR /app
COPY . /app/

RUN pip install -e .
RUN pip install "file://`pwd`#egg=lemur[dev]"
RUN pip install "file://`pwd`#egg=lemur[tests]"

ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8181 8181
CMD [ "bash"]
#CMD ["lemur", "start", "-b", "0.0.0.0:8181" ]
