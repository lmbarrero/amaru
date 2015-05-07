# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

# For user authentication using Django system
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def menu_principal(request):
    """
        Muestra en pantalla el menú principal del usuario administrador
    :param request:
    :return:
    """

    context = {'Debug': "Administrador Menu Principal: Menu Principal"}

    return render(request, 'administrador/menu_principal.html', context)


def crear_usuario(request):
    """
        Muestra en pantalla el menú principal del usuario administrador
    :param request:
    :return:
    """

    context = {'Debug': "Administrador Menu Principal: Menu Principal"}

    return render(request, 'administrador/menu_principal.html', context)


def registrar_departamento(request):
    """
        Muestra en pantalla el menú principal del usuario administrador
    :param request:
    :return:
    """

    context = {'Debug': "Administrador Menu Principal: Menu Principal"}

    return render(request, 'administrador/menu_principal.html', context)


def registrar_colegio(request):
    """
        Muestra en pantalla el menú principal del usuario administrador
    :param request:
    :return:
    """

    context = {'Debug': "Administrador Menu Principal: Menu Principal"}

    return render(request, 'administrador/menu_principal.html', context)

