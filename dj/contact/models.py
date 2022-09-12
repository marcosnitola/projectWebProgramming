from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    nombre_cliente = models.CharField(max_length=128)
    correo_cliente = models.EmailField(max_length=512)
    telefono_cliente = models.PositiveBigIntegerField()
    mensaje_cliente = models.CharField(max_length=1024)
    def __str__(self):
        return self.correo_cliente
