from django.conf.urls import patterns, url

urlpatterns = patterns('novaposhta.views',
                       url(r'^$', 'index'),
                       url(r'^city', 'city'),
                       url(r'^office/(?P<city_id>\d+)/$', 'office'),
)
