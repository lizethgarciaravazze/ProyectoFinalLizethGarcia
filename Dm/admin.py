from django.contrib import admin
from .models import Canal, CanalUsuario, CanalMensaje

# Register your models here.

class CanalMensajeInline(admin.TabularInline):
    model = CanalMensaje
    extra = 1

class CanalUsuarioInline(admin.TabularInline):
    model = CanalUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalMensajeInline, CanalUsuarioInline]

    class Meta:
        model = Canal

admin.site.register(Canal)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)