from django.shortcuts import render, redirect
from .form import EstoqueForm
from .models import Estoque
# Create your views here.

def cadastro_estoque(request):
    if(request.method == "POST"):
        form = EstoqueForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('url_lista_estoque')
    else:
        form = EstoqueForm()
        return render(request,'estoque_form.html',{"form":form})

def lista_estoque(request):
    data = {}
    data['estoque'] = Estoque.objects.all()

    return render(request,'lista_estoque.html',data)