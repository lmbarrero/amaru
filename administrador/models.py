# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    TIPO_CHOICES = (
        ('Estudiante_Colegio', 'Estudiante_Colegio'),
        ('Estudiante_Universitario', 'Estudiante_Universitario'),
        ('Profesor', 'Profesor'),
        ('Administrador', 'Administrador')
    )
    user = models.OneToOneField(User, primary_key='True')
    tipo = models.CharField(max_length=50, default='Estudiante_Colegio', choices=TIPO_CHOICES)
    direccion = models.CharField(max_length=100, blank='True', null='True')
    telefono = models.IntegerField(blank='True', null='True')
    habilitado = models.BooleanField(default='False')

    def __str__(self):              # __unicode__ on Python 2
        if self.user.last_name != "" and self.user.first_name != "":
            rn = self.user.last_name + ', ' + self.user.first_name
        else:
            rn = 'Usuario sin nombre'

        return rn

DEPARTAMENTO_CHOICES = (
    ('La Paz'.encode(encoding='utf-8'), 'La Paz'.encode(encoding='utf-8')),
    ('Oruro'.encode(encoding='utf-8'), 'Oruro'.encode(encoding='utf-8')),
    ('Potosi'.encode(encoding='utf-8'), 'Potosí'.encode(encoding='utf-8')),
    ('Cochabamba'.encode(encoding='utf-8'), 'Cochabamba'.encode(encoding='utf-8')),
    ('Chuquisaca'.encode(encoding='utf-8'), 'Chuquisaca'.encode(encoding='utf-8')),
    ('Tarija'.encode(encoding='utf-8'), 'Tarija'.encode(encoding='utf-8')),
    ('Pando'.encode(encoding='utf-8'), 'Pando'.encode(encoding='utf-8')),
    ('Beni'.encode(encoding='utf-8'), 'Beni'.encode(encoding='utf-8')),
    ('Santa Cruz'.encode(encoding='utf-8'), 'Santa Cruz'.encode(encoding='utf-8')),
)

TIPO_CHOICES = (
    ('Colegio', 'Colegio'),
    ('Universidad', 'Universidad'),
)


class Departamento(models.Model):
    departamento = models.CharField(max_length=30, unique='True', choices=DEPARTAMENTO_CHOICES)

    def primary_key(self):
        return str(self.pk)

    def __str__(self):              # __unicode__ on Python 2
        return self.departamento


class CentroEducativo(models.Model):
    centro_educativo = models.CharField(max_length=50, unique='True')
    tipo = models.CharField(max_length=50, default='Estudiante_Colegio', choices=TIPO_CHOICES)
    departamento = models.ForeignKey(Departamento)
    direccion = models.CharField(max_length=100, blank='True', null='True')
    telefono = models.IntegerField(blank='True', null='True')
    habilitado = models.BooleanField(default='False')

    def __str__(self):              # __unicode__ on Python 2
        return self.centro_educativo