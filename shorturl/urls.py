from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# App includes
from shorturl.views import HomePageView

# Site URLs
urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'', include('links.urls')),
)

# Admin URLs
urlpatterns += patterns(
    url(r'^admin/', include(admin.site.urls)),
)
