from django.db import models
from pessoa.models import Pessoa
from django.contrib.auth.models import User
# Create your models here.


class Funcionario (models.Model):
    pessoa = models.OneToOneField(Pessoa,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    quantidade_vendas = models.IntegerField(default=0)
    salario = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

    def __str__(self):
        return self.pessoa.nome
