from .models import Funcionario
from .forms import CadastroFuncionarioForm
from django.shortcuts import render,redirect
from .models import Funcionario

# Create your views here.

def listaFuncionario(request):
    data = {}
    data['funcionarios'] = Funcionario.objects.all()
    return render(request, 'lista_funcionario.html', data)

def cadastroFuncionario(request,pk,pp):
    if (request.method == "POST"):
        form = CadastroFuncionarioForm(request.POST)
        if (form.is_valid()):
            salario = form.cleaned_data['salario']
            Funcionario.objects.create(pessoa_id=pp,user_id=pk,salario = salario)

            return redirect('url_lista_funcionario')
    else:
        form = CadastroFuncionarioForm()
        return render(request,'cadastro_funcionario.html',{'form':form})