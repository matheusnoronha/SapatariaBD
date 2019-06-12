from django.forms import ModelForm
from .models import Venda
from produto.models import Produto
from django import forms
from estoque.models import Estoque

class NovaVendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(NovaVendaForm,self).__init__(*args,**kwargs)
        self.fields['produtos'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['produtos'].help_text = ""
        self.fields['produtos'].query = Estoque.objects.raw('SELECT * FROM estoque_estoque WHERE estoque_estoque.quantidade > 0')