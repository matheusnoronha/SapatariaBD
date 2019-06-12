from django.shortcuts import render,redirect
from .forms import NovaVendaForm, BuscarVendaForm
from .models import Venda

# Create your views here.


def nova_venda(request):
    if request.method == "POST":
        form = NovaVendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_lista_vendas')
    else:
        form = NovaVendaForm()
        return render(request, 'nova_venda.html', {"form": form})


def listar_vendas(request):
    data = {}
    data['vendas'] = Venda.objects.all()

    return render(request, 'lista_venda.html', data)


def listar_vendas_por_data(request):
    data = {}
    if request.method == 'POST':
        form = BuscarVendaForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            data['vendas'] = Venda.objects.raw('SELECT * FROM venda_venda WHERE data = %s', [date])
            return render(request, 'lista_venda.html', data)
    else:
        form = BuscarVendaForm()
        return render(request, 'nova_venda.html', {'form': form})
