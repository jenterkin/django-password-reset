from django.conf.urls import patterns, include, url
from password_reset.views import (
        request_link,
        reset,
    )

urlpatterns = patterns('',
    url(r'^request_link/$', request_link),
    url(r'^reset/$', reset),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
