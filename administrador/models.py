from django.db import models

# Create your models here.


class Departamento(models.Model):
    departamento = models.CharField(max_length=30)
    sigla = models.CharField(max_length=5)

    def primary_key(self):
        return str(self.pk)

    def __str__(self):              # __unicode__ on Python 2
        return self.departamento


class Colegio(models.Model):
    colegio = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento)
    direccion = models.CharField(max_length=100, blank='True', null='True')
    telefono = models.IntegerField(blank='True', null='True')
    habilitado = models.BooleanField(default='False')

    def __str__(self):              # __unicode__ on Python 2
        return self.colegio