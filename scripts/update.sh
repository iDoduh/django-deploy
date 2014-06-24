#!/bin/bash

update_site(){
    cd /data/isells
    source env/bin/activate
    cd isells
    # updating the codebase
    git checkout -- . && git fetch && git pull --rebase

    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate
}
export -f update_site

su www-data -c "bash -c update_site"

service uwsgi restart isells.eu
service uwsgi restart isells.ru

exit 0

# python manage.py celery worker --loglevel=info
