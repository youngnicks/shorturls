from django.conf.urls import patterns, url
from links.views import CreateLinkView, DeleteLinkView, RedirectLinkView

urlpatterns = patterns(
    '',
    url(r'^shorten/$', CreateLinkView.as_view(), name="create_link"),

    url(r'(?P<slug>\w{6})/delete/$', DeleteLinkView.as_view(),
        name="delete_link"),

    url(r'(?P<slug>\w{6})/$', RedirectLinkView.as_view(),
        name="redirect_link"),
)
