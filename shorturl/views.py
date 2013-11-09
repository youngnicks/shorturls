# Django includes
from django.views.generic.base import TemplateView
from django.contrib.sites.models import get_current_site

# App includes
from links.forms import LinkForm
from links.models import Link


class HomePageView(TemplateView):
    """
    View to display the home page.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['form'] = LinkForm
        context['links'] = Link.objects.all()
        context['current_site'] = get_current_site(self.request)
        return context
