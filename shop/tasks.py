import os;

from celery import task
from django.conf import settings


@task()
def addWebsite(site):
    os.system(settings.PROJECT_DIR + '/../scripts/create-site.sh shop_' + str(site.pk) + ' ' + site.domain)
    site.created = True
    site.save()
    delWebsite()
    return site


@task()
def delWebsite(site):
    os.system(settings.PROJECT_DIR + '/../scripts/delete-site.sh shop_' + str(site.pk))
    site.delete
    return site
