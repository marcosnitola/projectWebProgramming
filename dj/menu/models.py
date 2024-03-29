from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=64)
    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.PositiveIntegerField()
    popularidad = models.PositiveSmallIntegerField(default=0)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=128)
    img_url = models.CharField(max_length=256)
    def __str__(self):
        return self.nombre
