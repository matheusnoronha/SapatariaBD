from django.db import models

# Create your models here.
from produto.models import Produto


class Estoque(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField()