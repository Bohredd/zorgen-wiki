from core.models import Artigo
from django.shortcuts import render

def list_artigos(request):

    artigos = Artigo.objects.all()

    return render(request, 'core/artigos_list.html', {"artigos" : artigos})