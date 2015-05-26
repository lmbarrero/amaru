from django.contrib import admin

# Register your models here.

from .models import CentroEducativo
from .models import Departamento
from .models import Usuario


class MyUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario, MyUserAdmin)


class CentroEducativoAdmin(admin.ModelAdmin):
    pass

admin.site.register(CentroEducativo, CentroEducativoAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)