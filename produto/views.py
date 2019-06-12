from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import CadastroProdutoForm, TipoProdutoForm
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

def listarProdutoTipo(request):
    if (request.method == "POST"):
        form = TipoProdutoForm(request.POST)
        if (form.is_valid()):
            tipo = form.cleaned_data['tipo_produto']
            data= {}
            data['produtos'] = Produto.objects.raw('SELECT * FROM produto_produto WHERE tipo_produto = %s',[tipo])
            return render(request,'lista_produto.html',data)
    else:
        form = TipoProdutoForm()
        return render(request, 'tipo_produto_form.html', {"form": form})