# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Departamento, CentroEducativo
from administrador.serializers import DepartamentoSerializer, CenEduSerializer

# Create your views here.


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def lista_cen_edu(request, departamento, tipo):
    """
        Muestra una lista de todos los centros educativos de un determinado tipo en un departamento
    """
    try:
        cen_edu = CentroEducativo.objects.filter(departamento=departamento, tipo=tipo).order_by('pk')
    except CentroEducativo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CenEduSerializer(cen_edu, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CenEduSerializer(cen_edu, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cen_edu.delete()
        return HttpResponse(status=204)



@csrf_exempt
def lista_departamentos(request):
    """
        Muestra una lista de todos los departamentos, o permite crear uno nuevo
    """
    if request.method == 'GET':
        departamentos = Departamento.objects.order_by('pk')
        serializer = DepartamentoSerializer(departamentos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def detalle_departamento(request, pk):
    """
        Obtener o modificar un registro
    """
    try:
        departamento = Departamento.objects.get(pk=pk)
    except Departamento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DepartamentoSerializer(departamento)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartamentoSerializer(departamento, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        departamento.delete()
        return HttpResponse(status=204)


def menu_principal(request):
    """
        Muestra en pantalla el menú principal del usuario administrador
    :param request:
    :return:
    """

    tipo_usuario = request.session.get('tipo_usuario', "")

    if tipo_usuario == 'Administrador':
        context = {'debug_info': 'Administrador Menu Principal: Menu Principal Tipo_Usuario: ' + tipo_usuario}
        return render(request, 'administrador/menu_principal.html', context)
    else:
        return redirect('login:index')


def crear_usuario(request):
    """
        Permite crear un usuario nuevo en el sistema
    :param request:
    :return:
    """

    if 'cancel' in request.POST:
        return redirect("login:index")

    tipo_usuario = request.session.get('tipo_usuario', "")

    context = {'debug_info': 'Administrador Menu Principal: Crear Usuario',
               'tipo_usuario': tipo_usuario}

    return render(request, 'administrador/crear_usuario.html', context)


def registrar_cen_edu(request):
    """
        Permite registrar un colegio en el sistema
    :param request:
    :return:
    """

    if 'cancel' in request.POST:
        return redirect("login:index")

    tipo_usuario = request.session.get('tipo_usuario', "")

    if tipo_usuario != 'Administrador' and \
                    tipo_usuario != 'Profesor' and \
                    tipo_usuario != 'Estudiante_Colegio' and \
                    tipo_usuario != 'Estudiante_Universitario':
        tipo_usuario = 'Nuevo_Usuario'

    context = {'debug_info': 'Administrador Menu Principal: Registrar Colegio Tipo_Usuario: ' + tipo_usuario,
               'tipo_usuario': tipo_usuario}

    return render(request, 'administrador/registrar_cen_edu.html', context)


def seleccionar_cen_edu(request):
    """

    :param request:
    :return:
    """
    if 'cancel' in request.POST:
        return redirect("login:index")

    context = {'debug_info': 'Administrador Menu Principal: Crear Usuario',
               'tipo_usuario': 'NUEVO USUARIO'}
    return render(request, 'administrador/seleccionar_cen_edu.html', context)
