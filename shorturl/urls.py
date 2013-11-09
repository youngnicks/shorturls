from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Site URLs
urlpatterns = patterns(
    '',
    url(r'', include('links.urls')),
)

# Admin URLs
urlpatterns += patterns(
    url(r'^admin/', include(admin.site.urls)),
)
