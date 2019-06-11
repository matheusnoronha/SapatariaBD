from django.urls import path
from .views import cadastroFuncionario
from .views import listaFuncionario


urlpatterns = [
    path('',listaFuncionario, name = 'url_lista_funcionario'),
    path('<int:pk>/<int:pp>/cadastro/', cadastroFuncionario,name = 'url_cadastro_funcionario'),

]
