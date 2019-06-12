from django.forms import ModelForm
from .models import Produto
from django import forms

class CadastroProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','tamanho','marca','cor','valor','tipo_produto']


class TipoProdutoForm(ModelForm):
    class Meta:
        model= Produto
        fields = ['tipo_produto']