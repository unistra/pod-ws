# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from .views import home

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^webservice/', include('hypnos.apps.webservice.urls', namespace='webservice')),
    url(r'^admin/', include(admin.site.urls)),
)
