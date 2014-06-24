# -*- coding: utf-8 -*-
import urllib2
import re

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from novaposhta.models import NovaOffice, NovaCity


class Command(BaseCommand):
    def handle(self, *args, **options):

        page = urllib2.urlopen("http://novaposhta.ua/frontend/brunchoffices/ru?alpha=all")
        soup = BeautifulSoup(page, "html.parser")
        department_table = soup.find("table", {"cellpadding": 4})

        NovaOffice.objects.all().delete();
        NovaCity.objects.all().delete();

        count_imported = 0
        city = ''

        for tr in department_table.find_all('tr'):
            td = tr.findChild('td', {'class': 't-stdTblHeader'})
            if td is not None:
                # City (Region) -> matchObj
                matchObj = re.match(r'(.*) \((.*)\)', td.get_text(strip=True), re.M | re.I)

                if matchObj:
                    city = NovaCity(name=matchObj.group(1), region=matchObj.group(2))
                    city.save()
                else:
                    raise Exception("City & Region is no valid!")

            else:
                if tr.findChildren()[1].getText(strip=True):
                    address = tr.findChildren()[1].getText(strip=True)

                    # remove "Отделение N 2 (до 30 кг): "
                    pos = address.find(u'):')

                    # remove Отделение N1:
                    if pos is -1:
                        pos = address.find(u': ')

                    # hack to fix formatting error
                    if pos is -1:
                        pos = address.find(u', ')

                    if pos is -1:
                        print (u'Error, cannot import: "%s"' % address).encode("utf-8")
                    else:
                        address = address[pos + 2:].strip()

                        NovaOffice.objects.bulk_create([
                            NovaOffice(name=tr.findChildren()[0].getText(strip=True),
                                       address=address,
                                       phone=tr.findChildren()[2].getText(strip=True),
                                       city=city
                            )
                        ])
                        count_imported += 1

        print (u'Finished: %d offices' % count_imported).encode("utf-8")