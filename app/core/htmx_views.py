from django.http import HttpResponse

def filtrar_artigos_htmx(request):
    filtro = request.GET.get('filtro')

    print(filtro)
    return HttpResponse('')