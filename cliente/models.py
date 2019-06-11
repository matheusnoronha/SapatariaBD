from django.db import models
from pessoa.models import Pessoa

# Create your models here.

class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa,on_delete=models.PROTECT)