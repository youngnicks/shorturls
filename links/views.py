from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from links.forms import LinkForm


class CreateLinkView(CreateView):
    """
    A view that creates a Link.
    """
    template_name = 'create_link.html'
    form_class = LinkForm
    success_url = reverse_lazy('create_link')
