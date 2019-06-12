from django.urls import path
from .views import cadastroProduto
from .views import listarProduto, listarProdutoTipo


urlpatterns = [
    path('', listarProduto,name = 'url_lista_produto'),
    path('cadastro/',cadastroProduto,name = 'url_cadastro_produto'),
    path('tipo/',listarProdutoTipo, name='url_lista_produto_tipo')

]
