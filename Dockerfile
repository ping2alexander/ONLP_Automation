
# Base image for our new docker image.
FROM debian:buster
# Maintainer of an image.
MAINTAINER My Name alexj@celestica.com


RUN apt-get update && apt-get install -y build-essential \
                                         cmake \
                                         curl \
                                         default-jre \
                                         gcc \
                                         git \
                                         inetutils-ping \
                                         iproute2 \
                                         isc-dhcp-client \
                                         libffi-dev \
                                         libssl-dev \
                                         libxml2 \
                                         libxslt1-dev \
                                         make \
                                         openssh-server \
                                         psmisc \
                                         python \
                                         python-dev \
                                         python3-pip \
                                         python3-venv \
					 python-pip \
                                         rsyslog \
                                         snmp \
                                         sshpass \
                                         sudo \
                                         tcpdump \
                                         telnet \
                                         vim \
                                         #python-is-python2 \
                                         software-properties-common

RUN pip install setuptools==44.1.1

RUN pip install cffi==1.12.0 \
                contextlib2==0.6.0.post1 \
                cryptography==3.3.2 \
                "future>=0.16.0" \
                gitpython \
                ipaddr \
                jinja2==2.7.2 \
                jsonpatch \
                lxml \
                natsort \
                netaddr \
                netmiko==2.4.2 \
                paramiko==2.7.1 \
                passlib \
                pexpect \
                prettytable \
                psutil \
                pyasn1==0.1.9 \
                pyfiglet \
                lazy-object-proxy==1.6.0 \
                pylint==1.8.1 \
                pysnmp==4.2.5 \
                pytest-repeat \
                pytest-html \
                pytest-xdist==1.28.0 \
                pytest==4.6.5 \
                requests \
                rpyc \
                six \
                tabulate \
                statistics \
                textfsm==1.1.2 \
                virtualenv \
                retry \
                thrift==0.11.0 \
                allure-pytest==2.8.22 \
                msrest==0.6.21 \
		markupsafe \
		ansible==2.8.12 \
		colorama==0.1.7 \
		schema

RUN python3 -m pip install --upgrade --ignore-installed pip setuptools==58.4.0 wheel==0.33.6

RUN python3 -m pip install setuptools-rust \
                            aiohttp \
                            defusedxml \
                            azure-kusto-ingest \
                            azure-kusto-data \
                            cffi \
                            contextlib2==0.6.0.post1 \
                            cryptography==3.3.2 \
                            "future>=0.16.0" \
                            gitpython \
                            ipaddr \
                            ipython==5.4.1 \
                            snappi[ixnetwork,convergence]==0.7.44 \
                            jinja2==2.7.2 \
                            jsonpatch \
                            lxml \
                            natsort \
                            netaddr \
                            netmiko==2.4.2 \
                            paramiko==2.7.1 \
                            passlib \
                            pexpect \
                            prettytable \
                            psutil \
                            pyasn1==0.4.8 \
                            pyfiglet \
                            pylint==1.8.1 \
                            pyro4 \
                            pysnmp==4.4.12 \
                            pytest-repeat \
                            pytest-html \
                            pytest-xdist==1.28.0 \
                            pytest \
                            redis \
                            requests \
                            rpyc \
                            six \
                            tabulate \
                            textfsm==1.1.2 \
                            virtualenv \
                            pysubnettree \
                            #nnpy \
                            dpkt \
                            pycryptodome==3.9.8 \
                            ansible==2.8.12 \
                            pytest-ansible \
                            allure-pytest==2.8.22 \
                            retry \
                            thrift==0.11.0 \
                            ptf \
                            scapy==2.4.5 \
                            celery[redis]==4.4.7 \
                            msrest==0.6.21 \
			    colorama==0.1.7 \
		            schema

RUN pip2 install schema

RUN pip2 install colorama

#enable ssh

RUN apt-get update && apt-get -y install openssh-server supervisor
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22
CMD ["/usr/bin/supervisord"]
