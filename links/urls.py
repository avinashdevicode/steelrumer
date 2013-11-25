from django.conf.urls import patterns, include, url
from links.views import  LinkListView

urlpatterns = patterns('',
    url(r'^home/$', LinkListView.as_view(), name = 'home'),
)