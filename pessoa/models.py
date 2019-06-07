from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=75)
    cpf = models.IntegerField(max_length=12,primary_key=True,null=False,blank=False)
    rua = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.IntegerField(max_length=8)
