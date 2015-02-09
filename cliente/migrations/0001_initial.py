# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=20)),
                ('dataPagamento', models.IntegerField(max_length=31)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClienteSaude',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('altura', models.DecimalField(max_digits=5, decimal_places=2)),
                ('diametroBraco', models.DecimalField(max_digits=5, decimal_places=2)),
                ('diametroCintura', models.DecimalField(max_digits=5, decimal_places=2)),
                ('diametroPerna', models.DecimalField(max_digits=5, decimal_places=2)),
                ('horasMalharDia', models.IntegerField(max_length=24)),
                ('diasMalharSemana', models.IntegerField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnderecoUsuario',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(to='cliente.EnderecoUsuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='saude',
            field=models.ForeignKey(to='cliente.ClienteSaude'),
            preserve_default=True,
        ),
    ]
