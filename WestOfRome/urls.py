from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WestOfRome.views.blog', name='blog'),
    # url(r'^WestOfRome/', include('WestOfRome.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Book recommends : 
    # url(r'^admin/', include('django.contrib.admin.urls')),

    # http://www.djangobook.com/en/2.0/chapter06.html
    url(r'^admin/', include(admin.site.urls)),
)
