from django.shortcuts import render,redirect

from pessoa.models import Pessoa
from .forms import CadastroPessoaForm
# Create your views here.

def cadastrarPessoa(request,pk):
    if(request.method == "POST"):
        form = CadastroPessoaForm(request.POST)
        if(form.is_valid()):
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            rua = form.cleaned_data['rua']
            estado = form.cleaned_data['estado']
            cidade = form.cleaned_data['cidade']
            cep = form.cleaned_data['cep']

            pessoa = Pessoa.objects.create(nome= nome,cpf=cpf,rua = rua, estado = estado,
                                           cidade = cidade, cep = cep
                                           )
            pessoa.save()
            return redirect('url_cadastro_funcionario',pk=pk, pp=pessoa.cpf)
    else:
        form = CadastroPessoaForm()
        return render(request,'cadastro_pessoa.html',{"form":form})