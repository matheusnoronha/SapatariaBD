from django.forms import ModelForm
from .models import Produto

class CadastroProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','tamanho','marca','cor','valor']