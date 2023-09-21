from django.contrib import admin
from .models import Instagram_post, Novedade, Seccion, Productos, Categoria, Contacto, Multimedia_Principal, Marcas

# Register your models here.
@admin.register(Instagram_post)
class Instagram_postAdmin(admin.ModelAdmin):
    pass

@admin.register(Novedade)
class NovedadeAdmin(admin.ModelAdmin):
    pass

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    pass

@admin.register(Productos)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass

@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    pass

@admin.register(Multimedia_Principal)
class MultimediaAdmin(admin.ModelAdmin):
    pass
