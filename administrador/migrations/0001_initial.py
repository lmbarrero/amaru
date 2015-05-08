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
            name='Colegio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colegio', models.CharField(unique=b'True', max_length=30)),
                ('direccion', models.CharField(max_length=100, null=b'True', blank=b'True')),
                ('telefono', models.IntegerField(null=b'True', blank=b'True')),
                ('habilitado', models.BooleanField(default=b'False')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(unique=b'True', max_length=30, choices=[(b'La Paz', b'La Paz'), (b'Oruro', b'Oruro'), (b'Potos\xc3\xad', b'Potos\xc3\xad'), (b'Cochabamba', b'Cochabamba'), (b'Chuquisaca', b'Chuquisaca'), (b'Tarija', b'Tarija'), (b'Pando', b'Pando'), (b'Beni', b'Beni'), (b'Santa Cruz', b'Santa Cruz')])),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.OneToOneField(primary_key=b'True', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.CharField(default=b'Estudiante', max_length=50, choices=[(b'Estudiante', b'Estudiante'), (b'Profesor', b'Profesor'), (b'Administrador', b'Administrador')])),
                ('direccion', models.CharField(max_length=100, null=b'True', blank=b'True')),
                ('telefono', models.IntegerField(null=b'True', blank=b'True')),
                ('habilitado', models.BooleanField(default=b'False')),
            ],
        ),
        migrations.AddField(
            model_name='colegio',
            name='departamento',
            field=models.ForeignKey(to='administrador.Departamento'),
        ),
    ]
