# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from crew.models import Crew


class CrewDetailView(DetailView):

    model = Crew

    def get_context_data(self, **kwargs):
        context = super(CrewDetailView, self).get_context_data(**kwargs)
        #context['breadcrumbs'].append((self.object.get_absolute_url(), self.object.name), )
        #context['actions'] = self.object.action_set.select_related()

        return context
