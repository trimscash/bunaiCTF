FROM ubuntu:22.10


RUN mkdir /var/www
# workdir
WORKDIR /var/www/

COPY ./ ./


ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install python3 \
                       python3-pip
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

RUN chmod 755 -R /var/www
RUN adduser -u 1000 unko64
USER unko64

ENV PYTHONIOENCODING utf-8

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
