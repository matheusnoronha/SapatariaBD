from django.shortcuts import render,redirect
from .forms import NovaVendaForm
from .models import Venda

# Create your views here.

def nova_venda(request):
    if(request.method == "POST"):
        form = NovaVendaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('url_lista_vendas')
    else:
        form = NovaVendaForm()
        return render(request,'nova_venda.html',{"form":form})


def listar_vendas(request):
    data = {}
    data['vendas'] = Venda.objects.all()

    return render(request,'lista_venda.html', data)