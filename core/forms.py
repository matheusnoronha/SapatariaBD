from django import forms



class UserCreateForm(forms.Form):
    usuario = forms.CharField(max_length=75)
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput())
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())
