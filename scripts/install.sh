#!/bin/bash
SITE_NAME="isells"
SITE_DOMAIN1="isells.eu"
SITE_DOMAIN2="isells.ru"

#if test -z /data
if [ ! -d /data ]
then mkdir /data
chown www-data.www-data /data
echo "folder \"/data\" just created"
fi

# That will remove the directory if it's present, otherwise do nothing.
rm -rf /data/${SITE_NAME}

mkdir /data/${SITE_NAME}
chown www-data.www-data /data/${SITE_NAME}
echo "folder \"/data/${SITE_NAME}\" just created"

cd /data/${SITE_NAME}
mkdir logs
mkdir media
mkdir static
chown www-data.www-data *
echo "folders \"logs\", \"media\" and \"static\" was created and chowned to \"www-data\""
init_site(){
    cd /data/${SITE_NAME};
    virtualenv --system-site-packages env;
    source env/bin/activate;
    git clone https://github.com/alexzaporozhets/isells.git
    cd ${SITE_NAME}
    pip install -r requirements.txt
    python manage.py collectstatic --noinput

#нужно поправить
echo "
DEBUG = False
# Set your DSN value
SENTRY_DSN = 'https://9c99e157e5e84051b463437f340a385d:799b27ebb5ef4abf882640532d59d319@app.getsentry.com/4671'
" > local_settings.py
echo "setting databases in \"local_serrings.py\" done"
}

export SITE_NAME=${SITE_NAME}
export -f init_site

su www-data -c "bash -c init_site"

# adding nginx config
echo "
server {
    listen  80;
    server_name ${SITE_DOMAIN1};
    access_log /data/${SITE_NAME}/logs/${SITE_DOMAIN1}_access.log;
    error_log /data/${SITE_NAME}/logs/${SITE_DOMAIN1}_error.log;

    location / {
        uwsgi_pass  unix:///var/run/uwsgi/app/${SITE_DOMAIN1}/socket;
        include     uwsgi_params;
    }

    location /media/  {
        alias /data/${SITE_NAME}/media/;
    }

    location  /static/ {
        alias /data/${SITE_NAME}/static/;
    }
}
" > /etc/nginx/sites-enabled/${SITE_DOMAIN1}

echo "
server {
    listen  80;
    server_name ${SITE_DOMAIN2};
    access_log /data/${SITE_NAME}/logs/${SITE_DOMAIN2}_access.log;
    error_log /data/${SITE_NAME}/logs/${SITE_DOMAIN2}_error.log;

    location / {
        uwsgi_pass  unix:///var/run/uwsgi/app/${SITE_DOMAIN2}/socket;
        include     uwsgi_params;
    }

    location /media/  {
        alias /data/${SITE_NAME}/media/;
    }

    location  /static/ {
        alias /data/${SITE_NAME}/static/;
    }
}
" > /etc/nginx/sites-enabled/${SITE_DOMAIN2}
echo "configuration files for nginx(\"sites-enabled\") was added"

# adding uwsgi config
echo "
[uwsgi]
vhost = true
plugins = python
master = true
enable-threads = true
processes = 1
env = DJANGO_SETTINGS_MODULE=core.eu-settings
wsgi-file = /data/${SITE_NAME}/${SITE_NAME}/core/wsgi.py
virtualenv = /data/${SITE_NAME}/env
chdir = /data/${SITE_NAME}/${SITE_NAME}/
#touch-reload = /data/${SITE_NAME}/${SITE_NAME}/reload
" > /etc/uwsgi/apps-enabled/${SITE_DOMAIN1}.ini

echo "
[uwsgi]
vhost = true
plugins = python
master = true
enable-threads = true
processes = 1
env = DJANGO_SETTINGS_MODULE=core.ru-settings
wsgi-file = /data/${SITE_NAME}/${SITE_NAME}/core/wsgi.py
virtualenv = /data/${SITE_NAME}/env
chdir = /data/${SITE_NAME}/${SITE_NAME}/
#touch-reload = /data/${SITE_NAME}/${SITE_NAME}/reload
" > /etc/uwsgi/apps-enabled/${SITE_DOMAIN2}.ini
echo "both configs for \"uwsgi\" was added"


service uwsgi restart ${SITE_DOMAIN1}
service uwsgi restart ${SITE_DOMAIN2}

service nginx restart

exit 0
