from msilib.schema import Class
from django.db import models
from django.db.models import ManyToManyField, Model
from chat.models import chat
from juegos.models import Juegos 


# Create your models here.
class partida(models.Model):  
    nombre = models.CharField(max_length=50)
    juegoId = models.ForeignKey(Juegos,related_name="partida",on_delete=models.CASCADE,null=True, blank=True)
    chat_id= models.OneToOneField(chat,on_delete=models.CASCADE,blank=True, null=True)
    usuarioId= models.ManyToManyField("users.User", related_name="user")
 
    def __str__(self):
        return self.nombre