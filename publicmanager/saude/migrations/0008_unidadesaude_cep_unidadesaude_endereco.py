# Generated by Django 4.2.10 on 2025-01-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0007_unidadesaude_cnes'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidadesaude',
            name='cep',
            field=models.CharField(blank=True, max_length=14, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='unidadesaude',
            name='endereco',
            field=models.CharField(default=1, help_text='Nome da rua, travessa ou avenida', max_length=255, verbose_name='Endereço'),
            preserve_default=False,
        ),
    ]
