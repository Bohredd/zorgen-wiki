from django.http import JsonResponse, HttpResponse
from core.models import Artigo
from django.shortcuts import render
from django.template.loader import render_to_string


def filtrar_artigos_htmx(request):
    categoria = request.GET.get('categoria')
    if categoria:
        artigos = Artigo.objects.filter(
            tipo=categoria,
        )
    else:
        artigos = Artigo.objects.all()

    return render(request, 'core/partials/artigo_partial.html', {'artigos': artigos})
