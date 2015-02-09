# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='redeSocial',
            field=models.TextField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default=b'', max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dataPagamento',
            field=models.IntegerField(default=5, max_length=31),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]
