from django.conf.urls import patterns, include, url
#from links.views import LinkListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from links.views import LinkListView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'steelrumers.views.home', name='home'),
    # url(r'^steelrumers/', include('steelrumers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$' li)
    url(r'', include('links.urls'))
)

