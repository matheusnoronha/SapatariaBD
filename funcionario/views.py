import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .forms import CadastroFuncionarioForm
from django.shortcuts import render, redirect
from .models import Funcionario

# Create your views here.


def listaFuncionario(request):
    data = {}
    data['funcionarios'] = Funcionario.objects.raw('SELECT * FROM funcionario_funcionario')
    return render(request, 'lista_funcionario.html', data)


def cadastroFuncionario(request, pk, pp):
    if request.method == "POST":
        form = CadastroFuncionarioForm(request.POST)
        if form.is_valid():
            salario = form.cleaned_data['salario']
            Funcionario.objects.create(pessoa_id=pp, user_id=pk, salario=salario)

            return redirect('url_lista_funcionario')
    else:
        form = CadastroFuncionarioForm()
        return render(request, 'cadastro_funcionario.html', {'form': form})


def relatorioPDF(request):
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_funcionarios.pdf'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Funcionarios')

    funcionarios = Funcionario.objects.raw('SELECT * FROM funcionario_funcionario')

    str_ = 'Nome: %s | Quantidade de Vendas: %d'

    y = 750

    for funcionario in funcionarios:
        p.drawString(20, y, str_ %(funcionario.pessoa.nome, funcionario.quantidade_vendas))
        y -= 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
