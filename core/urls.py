from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms.sitemaps import CMSSitemap
from django.http import HttpResponse
from django.conf import settings

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

admin.autodiscover()

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,
            'cmspages': CMSSitemap}

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),

    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^shop/', include('shop.urls')),
    # AJAX
    url(r'^ajax/novaposhta/', include('novaposhta.urls')),

    # CMS
    url(r'^', include('cms.urls')),

)

# if settings.DEBUG:
urlpatterns = patterns('',
   url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
   url(r'', include('django.contrib.staticfiles.urls')),

   url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root':settings.STATIC_ROOT}),
) + urlpatterns