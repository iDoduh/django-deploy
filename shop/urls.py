from django.conf.urls import patterns, url

urlpatterns = patterns('shop.views',
    url(r'^$', 'index'),
    url(r'^create_success/(?P<site_id>\d+)/$', 'create_success'),
    url(r'^create', 'create'),
    url(r'^login', 'login'),
    url(r'^wait/(?P<site_id>\d+)/$', 'wait'),
    url(r'^delete/(?P<site_id>\d+)/$', 'delete'),
    url(r'^check_status/(?P<site_id>\d+)/$', 'check_status'),
    url(r'^check_domain/(?P<domain>[\w.-0-9]+)/$', 'check_domain'),
)