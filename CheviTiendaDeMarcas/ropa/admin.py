from django.contrib import admin
from .models import Genero, Categoria, Producto, Talla, Foto

# Register your models here.
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriasAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    pass

@admin.register(Talla)
class TallasAdmin(admin.ModelAdmin):
    pass

@admin.register(Foto)
class FotosAdmin(admin.ModelAdmin):
    pass
