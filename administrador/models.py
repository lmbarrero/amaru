# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    TIPO_CHOICES = (
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
        ('Administrador', 'Administrador')
    )
    user = models.OneToOneField(User, primary_key='True')
    tipo = models.CharField(max_length=50, default='Estudiante', choices=TIPO_CHOICES)
    direccion = models.CharField(max_length=100, blank='True', null='True')
    telefono = models.IntegerField(blank='True', null='True')
    habilitado = models.BooleanField(default='False')

    def __str__(self):              # __unicode__ on Python 2
        if self.user.last_name != "" and self.user.first_name != "":
            rn = self.user.last_name + ', ' + self.user.first_name
        else:
            rn = 'Usuario sin nombre'
            
        return rn


class Departamento(models.Model):
    DEPARTAMENTO_CHOICES = (
        ('La Paz', 'La Paz'),
        ('Oruro', 'Oruro'),
        ('Potosí', 'Potosí'),
        ('Cochabamba', 'Cochabamba'),
        ('Chuquisaca', 'Chuquisaca'),
        ('Tarija', 'Tarija'),
        ('Pando', 'Pando'),
        ('Beni', 'Beni'),
        ('Santa Cruz', 'Santa Cruz')
    )

    departamento = models.CharField(max_length=30, unique='True', choices=DEPARTAMENTO_CHOICES)

    def primary_key(self):
        return str(self.pk)

    def __str__(self):              # __unicode__ on Python 2
        return self.departamento


class Colegio(models.Model):
    colegio = models.CharField(max_length=30, unique='True')
    departamento = models.ForeignKey(Departamento)
    direccion = models.CharField(max_length=100, blank='True', null='True')
    telefono = models.IntegerField(blank='True', null='True')
    habilitado = models.BooleanField(default='False')

    def __str__(self):              # __unicode__ on Python 2
        return self.colegio