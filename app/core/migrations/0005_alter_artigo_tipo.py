# Generated by Django 5.0.6 on 2024-05-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_artigo_conteudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='tipo',
            field=models.CharField(choices=[('documentacao', 'Documentação'), ('env_file', 'Arquivo de Enviroment'), ('tutorial', 'Tutorial')], max_length=50),
        ),
    ]
