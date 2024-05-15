from core.models import Artigo, Tipo
from django.views.generic import ListView

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