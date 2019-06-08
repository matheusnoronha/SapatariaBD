from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import CadastroProdutoForm
from .models import Produto

# Create your views here.

def cadastroProduto(request):
    if(request.method == "POST"):
        form = CadastroProdutoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('url_lista_produto')
    else:
        form = CadastroProdutoForm()
        return render(request,'produto_form.html',{"form":form})

def listarProduto(request):
    data = {}
    data['produtos'] = Produto.objects.all()

    return render(request,'lista_produto.html', data)