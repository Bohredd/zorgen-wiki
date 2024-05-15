# Generated by Django 5.0.6 on 2024-05-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='arquivo',
            name='tipo',
            field=models.CharField(choices=[('documentacao', 'Documentação'), ('env_file', 'Arquivo de Enviroment'), ('tutorial', 'Tutorial')], default='Selecione o tipo de Artigo', max_length=50),
        ),
    ]