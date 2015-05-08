from django.contrib import admin

# Register your models here.

from .models import Colegio
from .models import Departamento
from .models import Usuario


class MyUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario, MyUserAdmin)


class ColegioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Colegio, ColegioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)