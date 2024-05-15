# Generated by Django 5.0.6 on 2024-05-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_artigo_tipo_arquivo_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='artigo',
            name='tipo',
            field=models.CharField(choices=[('documentacao', 'Documentação'), ('env_file', 'Arquivo de Enviroment'), ('tutorial', 'Tutorial')], default='Selecione o tipo de Artigo', max_length=50),
        ),
    ]
