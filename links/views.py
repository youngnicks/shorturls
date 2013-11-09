# Django includes
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

# App includes
from links.forms import LinkForm
from links.models import Link


class CreateLinkView(CreateView):
    """
    A view that creates a Link.
    """
    template_name = 'create_link.html'
    form_class = LinkForm
    success_url = reverse_lazy('home')


class DeleteLinkView(DeleteView):
    """
    A view that deletes a link.
    """
    model = Link
    success_url = reverse_lazy('home')


class RedirectLinkView(RedirectView):
    """
    A view to lookup a Link and redirect to its URL.
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, slug=kwargs['slug'])
        link.update_counter()
        self.url = link.url
        return super(RedirectLinkView, self).get_redirect_url(*args, **kwargs)
