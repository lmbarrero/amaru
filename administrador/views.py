# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

# Create your views here.


def menu_principal(request):
    """
        Muestra en pantalla el menú principal del usuario administrador
    :param request:
    :return:
    """

    tipo_usuario = request.session.get('tipo_usuario', "")

    if tipo_usuario == 'Administrador':
        context = {'debug_info': 'Administrador Menu Principal: Menu Principal'}
        return render(request, 'administrador/menu_principal.html', context)
    else:
        return redirect('login:index')


def crear_usuario(request):
    """
        Permite crear un usuario nuevo en el sistema
    :param request:
    :return:
    """

    tipo_usuario = request.session.get('tipo_usuario', "")

    if 'cancel' in request.POST:
        return redirect("login:index")

    context = {'debug_info': 'Administrador Menu Principal: Crear Usuario',
               'tipo_usuario': tipo_usuario}

    return render(request, 'administrador/crear_usuario.html', context)


def registrar_colegio(request):
    """
        Permite registrar un colegio en el sistema
    :param request:
    :return:
    """

    tipo_usuario = request.session.get('tipo_usuario', "")

    if tipo_usuario != 'Administrador' or \
                    tipo_usuario != 'Profesor' or \
                    tipo_usuario != 'Estudiante':

        return redirect("login:index")

    context = {'debug_info': 'Administrador Menu Principal: Registrar Colegio',
               'tipo_usuario': tipo_usuario}

    return render(request, 'administrador/registrar_colegio.html', context)