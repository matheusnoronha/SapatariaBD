from django.urls import path
from .views import cadastrarPessoa



urlpatterns = [
    path('<int:pk>/cadastro/',cadastrarPessoa,name = 'url_cadastro_pessoa')

]
