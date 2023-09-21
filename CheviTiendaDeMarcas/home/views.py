from django.shortcuts import render
from django.core.cache import cache
from .models import Instagram_post, Novedade, Seccion, Productos, Categoria, Contacto, Multimedia_Principal, Marcas
import json
from django.http import HttpResponse
# Create your views here.
def home (request):
    model1 = Instagram_post.objects.all().values()
    model2 = Novedade.objects.all().values()
    model3 = Seccion.objects.all().values()
    model4 = Productos.objects.all().values()
    model5 = Categoria.objects.all().values()
    model6 = Contacto.objects.all().values()
    model9 = Multimedia_Principal.objects.all().values()
    model10 = Marcas.objects.all().values()

    data = {
        'Instagram_post': list(model1),
        'Novedade': list(model2),
        'Seccion': list(model3),
        'Productos': list(model4),
        'Categoria': list(model5),
        'Contacto': list(model6),
        'Multimedia': list(model9),
        'Marcas': list(model10),
    }

    json_data = json.dumps(data)
    
    cache.set('data_api_cache', json_data, timeout=3600)  # Almacena en caché los datos durante 1 hora

    return HttpResponse(json_data, content_type='application/json')