from msilib.schema import Class
from django.db import models
from chat.models import chat
from juegos.models import Juegos 
from users.models import User

# Create your models here.
class partida(models.Model):  
    nombre = models.CharField(max_length=50)
    juegoId = models.ForeignKey(Juegos,on_delete=models.CASCADE,null=True, blank=True)
    chat_id= models.OneToOneField(chat,on_delete=models.CASCADE,blank=True, null=True)
    usuario = models.ManyToManyField(User)
 
    def __str__(self):
        return self.nombre