from django.shortcuts import render
from django.core.cache import cache
from .models import Genero, Categoria, Producto, Talla, Foto
import json
from django.http import HttpResponse

def clothes (request):
    model1 = Genero.objects.all().values()
    model2 = Categoria.objects.all().values()
    model3 = Producto.objects.all().values()
    model4 = Talla.objects.all().values()
    model5 = Foto.objects.all().values()

    data = {
        'generos': list(model1),
        'categorias': list(model2),
        'productos': list(model3),
        'tallas': list(model4),
        'fotosProductos': list(model5)
    }
    
    json_data = json.dumps(data)
    
    cache.set('data_api_cache', json_data, timeout=3600)  # Almacena en caché los datos durante 1 hora

    return HttpResponse(json_data, content_type='application/json')