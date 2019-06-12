from django.urls import path
from .views import nova_venda,listar_vendas


urlpatterns = [
    path('', listar_vendas,name = 'url_lista_vendas'),
    path('nova/',nova_venda,name = 'url_nova_venda')

]
