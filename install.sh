# install libpq-dev
# install postgresql
# install python-dev
# pip install psycop2




#RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
apt-get -y update
apt-get -y install ca-certificates
apt-get -y install wget
wget --quiet --no-check-certificate -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >> /etc/apt/sources.list
apt-get -y update
apt-get -y upgrade
locale-gen --no-purge en_US.UTF-8
export LC_ALL=en_US.UTF-8
update-locale LANG=en_US.UTF-8
apt-get -y install postgresql-9.3 postgresql-contrib-9.3 postgresql-9.3-postgis-2.1 postgis
echo "host    all             all             0.0.0.0/0               md5" >> /etc/postgresql/9.3/main/pg_hba.conf
service postgresql start && /bin/su postgres -c "createuser -d -s -r -l docker" && /bin/su postgres -c "psql postgres -c \"ALTER USER docker WITH ENCRYPTED PASSWORD 'docker'\"" && service postgresql stop
echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf
echo "port = 5432" >> /etc/postgresql/9.3/main/postgresql.conf

apt-get install libpq-dev python-dev
service postgresql start
/bin/su postgres -c "createdb powermanager" 


