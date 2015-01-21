FROM ubuntu:13.10
MAINTAINER Kuba Kucharski <kuba@kucharski.it>

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install wget
RUN wget --quiet --no-check-certificate -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >> /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y upgrade
RUN locale-gen --no-purge en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN apt-get -y install build-essential postgresql-9.3 postgresql-contrib-9.3 postgresql-9.3-postgis-2.1 postgis binutils libproj-dev gdal-bin python-pip python libpq-dev libpython-dev
RUN wget http://download.osgeo.org/geos/geos-3.3.8.tar.bz2
RUN tar xjf geos-3.3.8.tar.bz2; cd geos-3.3.8; ./configure; make; make install


RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

