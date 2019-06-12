from django.db import models

# Create your models here.
from funcionario.models import Funcionario


class Gerente (models.Model):
    funcionario = models.OneToOneField(Funcionario,on_delete=models.PROTECT)