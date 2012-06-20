from django.conf.urls import patterns, include, url
from views import unified_list, detail, tag_list

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', 'django.views.generic.simple.direct_to_template', { 'template': 'index.html' }),
    url(r'^c/$', unified_list),
    url(r'^t/(?P<slug>.*)/$', tag_list),
    url(r'^[lip]/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.*)/$', detail),
)
