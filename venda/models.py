from django.db import models
from produto.models import Produto
from funcionario.models import Funcionario

# Create your models here.

class venda(models.Model):
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    forma_de_pagamento = models.CharField(max_length=50)
    produtos = models.ManyToManyField(Produto)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)