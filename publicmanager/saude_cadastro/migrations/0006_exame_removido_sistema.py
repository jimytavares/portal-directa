# Generated by Django 4.2.10 on 2025-03-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude_cadastro', '0005_alter_unidadesetor_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='removido_sistema',
            field=models.BooleanField(default=False, verbose_name='Removido do sistema?'),
        ),
    ]
