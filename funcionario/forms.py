from django import forms
from .models import Funcionario


class CadastroFuncionarioForm(forms.Form):
    CHOICES = (('Option 1', 'Funcionario'), ('Option2', 'Gerente'))
    salario = forms.DecimalField(max_digits=10,decimal_places=2)
    cargo = forms.ChoiceField(choices=CHOICES)