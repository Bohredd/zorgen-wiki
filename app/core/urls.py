"""
URL configuration for zorgen_wiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . views import ArtigosListView, ArtigosCreateView
from . htmx_views import filtrar_artigos_htmx

htmx_patterns = [
    path("filtrar-query-artigos", filtrar_artigos_htmx, name="filtrarArtigosHtmx"),
]

urlpatterns = [
    path("list", ArtigosListView.as_view(), name='listarArtigos'),
    path("filtrar-query-artigos", filtrar_artigos_htmx, name="filtrarArtigosHtmx"),
    path("criar/", ArtigosCreateView.as_view(), name='createArtigos'),
] + htmx_patterns