from django.urls import path
from .views import cadastroProduto
from .views import listarProduto


urlpatterns = [
    path('', listarProduto,name = 'url_lista_produto'),
    path('cadastro/',cadastroProduto,name = 'url_cadastro_produto')

]
