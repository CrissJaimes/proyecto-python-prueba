from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre= models.CharField(max_length=20)
    localidad= models.CharField(max_length=50)
    trofeos= models.IntegerField()
    
    
class Estadio(models.Model):
    nombre= models.CharField(max_length=30)
    ubicacion= models.CharField(max_length=60)
    capacidad= models.IntegerField()
    
class Jugador(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    pais= models.CharField(max_length=40)
    posicion= models.CharField(max_length=30)