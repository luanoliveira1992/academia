# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparelho',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoriaAparelho',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
                ('riscoSaude', models.BooleanField(default=False)),
                ('doencasEvitar', models.TextField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categoriaaparelho',
            name='exercicio',
            field=models.ForeignKey(to='aparelhos.Exercicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aparelho',
            name='categorias',
            field=models.ForeignKey(to='aparelhos.CategoriaAparelho'),
            preserve_default=True,
        ),
    ]
