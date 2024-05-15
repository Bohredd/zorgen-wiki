from django.db import models
from django.db.models import TextChoices
from django.contrib.auth.models import User
from decouple import config

def upload_file(instance, filename):
    return f"{instance.tipo}/{filename}"

class Tipo(TextChoices):
    documentacao = ('documentacao', "Documentação")
    env_file = ('env_file', "Arquivo de Enviroment")
    tutorial = ('tutorial', "Tutorial")


class Arquivo(models.Model):
    file = models.FileField(
        upload_to=upload_file,
    )

    tipo = models.CharField(
        choices=Tipo.choices,
        max_length=50,
        default='Selecione o tipo de Artigo'
    )


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)

    uploader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    arquivos = models.ManyToManyField(
        'Arquivo',
        related_name='arquivos',
    )
