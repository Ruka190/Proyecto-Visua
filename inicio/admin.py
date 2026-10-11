from django.contrib import admin

from .models import Perfil, Preferencia


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'user', 'ciudad', 'edad')
    search_fields = ('display_name', 'user__username', 'ciudad')


@admin.register(Preferencia)
class PreferenciaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'edad_min', 'edad_max', 'distancia_km')
