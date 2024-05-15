from django.contrib import admin
from .models import Artigo, Arquivo

admin.site.register(Arquivo)
admin.site.register(Artigo)