from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser
from partidas.models import partida

from chat.models import chat 
# Create your models here.

class User(AbstractUser):
    username = models.CharField('Nome de Usuário', max_length=30, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    chatid  = models.ForeignKey(chat,on_delete=models.CASCADE,null=True, blank=True)
    partidaId = models.ForeignKey(partida,on_delete=models.CASCADE,null=True, blank=True)
    
    
    def __str__(self): 
        return self.name
    

    EMAIL_FIELD = 'email'  # ====> Acrescente essa linha
    USERNAME_FIELD = 'username'
    REQUERID_FIELDS = ['email']