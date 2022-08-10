from pyexpat import model
from django.db import models

class chat(models.Model): 
    mensaje = models.CharField(max_length=50)

    def __str__(self):  
        return self.mensaje
