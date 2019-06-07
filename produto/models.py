from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.IntegerField()
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    foto = models.ImageField()