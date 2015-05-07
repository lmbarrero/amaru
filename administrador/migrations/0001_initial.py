# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colegio', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100, null=b'True', blank=b'True')),
                ('telefono', models.IntegerField(null=b'True', blank=b'True')),
                ('habilitado', models.BooleanField(default=b'False')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=30)),
                ('sigla', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='colegio',
            name='departamento',
            field=models.ForeignKey(to='administrador.Departamento'),
        ),
    ]
