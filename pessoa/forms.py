from django.forms import ModelForm
from .models import Pessoa

class CadastroPessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'