from core.models import Artigo, Tipo
from django.views.generic import ListView, CreateView, FormView
from core.forms import ArtigoForms


class ArtigosListView(ListView):
    model = Artigo
    template_name = 'core/artigos_list.html'
    context_object_name = 'artigos'

    def get_queryset(self):
        return Artigo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categorias'] = Tipo.choices

        return context

class ArtigosCreateView(FormView):

    template_name = 'core/artigo_create.html'
    form_class = ArtigoForms
    success_url = '/'
    model = Artigo
