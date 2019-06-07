from django.db import models
from produto.models import Produto

# Create your models here.

class venda(models.Model):
    valor = models.DecimalField(decimal_places=2)
    forma_de_pagamento = models.CharField(max_length=50)
    produtos = models.ManyToManyField(Produto)
    funcionario = models.ForeignKey(Funcionario)