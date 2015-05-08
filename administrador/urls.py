from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^menu_principal/$', views.menu_principal, name='menu_principal'),
    url(r'^crear_usuario/$', views.crear_usuario, name='crear_usuario'),
    url(r'^registrar_colegio/$', views.registrar_colegio, name='registrar_colegio'),
    url(r'^registrar_colegio/#(?P<anchor>[-_\w]+)$', views.registrar_colegio, name='registrar_colegio'),
]