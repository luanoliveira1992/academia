# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.TextField(max_length=50)),
                ('cadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=10)),
                ('tipo', models.ForeignKey(to='usuarios.TipoUsuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
