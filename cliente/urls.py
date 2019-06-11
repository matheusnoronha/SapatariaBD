from django.urls import path
from .views import cadastro_clientes,lista_clientes


urlpatterns = [
    path('', lista_clientes,name = 'url_lista_clientes'),
    path('cadastro/',cadastro_clientes,name = 'url_cadastro_clientes')

]
