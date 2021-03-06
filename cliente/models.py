from django.db import models
from pessoa.models import Pessoa


class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome
