from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserCreateForm

# Create your views here.

@login_required
def home(request):
    return render(request,'index.html')







def cadastroUser(request):
    if(request.method == "POST"):
        form = UserCreateForm(request.POST)
        if(form.is_valid()):
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirmar_senha = form.cleaned_data['confirmar_senha']
            if(senha == confirmar_senha):
                user = User.objects.create_user(username= usuario,
                                                email= email,
                                                password=senha)
                return redirect('url_cadastro_pessoa', pk=user.id)

    else:
        form = UserCreateForm()
        return render(request,'cadastro_usuario.html',{"form":form})



