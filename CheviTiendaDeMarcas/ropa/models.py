from django.db import models

# Create your models here.
class Genero(models.Model):
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

class Categoria(models.Model):
    categoria_nombre_en_administrador = models.CharField(max_length=100)
    categoria_nombre_en_pantalla = models.CharField(max_length=100)
    genero_al_que_pertenece = models.ForeignKey(Genero, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.categoria_nombre_en_administrador

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    especificacion = models.TextField()
    tallas = models.ManyToManyField('Talla')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    on_sale = models.BooleanField(default=False)
    precio = models.CharField(max_length=100)
    Foto_Principal = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.titulo

class Foto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='images/')
    
class Talla(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
