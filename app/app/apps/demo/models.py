from django.db import models

class Cadena(models.Model):
    nombre	= models.CharField(max_length = 150)

class Tienda(models.Model):
    cadena		= models.ForeignKey(Cadena) 
    nombre		= models.CharField(max_length = 150)
    direccion	= models.CharField(max_length = 150)

