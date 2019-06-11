from django.db import models

# Create your models here.

class Produto(models.Model):
    CATEGORIAS = (
        ('Tenis','Tenis'),
        ('Mochilas','Mochilas'),
        ('Acessorios','Acessorios'),
    )

    nome = models.CharField(max_length=100)
    tamanho = models.IntegerField()
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    tipo_produto = models.CharField(max_length=20,choices=CATEGORIAS)

    def __str__(self):
        return self.nome +" "+ self.marca +" "+ self.cor