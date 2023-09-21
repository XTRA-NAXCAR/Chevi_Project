from django.db import models
from ropa.models import Producto, Categoria, Genero

OPTIONS = (
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
    (3, '3'),
    (3.5, '3.5'),
    (4, '4'),
    (4.5, '4.5'),
    (5, '5'),
)
OPTIONS_2 = (
    ('Hombre', 'Hombre'),
    ('Mujer', 'Mujer'),
)

# Create your models here.
class Multimedia_Principal(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.titulo

class Instagram_post(models.Model):
    imagen = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.link

class Novedade(models.Model):
    titulo_en_admin = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_en_admin

class Seccion(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    


class Productos(models.Model):
    Pertenece_a = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto

class Categoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Marcas(models.Model):
    imagen = models.ImageField(upload_to='images/')
    




class Contacto(models.Model):
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)

    def __str__(self):
        return self.telefono


