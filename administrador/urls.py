from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.menu_principal, name='menu_principal'),
    url(r'^menu_principal/$', views.menu_principal, name='menu_principal'),
    url(r'^crear_usuario/$', views.crear_usuario, name='crear_usuario'),
    url(r'^seleccionar_cen_edu/$', views.seleccionar_cen_edu, name='seleccionar_cen_edu'),
    url(r'^registrar_cen_edu/$', views.registrar_cen_edu, name='registrar_cen_edu'),
    url(r'^registrar_cen_edu/#(?P<anchor>[-_\w]+)$', views.registrar_cen_edu, name='registrar_cen_edu'),
    url(r'^departamentos/$', views.lista_departamentos),
    url(r'^departamentos/(?P<pk>[0-9]+)/$', views.detalle_departamento),
    url(r'^centro_educativo/(?P<departamento>[-_\w]+)/(?P<tipo>[-_\w]+)$', views.lista_cen_edu),
]