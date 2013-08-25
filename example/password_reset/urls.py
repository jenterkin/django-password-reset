from django.conf.urls import patterns, include, url
from password_reset.views import (
        password_reset,
    )

urlpatterns = patterns('',
    url(r'^password_reset/$', password_reset),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
