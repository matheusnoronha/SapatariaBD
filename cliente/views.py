from django.shortcuts import render,redirect
from cliente.models import Cliente
from pessoa.forms import CadastroPessoaForm
# Create your views here.

def cadastro_clientes(request):
    if(request.method == "POST"):
        form = CadastroPessoaForm(request.POST)
        if(form.is_valid()):
            pessoa = form.save()
            cliente = Cliente.objects.create(pessoa_id=pessoa.cpf)
            cliente.save()
            return redirect('url_lista_clientes')
    else:
        form =CadastroPessoaForm()
        return render(request,'cadastro_pessoa.html',{'form':form})

def lista_clientes(request):
    data = {}
    data['clientes'] = Cliente.objects.all()
    return render(request, 'lista_clientes.html', data)