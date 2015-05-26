# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers
from .models import Departamento, DEPARTAMENTO_CHOICES, CentroEducativo, TIPO_CHOICES


class DepartamentoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    departamento = serializers.ChoiceField(choices=DEPARTAMENTO_CHOICES)

    def create(self, validated_data):
        return Departamento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.departamento = validated_data.get('departamento', instance.departamento)
        instance.save()
        return instance


class CenEduSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    centro_educativo = serializers.CharField(max_length=50)
    tipo = serializers.ChoiceField(default='Estudiante_Colegio', choices=TIPO_CHOICES)
    departamento = DepartamentoSerializer(Departamento)
    direccion = serializers.CharField(max_length=100)
    telefono = serializers.IntegerField()
    habilitado = serializers.BooleanField(default='False')

    def create(self, validated_data):
        return CentroEducativo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.centro_educativo = validated_data('centro_educativo', instance.cntro_educativo)
        instance.tipo = validated_data('tipo', instance.tipo)
        instance.departamento = validated_data('departamento', instance.departamento)
        instance.direccion = validated_data('direccion', instance.direccion)
        instance.telefono = validated_data('telefono', instance.telefono)
        instance.habilitado = validated_data('habilitado', instance.habilitado)

        instance.cen_edu = validated_data.get('cen_edu', instance.cen_edu)
        instance.save()
        return instance