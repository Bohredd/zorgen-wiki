from core.models import Artigo
from django.shortcuts import render
from django.views.generic import ListView

class ArtigosListView(ListView):
    model = Artigo
    template_name = 'core/artigos_list.html'
    context_object_name = 'artigos'

    def get_queryset(self):
        return Artigo.objects.all()