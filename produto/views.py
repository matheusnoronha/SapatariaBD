from django.shortcuts import render, redirect
import request
from .models import Produto
from .form import CadastroProdutoForm
# Create your views here.

def cadastroProduto(request):
    if(request.method == "POST"):
        form = CadastroProdutoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('url_lista_produto')

    else:
        form = CadastroProdutoForm()
        return render(request,"produto/cadastro_produto.html",{'form':form})

def listarProduto(request):
    data = {}
    data['produtos'] = Produto.objects.all()

    return render(request,"produto/lista_produto.html",data)