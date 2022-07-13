from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Bicicleta(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    rodado = models.IntegerField()
    precio = models.DecimalField(max_digits=8,decimal_places=2)

class Insumo(models.Model):
    marca = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=8,decimal_places=2)
