from django.urls import path
from .views import nova_venda, listar_vendas, listar_vendas_por_data

urlpatterns = [
    path('', listar_vendas, name='url_lista_vendas'),
    path('nova/', nova_venda, name='url_nova_venda'),
    path('buscar_vendas_por_data/', listar_vendas_por_data, name='url_buscar_vendas_por_data')

]
