from django.db import models
from pessoa.models import Pessoa
# Create your models here.

class Funcionario (models.Model):
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    quantidade_vendas = models.DecimalField(decimal_places=2,max_digits=10)
    salario = models.DecimalField(decimal_places=2,max_digits=10)
