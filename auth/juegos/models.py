from pyexpat import model
from django.db import models


# Create your models here.
class Juegos(models.Model): 
    nombre = models.CharField(max_length=50)
    def __str__(self): 
        return self.nombre