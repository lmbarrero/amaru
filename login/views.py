# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

# For user authentication using Django system
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    """
        Vista predeterminada para iniciar sesión en el servidor.
        Si no existen usuarios, se pide la creación de un administrador,
        caso contrario, se muestra un formulario de inicio de sesión.
        Este módulo utiliza el sistema de autenticación de Django
    :param request:
    :return:
    """

    user_id = verificar_admin(request)

    if user_id >= 1:
        request.session['tipo_usuario'] = 'Administrador'
        return redirect('administrador:menu_principal', permanent=True)
    elif user_id == -2:
        request.session['tipo_usuario'] = 'Profesor'
        return redirect('usuario:menu_principal', permanent=True)
    elif user_id == -3:
        request.session['tipo_usuario'] = 'Estudiante'
        return redirect('usuario:menu_principal', permanent=True)
    else:
        return render(request, 'login/login.html')


def validate(request):
    """
        En caso de existir usuarios registrados, se inicia el proceso de
        auntenticación y se mostrará la página correspondiente, para un
        usuario Normal o para un usuario Administrador.
    :param request:
    :return:
    """

    username = request.POST.get('username', "")
    password = request.POST.get('password', "")

    if 'login' in request.POST:
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                init_session(request, user)

    if 'registrarse' in request.POST:
        context = {'debug_info': 'Administrador Menu Principal: Crear Usuario',
                   'tipo_usuario': 'NUEVO USUARIO'}

        return render(request, 'administrador/crear_usuario.html', context)

    return redirect('login:index')


def init_session(request, user):
    """
        Permite finalizar la sesión, eliminando del servidor
        todo rastro de la sesión
    :param request:
    :return:
    """

    login(request, user)
    request.session['user_id'] = user.id


def end_session(request):
    """
        Permite finalizar la sesión, eliminando del servidor
        todo rastro de la sesión
    :param request:
    :return:
    """

    logout(request)

    return redirect('login:index', permanent=True)


def verificar_admin(request):
    """
        Verifica si un usuario ha iniciado sesión y ha sido autenticado como administrador
    :param request:
    :return:
        -1 : El usuario no está autenticado.
        -2 : El usuario está autenticado, pero no es un administrador
    """

    try:
        user_id = request.session['user_id']  # request.user.is_authenticated()
        user = User.objects.get(pk=user_id)
    except KeyError:
        user_id = 0
        user = None

    if user is None:
        return -1
    elif user_id != 0 and user.is_active and user.is_staff and user.is_superuser:
        return user_id
    else:
        return -2