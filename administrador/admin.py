from django.contrib import admin

# Register your models here.

from .models import Colegio


class ColegioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Colegio, ColegioAdmin)