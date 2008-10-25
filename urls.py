from django.conf.urls.defaults import *
from djegg.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djegg/', include('djegg.foo.urls')),

    (r'^time/$', current_datetime),
    (r'^plot/$', plot),
    (r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': ''}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
