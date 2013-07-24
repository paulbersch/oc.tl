from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apps.links.urls import urlpatterns as linkurls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linkblog.views.home', name='home'),
    # url(r'^linkblog/', include('linkblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', 'django.views.generic.simple.direct_to_template', { 'template': 'index.html' }),
    url(r'^$', 'links.views.unified_list'),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + linkurls
