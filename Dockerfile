FROM httpd:2.4
COPY ./conf/httpd.conf /usr/local/apache2/conf/httpd.conf
RUN useradd -ms /bin/bash student
RUN apt-get update
RUN apt-get install -y nano less man-db manpages-dev python3 
RUN apt-get install -y procps net-tools traceroute iputils-ping dnsutils whois curl dos2unix
RUN apt-get upgrade -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN dos2unix /usr/local/apache2/cgi-bin/*
WORKDIR /home/student
