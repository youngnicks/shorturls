from django.conf.urls import patterns, url
from links.views import CreateLinkView

urlpatterns = patterns(
    '',
    url(r'^shorten/$', CreateLinkView.as_view(), name="create_link"),
)
