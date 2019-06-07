from django import forms

class CadastroProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    tamanho = forms.IntegerField()
    marca = forms.CharField(max_length=100)
    cor = forms.CharField(max_length=50)
    valor = forms.DecimalField(max_digits=10,decimal_places=2)
    foto = forms.ImageField()

