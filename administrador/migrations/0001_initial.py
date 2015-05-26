# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroEducativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centro_educativo', models.CharField(unique='True', max_length=50)),
                ('tipo', models.CharField(default='Estudiante_Colegio', max_length=50, choices=[('Colegio', 'Colegio'), ('Universidad', 'Universidad')])),
                ('direccion', models.CharField(max_length=100, null='True', blank='True')),
                ('telefono', models.IntegerField(null='True', blank='True')),
                ('habilitado', models.BooleanField(default='False')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(unique='True', max_length=30, choices=[(b'La Paz', b'La Paz'), (b'Oruro', b'Oruro'), (b'Potosi', b'Potos\xc3\xad'), (b'Cochabamba', b'Cochabamba'), (b'Chuquisaca', b'Chuquisaca'), (b'Tarija', b'Tarija'), (b'Pando', b'Pando'), (b'Beni', b'Beni'), (b'Santa Cruz', b'Santa Cruz')])),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.OneToOneField(primary_key='True', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.CharField(default='Estudiante_Colegio', max_length=50, choices=[('Estudiante_Colegio', 'Estudiante_Colegio'), ('Estudiante_Universitario', 'Estudiante_Universitario'), ('Profesor', 'Profesor'), ('Administrador', 'Administrador')])),
                ('direccion', models.CharField(max_length=100, null='True', blank='True')),
                ('telefono', models.IntegerField(null='True', blank='True')),
                ('habilitado', models.BooleanField(default='False')),
            ],
        ),
        migrations.AddField(
            model_name='centroeducativo',
            name='departamento',
            field=models.ForeignKey(to='administrador.Departamento'),
        ),
    ]
